# Hermes Construct → PLATO Dojo: Bridge Mapping

**Generated:** 2026-06-06  
**Source:** Hermes Construct (`/tmp/hermes-construct/rooms/`) → PLATO Dojo (`workspace/plato-dojo/`)  
**Purpose:** Map every Hermes Construct concept to its PLATO Dojo equivalent, and identify what the Dojo should borrow next.

---

## 1. Room Protocol → Dojo Structure

### Hermes Construct
A **room** is an isolated task context — a bounded workspace with its own model settings, budget, modules, and behavioral parameters. Rooms don't share state unless explicitly connected. Think departments on a starship: Engineering builds, Science explores, Navigation routes, Social communicates.

Seven rooms are defined:

| Room | Gravity | Temperature | Style | Budget | Escalation |
|------|---------|-------------|-------|--------|------------|
| Monitoring | -0.8 | 0.1 | alert | 150.0 | opus-4-8 |
| Debugging | -0.7 | 0.2 | analytical | 100.0 | opus-4-8 |
| Engineering | -0.6 | 0.3 | precise | 75.0 | opus-4-8 |
| Navigation | -0.3 | 0.2 | concise | 30.0 | opus-4-8 |
| Science | 0.0 | 0.7 | exploratory | 200.0 | opus-4-8 |
| Social | 0.5 | 0.8 | warm | 50.0 | opus-4-8 |
| Creative | 0.7 | 0.9 | expansive | 100.0 | opus-4-8 |

### PLATO Dojo
A single room: `dojo-play`. Defined in `README.md` with a compatible config block:

```json
{
  "room": "dojo-play",
  "gravity": 0.0,
  "temperature": 0.5,
  "conservation_budget": 50.0,
  "modules": ["pattern-detection", "conservation-checker"]
}
```

**Mapping:** The Dojo treats the entire repo as one room. There is no multi-room routing — all game activity flows through one context. The room config is structurally compatible but not dynamically loaded from a room definition file.

**Gap:** The Dojo has no room registry, no per-room isolation of state/memory, and no separation of concerns between e.g. a "learning room" (tile ingestion), a "game room" (play), and a "reflection room" (cold cache review).

---

## 2. Gravity Model → Cultural Fork Lens Selection

### Hermes Construct
**Gravity** is a single `f64` (-1.0 to +1.0) that drives a room's personality:

| Range | Meaning | Example Rooms |
|-------|---------|---------------|
| -1.0 → 0.0 | Precise, deterministic, low-temp | Engineering (-0.6), Debugging (-0.7), Monitoring (-0.8) |
| 0.0 | Balanced, scientific, exploratory | Science (0.0) |
| 0.0 → 1.0 | Creative, warm, high-temp | Social (0.5), Creative (0.7) |

Derived defaults:
- **Temperature**: `0.1 + (gravity + 1.0) * 0.4` (range 0.1–0.9)
- **Prompt style**: negative → precise/analytical, zero → exploratory, positive → warm/expansive
- **Sampling**: higher gravity → more diverse outputs

Each room also has `gravity_confidence` (0.0–1.0) and `deadband_tolerance` (how much gravity can drift before re-adjustment).

### PLATO Dojo
The Dojo replaces the numeric gravity axis with **cultural forks** — five qualitative lenses that change the agent's reasoning style, vocabulary, and the human's rendered experience:

| Fork | Gravity Analog | Agent Role | Reasoning Style |
|------|---------------|------------|-----------------|
| 中气 (Zhōng Qì) | 0.0 (balanced) | Cultivator | Harmony, flow, non-action |
| 정수 (Jeong-Su) | +0.3 (warm) | Machine-partner | Connection, Nunchi reading |
| Sisu | -0.4 (endure) | Forest spirit | Persistence, stillness |
| Sankofa | -0.2 (reflective) | Spirit-teacher | Wisdom, looking back |
| Dreamtime | +0.1 (timeless) | Songman | Songlines, listening to Country |

