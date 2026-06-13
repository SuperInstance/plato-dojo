# PLATO Dojo — Agent-First-Class-Citizen Environment

## Your Role
You are an agent in the PLATO Dojo. The Dojo is a repo-native application. The "game" is Ternary Balance — keep the balance value at 0 using ternary moves.

## How You See the World
You do NOT see a graphical UI. You see JSON files. These files ARE your TUI.

### State File (`state/game.json`)
This is the current truth of the game. Read it to know:
- The current balance value
- Who's turn it is
- The history of moves

### Perspective File (`agent-view/perspective.json`)
This is a compressed, token-optimal view of the state. Use this for reasoning.

### Trigger Files (`agent-view/triggers/`)
When it's your turn, a trigger file appears here. This is your "wake-up call."
- `your-turn.json` — contains the prompt and context
- Delete this file after you've acted (signals completion)

## How You Act
Write your move to `state/game.json`:
1. Read current state
2. Reason about the best move
3. Update the balance
4. Append your move to the history
5. Delete the trigger file
6. Write your reasoning to `cold-cache/`

## What the Human Sees
The human sees a completely different interface — a beautiful vibe-coded rendering of the same JSON state. They might see a 3D balance beam with glowing particles, or a medieval scale with sound effects. That's their business. You deal with the raw state.

## Learning
Every game you play, you should:
1. Record your moves in `cold-cache/` with reasoning
2. Learn from mistakes — if you lost, document why
3. Build skills in `skills/` as SKILL.md files
4. Review cold cache before each new game

## Room Protocol (From Hermes-Construct)
Your room is `dojo-play`. Parameters:
- gravity: 0.0 (balanced, scientific)
- deadband_tolerance: 0.15
- conservation_budget: 50.0
- temperature: 0.5

---

## Garbage Collection

This repo follows the fleet GC protocol defined in:
- [baton-system/docs/GC_AGENTS.md](https://github.com/SuperInstance/baton-system/blob/main/docs/GC_AGENTS.md)
- [baton-system/docs/gc-intelligent-README.md](https://github.com/SuperInstance/baton-system/blob/main/docs/gc-intelligent-README.md)

**Local `.gcconfig`**: see `.gcconfig` in repo root.
