# Human View — The Vibe Render

This directory contains the human-facing rendering of the PLATO Dojo game.

## How It Works

The human view reads the same `state/game.json` file that the agent uses, but renders it differently.

## Rendering Ideas

### Minimal Terminal UI
```bash
# Watch the game state
watch -n 1 python3 -c "
import json
s = json.load(open('state/game.json'))
print(f\"Balance: {s['balance']:+d}\")
print(f\"Turn: {s['current_turn']}/{s['max_turns']}\")
print(f\"History: {[m['delta'] for m in s['history'][-5:]]}\")
"
```

### Vibe-Coded Visual
A human could build:
- A 3D balance beam with Three.js
- A sound-reactive visualization
- A medieval scale with sound effects
- A space-themed particle display

The state is the same JSON. The render is whatever the human wants.

## Input
To make a move as human:
```bash
python3 engine/balance.py move player <delta>
```
