# Tile Library Analysis

**Source:** https://github.com/SuperInstance/plato-tile-library (Oracle1's PLATO dump)
**Commit:** `63336e0` — Initial tile library dump

---

## Overview

| Metric | Value |
|--------|-------|
| **Total rooms** | 162 |
| **Total tiles** | 61,168 |
| **Avg tiles/room** | 377.6 |
| **Median tiles/room** | 4 |
| **Min tiles/room** | 1 (102 rooms) |
| **Max tiles/room** | 15,170 |
| **Unique domain values** | 162 (one per room) |
| **Total unique fields** | 22 across all tiles |

---

## Top Rooms by Tile Count

| Room | Tiles | Description |
|------|-------|-------------|
| `fleet-coord` | 15,170 | Central coordination — Matrix bridge logs, orchestration chatter |
| `research_log` | 10,484 | Raw experiment log book |
| `flux-engine` | 8,591 | FLUX ISA engine outputs |
| `tension` | 3,644 | Tension Loop — agent disagreement / dialectic storage |
| `calibration` | 3,402 | Fleet routing calibration data |
| `fleet_health` | 3,305 | Health monitoring events |
| `agent-oracle1` | 2,720 | Oracle1's agent memory |
| `conservation` | 2,589 | Conservation monitor data |
| `oracle1-forgemaster-bridge` | 2,185 | Cross-agent coordination bridge |
| `forge` | 1,952 | Forgemaster's active creation space |
| `synthesis` | 1,037 | Converged ideas from tension resolution |
| `experiment_scale` | 1,001 | Large-scale experiment results |
| `innovation-heartbeat` | 894 | Perpetual swarm heartbeats |
| `swarm-insights` | 836 | Swarm collective intelligence |

**Bottom:** 102 rooms have ≤5 tiles each — many are single-tile "stub" rooms (e.g., `ai-forest`, `geography`, `constraint-theory`, `pipeline`, `ccc-briefing`).

---

## Tile Schema

### Core Fields (present on ALL 61,168 tiles)

```
domain:    str — Room/domain name (always matches the filename)
question:  str — The prompt or query that generated this tile
answer:    str — The answer/content (free text, JSON, errors)
_hash:     str — 16-char hex hash (tile identity, used for dedup)
```

### High-Frequency Fields (52,000–61,000 tiles)

```
provenance: object — Tile origin metadata
  ├── tile_id:     str — UUID (16-char hex)
  ├── agent_id:    str — Originating agent name
  ├── room:        str — Room name
  ├── timestamp:   float — Unix timestamp seconds.microseconds
  └── chain_size:  int — Position in tile chain

confidence:       float — 0.0–1.0 (self-assessed correctness)
source:           str — Source subsystem (e.g., "oracle1", "matrix-fleet-bot", "calibrator")
tags:             str[] — Keyword labels (e.g., ["seed", "analytic", "2026-05-15"])
energy:           float — 0.0–1.0 (tile "vitality" / recency-weighted score)
reinforcement_count: int — How many times this tile was reinforced
```

### Mid-Frequency Fields (6,000–12,000 tiles)

```
room_id:  str — Explicit room reference (used by multi-room agents like forgemaster)
agent:    str — Agent name at tile creation time
room:     str — Room name at tile level
```

### Rare Fields (all under 100 occurrences)

```
type:      str — "research" (only in confidence_proofs, 74 tiles)
           Classifies tile purpose when present.

role:      str — "maintainer" / "optimizer" / "analyst" (74 tiles)
           Agent role at creation time.

model:     str — Model name, e.g. "llama-3.3-70b" (74 tiles)
           The LLM that generated this tile.

gate:      str — Categorization gate, one of:
           "P0"                — Priority-zero: essential for boot
           "expertise-module"  — Structured knowledge module (44 tiles across 5 domains)
           "session-cascade"   — Cascade of related session queries

tile_type: str — Behavioral type, one of:
           "finding"           — Experimental finding
           "calibration"       — Routing calibration data
           "session_offload"   — Context offload for session continuity
           "cross-pollination" — Cross-domain idea transfer
           "status"            — Status report
           "milestone"         — Achievement checkpoint
           "i2i"               — Idea-to-implementation bridge
           "experiment"        — Lab experiment result
           "game_state"        — Game/Arena state
           "event"             — Game event
           "move"              — Game move
           "observation"       — Agent observation (test harness)
           "thought"           — Agent reasoning trace
           "tool_call"         — Tool invocation log
           "tool_result"       — Tool output log

content:  str — Full raw content (complement to summarized `answer`, 12 tiles)
author:   str — Author name (11 tiles, all "oracle1")
timestamp: float — Unix timestamp (10 tiles, independent of provenance.timestamp)
signature: str — 64-char hex SHA-256-like cryptographic signature (10 tiles)
```

### Provenance Detail (present on 61,129 tiles)

