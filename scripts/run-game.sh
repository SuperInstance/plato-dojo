#!/usr/bin/env bash
# PLATO Dojo — Full Game Runner
# Runs a complete 20-turn game with all five cultural perspectives
set -euo pipefail

DOJO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DIFFICULTY="${1:-easy}"
STYLE="${2:-sankofa}"

echo "============================================"
echo "  🌏 PLATO Dojo — Full Game"
echo "  Difficulty: $DIFFICULTY"
echo "  Agent lens: $STYLE"
echo "============================================"
echo ""

# Fresh game
cd "$DOJO_DIR"
python3 engine/balance.py new "$DIFFICULTY" > /dev/null

# Play all turns
for i in $(seq 1 20); do
  # Human turn (random reasonable move)
  RAND_MOVE=$((RANDOM % 3 - 1))  # -1, 0, or +1
  python3 engine/balance.py move player "$RAND_MOVE" > /dev/null 2>&1

  # Agent turn
  python3 scripts/agent.py --one-shot --style "$STYLE" > /dev/null 2>&1

  # Print state
  python3 -c "
import json
s = json.load(open('$DOJO_DIR/state/game.json'))
h = s['history']
if len(h) >= 2:
    p_move = h[-2]
    a_move = h[-1]
    print(f'  Turn {s[\"current_turn\"]//2:2d}: player={p_move[\"delta\"]:+d}(p{p_move[\"perturbation\"]:+d}) → balance={p_move[\"balance_after\"]:+3d} | agent={a_move[\"delta\"]:+d}(p{a_move[\"perturbation\"]:+d}) → balance={a_move[\"balance_after\"]:+3d}')
"

  # Check game over
  GAME_STATUS=$(python3 -c "import json; print(json.load(open('$DOJO_DIR/state/game.json'))['status'])")
  if [ "$GAME_STATUS" = "game_over" ]; then
    echo ""
    echo "  🏁 Game over at turn $((i))"
    break
  fi
done

# Final analysis
echo ""
echo "============================================"
echo "  📊 Game Summary"
echo "============================================"
python3 -c "
import json
s = json.load(open('$DOJO_DIR/state/game.json'))
final = s['balance']
moves = [m['delta'] for m in s['history']]
pert = [m['perturbation'] for m in s['history']]
agent_moves = [m for m in s['history'] if m['actor'] == 'agent']

print(f'  Game:      {s[\"game_id\"]}')
print(f'  Turns:     {s[\"current_turn\"]}')
print(f'  Final bal: {final:+d}')
print(f'  Moves:     {moves}')
print(f'  Perterb:   {pert}')
print(f'')
print(f'  Agent stats:')
print(f'    Moves:    {len(agent_moves)}')
print(f'    Avg delta: {sum(m[\"delta\"] for m in agent_moves)/len(agent_moves):+.2f}' if agent_moves else '    (none)')

# Score
print(f'')
p_score = s.get('players', {}).get('player', {}).get('score', 0)
a_score = s.get('agents', {}).get('agent', {}).get('score', 0)
print(f'  Player score: {p_score}')
print(f'  Agent score:  {a_score}')
if p_score < a_score:
    print(f'  🏆 Player wins (closer to 0)')
elif a_score < p_score:
    print(f'  🤖 Agent wins')
else:
    print(f'  🤝 Tie!')
"

echo ""
echo "All perspectives at end state:"
python3 engine/perspector.py

echo ""
echo "Agent cold cache entries:"
ls cold-cache/agent-*.md 2>/dev/null | wc -l
echo "  stored in cold-cache/"
