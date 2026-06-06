# SKILL: Play Ternary Balance

## Summary
Play a turn of Ternary Balance — keep balance closest to 0.

## Trigger
When `agent-view/triggers/agent-turn.json` appears, it's your turn.

## Reading State
Read `agent-view/perspective.json` for the compressed view:
- `s`: current balance (target is 0)
- `ct`: current turn
- `mt`: max turns
- `l3`: last 3 moves (your and opponent's)
- `a`: available moves [-1, 0, +1]

## Strategy
- If balance is positive, try -1 to bring it back
- If balance is negative, try +1
- If balance is 0, try 0 (safe) or +/-1 for advanced play
- Random perturbations will knock you off course — adapt

## Acting
1. Run: `python3 engine/balance.py move agent <delta>`
2. Remove trigger: `rm agent-view/triggers/agent-turn.json`
3. Write reasoning to: `cold-cache/turn-<number>.md`

## Learning
After game ends:
- Read `cold-cache/` to review mistakes
- Write a new strategy to this file if you learned something