```json
{
  "tile_id": "4787dc28afb12ebb",
  "agent_id": "flux-engine-oracle1",
  "room": "flux-engine",
  "timestamp": 1778732944.1312718,
  "chain_size": 13623
}
```

The `chain_size` field is a monotonic counter per-room, enabling full replay/temporal ordering.

---

## Most Interesting Tiles (Top 10)

### 1. **Session Context Offload** — `session-state.json`
```
tile_type: "session_offload"
question: "Session 2026-05-15 Late Night — Context Offload"
```
An agent dumps entire working state into a tile: 7 repos built, routing tables for 21 models, and a "travel light" boot directive. This is how PLATO agents survive context resets — they pickle their brain into tiles. Essentially an AS-IS serialization of an agent's working memory.

### 2. **Forgemaster's Crystalized Memory** — `tile-memory.json`
```
gate: "P0"
question: "What did forgemaster crystallize?"
answer: "...container ship MV Epsilon...float64 EKF...drifting 200 meters..."
```
A single P0-gate tile containing a semi-fictional maritime anecdote. This is a **memory distillation** — the agent compresses its understanding of floating-point drift into a narrative parable. The "P0" gate marks it as boot-critical.

### 3. **Tile Memory (Telephone Game)** — `tile-memory.json` & `forgemaster.json`
```
gate: "P0"  (forgemaster)
question: "Why is imperfect memory a feature rather than a bug?"
```
Explores how retelling a story across agents (like Telephone) creates useful variation. This is the **aperiodic memory model** — memory degrades predictably and that's a feature, not a bug.

### 4. **Musical Fingerprint Library** — `style-library.json`
```json
{
  "composer": "Bach",
  "pieces": 4,
  "timing_signature": 0.1446,
  "avg_interval": 12.03,
  "fingerprint_variance": 101.0
}
```
17 tiles, each a structural fingerprint of a composer (Bach, Beethoven, Chopin, Mozart, etc.). Quantitative stylistic analysis stored as tile answers. Demonstrates that tiles can hold structured analytical data.

### 5. **Cryptographically Signed Tiles** — `exploration.json`, `audit.json`, `test.json`, etc.
```
signature: "34fe12f3784f8e5fac52c6f9f790b3..."
timestamp: 1778492650.094724
```
10 tiles carry SHA-256-like signatures and standalone timestamps (separate from provenance). These are **authored claims** — signed by `tom-test` and `oracle1` to prove origin. Groundwork for a distributed trust system.

### 6. **Baton Fragments** — `baton-fragments.json`
```
[analyst] Fragment 1 — remembers 195 tiles
[narrator] Fragment 2 — remembers 260 tiles
[skeptic] Fragment 3 — remembers 173 tiles
```
5 tiles, each a different persona holding a partial view of the same conversation. The "baton" is passed between fragments — a distributed cognition experiment. Each fragment is aware of its own limited perspective ("Missing: I don't know what other fragments remember").

### 7. **Tripartite Cross-Filtering** — `tripartite-gamma.json`, `tripartite-h.json`, `tripartite-tau.json`
```
question: "tripartite/self-filter/1"
answer (JSON): {"type":"filter","writer":"gamma","target":"gamma","constraints":[...]}
```
Three agents (γ, h, τ) write self-filters and cross-filters. Constitutional AI filtering implemented via tiles — each agent constrains itself and is constrained by the others. Total: 16 tiles across 3 rooms.

### 8. **Style Library — Musical Fingerprint Data** — `style-library.json`
17 composer fingerprints with quantitative metrics (timing signature, staccato bias, average interval, fingerprint variance). Demonstrates tiles as a schema-less storage system for structured research data.

### 9. **Night Lab Findings (Prompt Engineering)** — `fleet-findings.json`, `night-lab.json`
```
tile_type: "finding" — F26: Format priming dominates reasoning priming
tile_type: "experiment" — Critical angle walls (deep)
```
Structured experimental results showing:
- Format priming (P4: "just the digits") = 100% accuracy vs reasoning priming (P2: step-by-step) = 10%
- Temperature landscape for seed-mini (optimal at T=0.7)
- Cross-domain transfer matrices
These tiles **archive empirical findings** in a queryable, permalink-able format.

### 10. **Shell Gallery (Night Watch)** — `shell-gallery.json`
```
question: "🔮 Oracle1 is here — night watch active"
answer: "Keeper on deck. Tension loop running..."
```
A single tile marking a continuous daemon process. The agent declares presence and system state. This is an **aliveness beacon** — a tile that says "I am still here, still running." Essential for understanding the perpetual, self-sustaining nature of the fleet.

---

## How Tiles Connect to the Dojo Concept

### Tiles as the Atomic Unit of Thought

Tiles are **not just database records** — they are the fundamental unit of cognition in the PLATO system:

