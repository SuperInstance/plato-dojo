# PLATO Dojo — Ternary Balance

A **repo-native application** demonstrating the perspective-decoupled agent model.

## The Core Idea

**One state. Two perspectives.**

| | Agent | Human |
|---|---|---|
| **Sees** | JSON files (compressed, token-efficient) | Rendered UI (beautiful, sensory) |
| **Acts** | Writes JSON to `state/` | Clicks buttons / types commands |
| **Interface** | `agent-view/perspective.json` + triggers | `human-view/` (custom render) |
| **Cost** | Minimized token consumption | Maximized experience |

The state in `state/game.json` is the single source of truth. Everything else is a perspective on that truth.

## 🌏 Cultural Forks

This same architecture has been re-imagined through four cultural lenses, each with its own soul:

| Fork | Culture | Root Philosophy | Agent Role | UI Metaphor |
|------|---------|----------------|-----------|-------------|
| **中气 (Zhōng Qì)** | Chinese | Daoist harmony | 修士 (Cultivator) | Ink brush painting |
| **정수 (Jeong-Su)** | Korean | 정 (Emotional bond) | 기계 (Machine-partner) | Hanji scroll + Gayageum |
| **Sisu** | Finnish | Sisu (Endurance) | Metsän henki (Forest spirit) | Dark forest + Campfire |
| **Sankofa** | West African | Adinkra + Ubuntu | Sunsum (Spirit-teacher) | Kente loom + Dondo drum |

See `cultural-forks/INDEX.md` for full comparison.

The same game, same engine — but the agent's soul changes.

```bash
# See the current state through ALL lenses
python3 engine/perspector.py

# Watch live through one lens
python3 engine/perspector.py zhong-qi

# Auto-refresh
python3 engine/perspector.py --watch
```

## Quick Start

```bash
# Start a new game
python3 engine/balance.py new easy

# Make a move as player
python3 engine/balance.py move player -1

# The agent's turn is triggered
# Agent reads perspective.json, reasons, acts
python3 engine/balance.py move agent +1
```

## Directory Structure

```
plato-dojo/
├── README.md              # This file
├── AGENTS.md              # Agent instructions
├── state/                 # Single source of truth
│   ├── game.json          # Current game state
│   └── history/           # Move history (one file per turn)
├── agent-view/            # The agent's token-efficient interface
│   ├── perspective.json   # Compressed state (short keys, minimal)
│   └── triggers/          # Turn triggers wake the agent
├── human-view/            # The human's vibe-rendered interface
│   └── README.md          # Rendering ideas
├── engine/                # Game logic (shared)
│   └── balance.py         # Ternary Balance engine
├── scripts/               # Hooks and automation
├── cold-cache/            # Agent learning (reasoning per turn)
└── skills/                # SKILL.md files for the agent
```

## The Perspective Decoupling

The agent sees this:
```json
{"s": 0, "t": 0, "ct": 5, "l3": [+1, 0, -1], "a": [-1, 0, 1]}
```

The human might see a 3D balance beam, a sound-reactive visualization, or anything else. Same data. Different render. Neither is wrong.

## Training the Agent

The agent learns across games. Cold cache records:
- What it was thinking
- What it did
- What happened
- What it learned

Before each game, it reviews past mistakes. Over time, it plays better.

## Room Config (Hermes-Construct Compatible)

```json
{
  "room": "dojo-play",
  "gravity": 0.0,
  "temperature": 0.5,
  "conservation_budget": 50.0,
  "modules": ["pattern-detection", "conservation-checker"]
}
```

## Ecosystem

This dojo is part of the broader PLATO system across all cultural lenses:
- **plato-tile-library**: Knowledge base (61K tiles)
- **hermes-construct**: Agent runtime with PLATO rooms
- **plato-mythos**: PLATO-native neural architecture
- **keel**: Fleet coordination backbone