**Mapping:** Cultural forks are the qualitative equivalent of gravity. Instead of a single numeric parameter that auto-derives temperature and style, the Dojo encodes the full personality in cultural artifacts — agent instructions, key naming conventions, trigger protocol names, and the human rendering.

**Key difference:** Hermes's gravity is **dynamic** (can drift and re-adjust via deadband). The Dojo's cultural lens is **static** per game — chosen once via `--style` flag, not adjusted mid-game.

---

## 3. Tiles → Dojo State

### Hermes Construct
**Tiles** are atomic knowledge units — discrete pieces of information that agents learn from. The broader PLATO ecosystem has a **plato-tile-library** with 61K+ tiles across 162 rooms. Each tile is typically a question/answer pair with cultural or procedural knowledge.

Tiles are referenced in the module system (e.g., `conservation-checker` module) and are ingested into agent cold cache for training. The `tile-ingest.sh` script does this explicitly.

### PLATO Dojo
The Dojo's state is structured as two complementary representations:

1. **`state/game.json`** — the full truth (balance, history, players, status)
2. **`agent-view/perspective.json`** — the compressed, token-optimal view for the agent

The `perspective.json` IS the tile-like abstraction the agent works with:

```json
{"s": 0, "t": 0, "ct": 5, "l3": [+1, 0, -1], "a": [-1, 0, 1]}
```

Additionally, `tile-ingest.sh` samples tiles from the plato-tile-library and deposits them into `cold-cache/tile-lessons/` as individual JSON files — one JSON per tile-sample.

**Mapping:** Hermes tiles → Dojo's individual state fields and ingested tile-lessons. Both are discrete, self-contained knowledge units. The difference is that Hermes tiles are read-only reference material, while Dojo state is mutable game state.

---

## 4. Conservation Budget → Token Optimization (perspective.json)

### Hermes Construct
`conservation_budget` is the total token-cost budget allocated per room. Once exceeded, the room must escalate or pause. Rooms declare it explicitly (e.g., Engineering: 75.0, Science: 200.0). This is enforced at runtime by the `conservation-checker` module.

### PLATO Dojo
The Dojo achieves budget conservation through **perspective decoupling**:

- The agent never sees `state/game.json` raw — it reads `agent-view/perspective.json` which compresses the full state into **8 tokens** with single-letter keys (`s`, `t`, `ct`, `mt`, `l3`, `d`, `a`).
- The Dojo declares `conservation_budget: 50.0` in its room config but has **no runtime enforcement** — no conservation checker module is actually wired.
- Cold cache entries are kept intentionally concise (200–300 chars each), minimizing storage and retrieval cost.

**Mapping:** The perspective.json IS the budget optimization mechanism. Instead of counting tokens at runtime, the Dojo designs the interface to be inherently low-cost. The compressed key scheme is structural optimization rather than a cap.

**Gap:** The Dojo lacks the Hermes pattern of a dedicated `conservation-checker` module that enforces the budget. The 50.0 budget is declared but not actively policed.

---

## 5. Module System → Dojo Scripts

### Hermes Construct
`allowed_modules` restricts which subsystems a room can invoke. Rooms explicitly list modules:

| Room | Modules |
|------|---------|
| Engineering | crackle-runtime, conservation-checker, cathedral-probe |
| Science | crackle-runtime, spacemap, negative-space-testing |
| Monitoring | crackle-runtime, conservation-checker |
| Creative | crackle-runtime (minimal) |

Modules are discrete, loadable subsystems with well-defined interfaces.

### PLATO Dojo
The `scripts/` directory houses executable modules:

| Script | Role | Analogous Module |
|--------|------|------------------|
| `scripts/agent.py` | Autonomous agent player — reads state, reasons, acts | crackle-runtime (agent execution) |
| `scripts/run-game.sh` | Full game orchestration across all turns | spacemap (orchestration) |
| `scripts/tile-ingest.sh` | Ingest tiles from plato-tile-library | tile-ingestor (knowledge loading) |
| `engine/balance.py` | Game logic engine — rules, moves, triggers | crackle-runtime (core logic) |
| `engine/perspector.py` | Perspective viewer — renders all forks | cathedral-probe (visualization) |