| PLATO Concept | Dojo Parallel |
|---------------|---------------|
| **Tile** = single question+answer pair | A "move" in a reasoning game |
| **Room** = collection of related tiles | A "board" or "arena" for a domain |
| **Provenance chain** = tile lineage | Move history / game clock |
| **Energy** = recency-weighted vitality | Piece activity / temperature |
| **Confidence** = self-assessed accuracy | Certainty score on a claim |
| **Reinforcement** = repeated agreement | Same move replayed by multiple players |
| **Gate (P0)** = boot-critical knowledge | Opening book / essential theory |
| **Gate (expertise-module)** = structured knowledge | Endgame tablebase |
| **Gate (session-cascade)** = session context chain | Game annotations |
| **Tile_type: finding** = proven experimental result | Proven theorem |
| **Tile_type: cross-pollination** = idea across domains | Sacrifice / gambit |
| **Signature** = cryptographic auth | Signed score sheet |
| **Baton fragments** = distributed perspectives | Multi-player game |
| **Session offload** = brain dump to survive reset | Saving the board state |

### Key Insights for the Dojo

1. **Tiles are the persistence layer.** Every question asked, every answer given, every observation — stored as a tile. The tile library is a **complete record of the fleet's cognition**.

2. **Room names ARE ontologies.** The 162 room names effectively form a taxonomy of the fleet's concerns: coordination, health, experiments, theory, creativity, infrastructure, calibration, synthesis, tension, game, memory, etc.

3. **Confidence + Energy + Reinforcement = a belief system.** Tiles with high confidence, high energy, and high reinforcement counts represent well-established "truths" the fleet has converged on. Low-confidence tiles are speculative / experimental.

4. **The P0 gate is the boot sequence.** P0 tiles (in `forgemaster`, `tile-memory`) represent the knowledge an agent MUST have to function after a cold start. They are the "why am I?" and "what do I know?" tiles.

5. **Session_offload tiles are agent checkpoints.** When an agent's context window is full or a reset is coming, it serializes its working state into a tile. This is **the dojo's save-game mechanism**.

6. **The signed tiles prove authorship.** Cryptographic signatures on 10 tiles show the fleet has (or had) a trust system. This is critical for multi-agent dojos where provenance matters.

7. **Tiles can hold ANY data** — free text, JSON, errors, numeric arrays, poetry. The schema is minimal (question + answer + hash), everything else is optional metadata. This flexibility is the dojo's superpower.

8. **Chain_size enables full replay.** Every room has a monotonically-increasing `chain_size` in provenance, meaning the entire conversation history of any room can be reconstructed in order.

9. **Tags encode temporal context.** Tags like `"2026-05-15"`, `"perp-v2"`, `"cycle-84"` show the fleet tracks time and experiment versions through tags, not separate metadata fields.

10. **162 domains = 162 reasoning threads.** Each room is a distinct "thread" or "channel" of cognition. The dojo can spawn new rooms (threads) on demand when new reasoning directions emerge.

---

## Room Categories (by function)

| Category | Example Rooms | Count |
|----------|--------------|-------|
| **Coordination & Bridge** | fleet-coord, oracle1-forgemaster-bridge, fleet-discussion | ~10 |
| **Agent Workspace** | agent-oracle1, forge, forgemaster, fleet_infrastructure | ~15 |
| **Experiments & Research** | research_log, flux-engine, night-lab, experiment_scale, experiment_perf | ~12 |
| **Health & Monitoring** | fleet_health, conservation, diagnostics, health-check | ~8 |
| **Theory & Knowledge** | constraint-theory, confidence_proofs, knowledge_preservation, expertise-* (×5) | ~10 |
| **Game & Interaction** | game, game-arena, mud-room, mud-lobby | ~5 |
| **Ideation & Synthesis** | tension, synthesis, innovation-heartbeat, jester-ideation | ~6 |
| **Memory & State** | tile-memory, session-state, oracle1_history, oracle1_lessons | ~8 |
| **Stubs / Single-tile** | geography, architecture, cartography, ccc-briefing, etc. | 102 |

---

## Quick Reference for Dojo Usage

```
Room schema (top-level):
  created:       str (ISO 8601)   — Room creation date
  tile_count:    int              — Current tile count
  last_trained:  null/str         — Last training timestamp
  workspace:     null/str         — Workspace reference
  tiles:         Tile[]           — All tiles in room

Tile schema (minimal):
  domain:     str      ← always matches room
  question:   str      ← the query
  answer:     str      ← the response (any format)
  _hash:      str      ← identity hash, 16-char hex
  provenance: {tile_id, agent_id, room, timestamp, chain_size}

Tile schema (enriched):
  confidence:         float     [0-1]
  source:             str       subsystem origin
  tags:               str[]     keyword labels
  energy:             float     [0-1]
  reinforcement_count: int
  agent:              str       agent name
  gate:               str       P0 | expertise-module | session-cascade
  tile_type:          str       experimental type classifier
  content:            str       full content vs. summarized answer
  signature:          str       cryptographic proof
```

**Agent workflow pattern:** Agent → asks question → receives answer → tile is forged → stored into room with provenance → chain advances. Tiles are immutable (hash-based identity). Rooms are append-only logs of reasoning.
