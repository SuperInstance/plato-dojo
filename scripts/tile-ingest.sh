#!/usr/bin/env bash
# Tile Ingestion — Ingest knowledge from plato-tile-library into agent's cold cache
set -euo pipefail

TILE_LIB="${1:-/tmp/plato-tile-library}"
DOJO_DIR="/home/ubuntu/.openclaw/workspace/plato-dojo"
COLD_CACHE="${DOJO_DIR}/cold-cache"
STATE_DIR="${DOJO_DIR}/state"

echo "=== PLATO Tile Ingestion ==="

# 1. Check if tile library exists, clone if not
if [ ! -d "$TILE_LIB" ]; then
  echo "📦 Cloning plato-tile-library..."
  git clone --depth 1 https://github.com/SuperInstance/plato-tile-library.git "$TILE_LIB" 2>/dev/null || {
    echo "⚠️  Could not clone. Will read local tiles."
    TILE_LIB="/dev/null"
  }
fi

# 2. Discover rooms and count tiles
echo "🔍 Scanning tiles..."
ROOM_COUNT=0
TILE_COUNT=0

if [ -d "$TILE_LIB/rooms" ]; then
  for roomfile in "$TILE_LIB/rooms"/*.json; do
    ROOM_COUNT=$((ROOM_COUNT + 1))
    ROOM=$(basename "$roomfile" .json)
    TILES=$(python3 -c "
import json
with open('$roomfile') as f:
    d = json.load(f)
tiles = d.get('tiles', d.get('questions', d.get('items', [])))
print(len(tiles))
" 2>/dev/null || echo "0")
    TILE_COUNT=$((TILE_COUNT + TILES))
    echo "  Room: $ROOM — $TILES tiles"
  done
fi

echo "📊 Total: $ROOM_COUNT rooms, $TILE_COUNT tiles"
echo ""

# 3. Sample tiles into cold cache for agent training
mkdir -p "${COLD_CACHE}/tile-lessons"
SAMPLE_COUNT=0

if [ -d "$TILE_LIB/rooms" ]; then
  for roomfile in "$TILE_LIB/rooms"/*.json; do
    ROOM=$(basename "$roomfile" .json)
    
    python3 -c "
import json, random
with open('$roomfile') as f:
    d = json.load(f)
tiles = d.get('tiles', d.get('questions', d.get('items', [])))
sample = random.sample(tiles, min(5, len(tiles)))
for i, t in enumerate(sample):
    entry = {
        'room': '$ROOM',
        'question': t.get('question', t.get('q', '?')),
        'answer': str(t.get('answer', t.get('a', t.get('response', ''))))[:200],
        'adinkra': t.get('adinkra', t.get('symbol', '—')),
        'principle': t.get('principle', t.get('lesson', '')),
    }
    filename = f\"${COLD_CACHE}/tile-lessons/$ROOM-sample-{i}.json\"
    with open(filename, 'w') as out:
        json.dump(entry, out, indent=2)
    print(f'  Wrote {filename}')
" 2>/dev/null
    
    SAMPLE_COUNT=$((SAMPLE_COUNT + 5))
  done
fi

echo ""
echo "✅ Ingested $SAMPLE_COUNT tile samples into cold-cache/tile-lessons/"
echo ""
echo "=== Done ==="