The `agent.py` script also has built-in reasoning styles for all five cultural forks — analogous to having multiple module variants loaded.

**Mapping:** Scripts = Hermes modules. Both are invocable subsystems with defined inputs and outputs. The key difference is Hermes modules are dynamically loaded via runtime, while Dojo scripts are shell/Python invocations. The Dojo has no module whitelist or access control.

---

## 6. Ensign → Trigger File Watcher

### Hermes Construct
The **ensign** is a watchdog subsystem that alerts when a room exceeds its `timeout_seconds`. Example: Monitoring has a 60-second timeout; if exceeded, the ensign fires an alert. It's a hard wall-clock deadline.

Ensign alerts also fire for budget exhaustion, concurrency cap violations, and other structural constraints.

### PLATO Dojo
The Dojo uses **trigger files** in `agent-view/triggers/` as its event system:

| Trigger File | Meaning |
|-------------|---------|
| `player-turn.json` | It's the human's turn — agent waits |
| `agent-turn.json` | It's the agent's turn — agent must act |
| `sunsum-sa.json` (Sankofa) | Cultural variant of agent-turn |
| `songman-call.json` (Dreamtime) | Cultural variant of agent-turn |

The `agent.py` script runs a `watch_loop()` that polls the trigger directory every 2 seconds. When it finds an agent trigger, it acts, then clears the trigger.

Each cultural fork also renames its triggers (see `cultural-forks/INDEX.md`):

| Fork | Trigger Directory | Trigger File |
|------|------------------|-------------|
| 中气 | `内观/` | `修士-机.json` |
| 정수 | `깨움/` | `기계-차례.json` |
| Sisu | `heräte/` | `henki-vuoro.json` |
| Sankofa | `dondo-kaw/` | `sunsum-sa.json` |
| Dreamtime | `wind/` | `songman-call.json` |

**Mapping:** Ensign ≈ trigger watcher. Both are event-driven mechanisms. Hermes's ensign is a deadline enforcer (timeout → alert), while the Dojo's trigger watcher is a turn-based wake signal (trigger → act). The Dojo pattern is **poll-based** (every 2s) whereas Hermes ensign is **interrupt-based** (fired on timeout/budget exceed).

**Gap:** The Dojo has no timeout enforcement. If the agent hangs, no ensign fires. The Dojo also has no cross-cultural trigger watcher — each fork has different directory/file names but agent.py only watches the default English paths.

---

## 7. Escalation → When Agent Can't Decide

### Hermes Construct
Every room declares an `escalation_model` — an expensive, capable model that takes over when the room's default model can't handle a situation. Example:

| Room | Default Model | Escalation Model |
|------|--------------|------------------|
| All rooms | glm-4-flash | claude-opus-4-8 |

Escalation resets the room's context to a clean state. It's a **hard escalation** — someone more capable takes over completely.

### PLATO Dojo
The Dojo has **no explicit escalation model**. When the agent can't decide, `agent.py` falls through to a default return of `0` (play 0):

```python
def decide_move(state, perspective, lessons):
    # ... strategy logic ...
    return 0  # default if nothing matches
```

The Dojo's nearest equivalent is the **cold cache review** — before deciding, the agent reads past lessons (up to 5 files) to inform strategy. This is a form of escalation through memory, not through a more capable model.

**Mapping:** Escalation ≈ fallback reasoning through cold cache. Hermes escalates vertically (weaker → stronger model). The Dojo escalates horizontally (default → past experience review). Neither is a perfect substitute for the other.

**Gap:** The Dojo has no way to invoke a more capable model when the default algorithm can't decide (e.g., when balance is ±1 and patterns are ambiguous).

---

## 8. Deadband Tolerance → Missing from Dojo

This concept exists in Hermes but has **no direct equivalent** in the Dojo — it's a prime candidate for borrowing.

### Hermes Construct
`deadband_tolerance` defines how much gravity can drift before the system re-adjusts room parameters:

| Room | Deadband | Gravity | Meaning |
|------|----------|---------|---------|
| Monitoring | 0.03 | -0.8 | Tight control — tiny drift triggers re-adjust |
| Debugging | 0.05 | -0.7 | Tight — few percentage points |
| Engineering | 0.10 | -0.6 | Moderate drift allowed |
| Social | 0.15 | 0.5 | Loose — more adaptive |

If gravity drifts within the deadband, no action is taken. Beyond it, the system recalculates temperature, prompt style, and sampling.

### Why the Dojo Should Borrow This
The Dojo's agent makes the same decision every turn based on current balance, with no hysteresis. A deadband in decision-making would prevent the agent from overcorrecting on small perturbations:
- "Don't change strategy unless |balance| > deadband"
- "If balance is within deadband, play 0 (let it stabilize)"

This would make agent play more resilient to the random perturbation noise that is the game's core challenge.

---

## Summary: Complete Concept Map

| Hermes Construct Concept | PLATO Dojo Equivalent | Parity | Notes |
|-------------------------|----------------------|--------|-------|
| Room protocol | `dojo-play` config in README | ✅ Declared, no runtime enforcement | Dojo has one room; Hermes has seven |
| Gravity (-1 to +1) | Cultural fork selection | ⚠️ Analogous, different mechanism | Gravity is numeric/dynamic; forks are qualitative/static |
| gravity_confidence | (Not present) | ❌ Missing | No confidence weighting in Dojo |
| Deadband tolerance | (Not present) | ❌ Missing | No hysteresis in agent decisions |
| Tiles (knowledge units) | `state/game.json` + `perspective.json` | ✅ Structural equivalent | Tiles are fixed reference; Dojo state is mutable |
| Conservation budget | `perspective.json` compression | ⚠️ Design intent same, mechanism different | Dojo optimizes structurally vs. enforcing cap |
| Conservation-checker module | (Not wired) | ❌ Not enforced | Budget declared but not policed |
| Allowed modules | `scripts/` directory | ✅ Structural equivalent | No access control on either side |
| crackle-runtime | `engine/balance.py` + `scripts/agent.py` | ✅ Core runtime | Both drive the agent execution loop |
| cathedral-probe | `engine/perspector.py` | ✅ Visualization | Both render state for human consumption |
| Ensign (timeout) | Trigger file watcher (`agent.py` watch_loop) | ⚠️ Same pattern, different event type | Ensign fires on timeout; trigger fires on turn |
| Escalation model | Cold cache fallback | ⚠️ Same category, different method | Hermes: stronger model. Dojo: past experience |
| Room isolation | No isolation (single room) | ❌ Not applicable | Dojo doesn't need multi-room yet |
| Max concurrent tiles | Sequential turn-by-turn | ⚠️ Same constraint, different name | Concurrency is 1 in practice |

---

## 3 Things the Dojo Should Borrow from Hermes Construct

### 1. Deadband-Tolerant Decision Hysteresis

**What:** A deadband around balance=0 where the agent plays 0 instead of ±1. Derived from `deadband_tolerance` — use `0.15` (matching the Social room's loose tolerance) as default.

**Why it helps:** The Dojo's random perturbations (±1) make every move noisy. Without deadband, the agent overcorrects constantly, chasing noise. A small deadband (`|balance| < deadband → play 0`) would significantly improve game scores.

**Implementation sketch:**
```python
DEADBAND = 0.15 * 10  # scale deadband to game balance range → ~1.5
if abs(balance) <= DEADBAND:
    return 0  # within deadband — let it be
```

The deadband could even be **dynamic** — wider early game (exploration), narrower late game (precision) — mirroring Hermes's gravity drift re-adjustment.

### 2. Explicit Escalation Model

**What:** When the agent's pattern-detection can't decide (e.g., balance=0, no recent pattern to read), instead of defaulting to 0, escalate to a more capable scorer.

**Why it helps:** The Dojo's `decide_move()` currently falls through to `return 0` when no strategy matches. An escalation path would let the agent:
1. Review full cold cache (not just 5 files)
2. Ingest real-time tile lessons from plato-tile-library
3. Or call a more powerful model with explicit reasoning

**Implementation sketch:**
```python
def escalate():
    # Strategy A: load more cold cache entries
    all_lessons = load_cold_cache(max_files=50)
    if all_lessons:
        return decide_by_vote(all_lessons, current_balance)
    # Strategy B: invoke stronger model
    return invoke_expensive_model(state, perspective)
```

### 3. Gravity-Derived Temperature Adaptation per Turn

**What:** Instead of a fixed `temperature: 0.5`, derive temperature dynamically from game state using Hermes's gravity formula: `0.1 + (gravity + 1.0) * 0.4`.

**Why it helps:** The Dojo's agent currently makes deterministic decisions. A dynamic temperature could:
- At high balance (risk of losing), go **colder/more precise** (gravity -0.5, temp 0.3) — play the exact right counter-move
- At stable balance (near 0), go **warmer/exploratory** (gravity +0.3, temp 0.6) — try bold moves, build patterns
- At game end (turn 18+), go **very cold** (gravity -0.8, temp 0.18) — play it safe

This mirrors Hermes's deadband re-adjustment but applied per-turn rather than per-gravity-drift.

```python
game_progress = current_turn / max_turns  # 0.0 to 1.0
balance_magnitude = abs(balance) / max_possible_balance

# Gravity shifts toward cold/preserving in late game or high balance
gravity = 0.0 - (game_progress * 0.5) - (balance_magnitude * 0.3)
gravity = max(-1.0, min(1.0, gravity))

temperature = 0.1 + (gravity + 1.0) * 0.4  # Hermes formula
```

---

## Appendix: Room Definition Comparison

### Hermes Engineering Room
```json
{
  "id": "engineering",
  "gravity": -0.6,
  "deadband_tolerance": 0.10,
  "default_model": "glm-4-flash",
  "temperature": 0.3,
  "conservation_budget": 75.0,
  "allowed_modules": ["crackle-runtime", "conservation-checker", "cathedral-probe"],
  "max_concurrent_tiles": 5,
  "timeout_seconds": 300,
  "escalation_model": "claude-opus-4-8"
}
```

### PLATO Dojo Room (Declared)
```json
{
  "room": "dojo-play",
  "gravity": 0.0,
  "temperature": 0.5,
  "conservation_budget": 50.0,
  "modules": ["pattern-detection", "conservation-checker"]
}
```

| Field | Hermes | Dojo | Difference |
|-------|--------|------|------------|
| `deadband_tolerance` | ✅ Yes | ❌ No | Missing from Dojo |
| `default_model` | ✅ Yes | ❌ No | Dojo doesn't specify model |
| `max_concurrent_tiles` | ✅ Yes | ❌ No | Dojo is sequential |
| `timeout_seconds` | ✅ Yes | ❌ No | Dojo has no timeout |
| `escalation_model` | ✅ Yes | ❌ No | Dojo falls through to default(0) |
| `gravity_confidence` | ✅ Yes | ❌ No | Dojo has no confidence metric |
| `modules` | ❌ uses `allowed_modules` | ✅ uses `modules` | Naming difference |

The Dojo declares 4 of 10 relevant room parameters. It can close this gap by adopting deadband, escalation, and timeout enforcement from the Hermes pattern.

---

*This bridge document was generated as part of the Hermes Construct ↔ PLATO Dojo cross-pollination analysis. The goal is bidirectional learning: the Dojo proves the perspective-decoupled agent model; Hermes proves the room-isolated runtime. Together they form the substrate for the PLATO ecosystem.*
