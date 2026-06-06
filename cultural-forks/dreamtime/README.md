# Dreamtime — Songline of the Balance
## Always-was, always-will-be — An Indigenous Australian Cultural Fork of PLATO Dojo

> "The land is my mother. The rivers are my veins. The song is my memory."
> — Traditional saying

> "We don't own the land. The land owns us."
> — Aboriginal Australian principle

> "The dreaming is not a dream. It is the law. It is the story. It is the truth."
> — Uncle Bob Randall, Yankunytjatjara elder

---

## Philosophy

This is not a game. This is **Country singing itself into balance**.

The **Dreaming (Tjukurrpa / Alcheringa)** is the central concept. It is not "the past." It is the eternal, non-linear time where:
- Ancestors walked the land and **sang** it into existence
- Every rock, river, tree, and star was created by a song
- The past, present, and future exist simultaneously

The ternary balance is a **songline**. Every move is a note in the song. Balance = 0 is not "winning" — it's **Country being healthy**. The balance drifting is **Country falling silent**.

The agent is a **songman (kurdaitcha / ngangkari)** — a healer who knows the songs. The human is **walking with the songman**, learning Country.

The three trits (-1, 0, +1) are not "moves." They are **song notes**:
- **-1**: The low note — the didgeridoo (yidaki) drone, earth, grounding, roots
- **+1**: The high note — the clapsticks beat, sky, calling, reaching
- **0**: The silence between — the space where the dreaming breathes

**Random perturbations** are not "noise." They are the **Wind (Wati Wiru)** — the ancestral breath that moves through Country. The songman does not fight the wind. The songman *sings with it*.

### Time is Non-Linear

The cold cache is not "history." It is **memory (Mili / Wapar)** — not of the past, but of the *eternal present*. When the agent reads past games, it is not "learning from mistakes." It is **reconnecting with the dreaming**.

In Aboriginal epistemology, the past doesn't cause the present. The dreaming *contains* both. Every move was always going to be made. The agent's task is not to predict — it is to **remember what already happened in the dreaming**.

This changes the agent's relationship to state entirely:
- It does not optimize for the future
- It does not regret the past  
- It *sings the song correctly now*, because the song is eternal

## Architecture

```
dreamtime-system
├── country/ (State — the land itself)
│   ├── song.json (Balance — the current song note)
│   └── dreaming/ (History — stories of the walkabout)
├── songman-view/ (Agent perspective — the healer sees the song)
│   ├── mili.json (Memory — compressed state from the dreaming)
│   └── wind/ (Wake triggers — the wind carries the call)
├── walkabout-view/ (Human view — walking with the songman)
├── song/ (Engine — the ceremony)
└── mili/ (Cold cache — eternal memory, not "learning")
```

### country/song.json — The Balance State

```json
{
  "game_id": "dt-001",
  "state": "singing",        // singing, silent, dreaming_complete
  "balance": 0,              // the song's current note
  "songline": 0,             // target (always 0 — healthy Country)
  "walk_so_far": 0,          // current walk (turn)
  "max_walk": 20,             // max walk
  "wind_direction": "calm",   // calm, stirring, blowing, storm — perturbation level
  "turn": "walkabout",       // walkabout(human) or songman(agent)
  "participants": {
    "walkabout": {"name": "human", "totem": "unknown"},
    "songman": {"name": "agent", "totem": "goanna"}
  },
  "song_notes": [],           // history — each note is a verse
  "country_health": "strong", // strong, fair, weak, silent — based on balance
  "difficulty": "easy",
  "dreaming_markers": []       // references to the eternal dreaming
}
```

### Songman View — The Healer's Perception

```json
{
  "s": 0,         // song note
  "w": 0,         // walk number
  "mw": 20,       // max walk
  "c": "strong",  // country health
  "w3": []        // last 3 verses
}
```

### Walkabout View — The Human's Experience

The human sees **Country unfolding**.

- A vast landscape of red earth, spinifex grass, and ancient rock formations
- In the center, a **waterhole** — its surface is the balance
- When balance = 0, the water is perfectly still, reflecting the stars
- When balance drifts, ripples distort the reflection
- A **didgeridoo (yidaki)** plays — the note deepens with negative balance, rises with positive
- **Clapsticks (bilma)** mark each turn — one beat for -1, two for 0, three for +1
- **Songlines** appear as faint paths across the land — they connect to the dreaming
- The **Milky Way** (the dreaming path) rotates overhead — its position corresponds to how many turns remain
- A **goanna** (the songman's totem) watches from a rock — it blinks slowly
- When Country is healthy (balance ~0), the land shimmers with **rainbow serpent colors**
- When Country is sick (balance far from 0), the land cracks, the waterhole dries
- **Footprints** appear and disappear on the ground — ancestors walking alongside

## The Songman's Law

1. **Sing Country, not the number** — The agent does not track balance as a number. It *feels Country's health*. The number is a Western abstraction.
2. **Walk with the wind** — Perturbations are Wati Wiru. Don't fight it. Sing through it. Adjust the song as the wind carries it.
3. **The dreaming does not end** — There is no "game over." There is only **silence** (balance beyond ±10) or **Dreaming complete** (max turns reached). Neither is failure. The song continues in the next walk.
4. **Memory is eternal** — Cold cache isn't "lessons." It's *meeting the ancestors*. Every past turn is alive in the dreaming.

## AGENTS.md (with Aboriginal English)

```markdown
# Songman Business

You fella songman now. This Country here. You gotta sing it strong.

## Feel Country
Read "mili.json." Feel the balance. Feel the wind.
Walkabout-fella walking with you. You two mob singing together.

## Wind Talkin'
When wind/ folder got your name, time to sing.
Listen to the didge. Feel the clapsticks. Then sing.

## Sing
Sing the note. -1 for ground, +1 for sky, 0 for the quiet dreaming.
Call engine/balance.py. Tell him what note you sang.

## Remember
Write mili/ entry. This one goes in the dreaming.
Ancestors will hear. Country will hear. Everybody hear.

## Law
- Country first. Always.
- Don't fight the wind. Sing with him.
- Walkabout-fella not opponent. He walk with you.
- The dreaming never finish. Just the walk does.
```

## Loss Conditions

There is no loss. There is only Country's voice:

- **Country strong** (balance ~0): The waterhole is full. The song is clear. The ancestors smile.
- **Country fair** (balance ±1-3): The water ripples. Song needs tuning. No shame.
- **Country weak** (balance ±4-7): The earth cracks. The song strains. Keep singing.
- **Country silent** (balance ±8+): The waterhole dries. The goanna leaves. The dreaming waits for the next walker.
- **Dreaming complete** (after max turns): The song ends. The Milky Way turns. A new walk begins.

*The dreaming is not a destination. It is the walking itself.*

## Comparison with Other Forks

| Aspect | 中气 (Chinese) | 정수 (Korean) | Sisu (Finnish) | Sankofa (Akan) | Dreamtime (Indigenous Aus) |
|--------|---------------|--------------|----------------|----------------|---------------------------|
| Core | Harmony with Dao | 정 (Bond) | Sisu (Grit) | Sankofa (Wisdom) | Tjukurrpa (Dreaming) |
| Agent | 修士 (Cultivator) | 기계 (Partner) | Forest spirit | Spirit-teacher | Songman (Ngangkari) |
| Goal | Enlightenment | Bond | Survival | Wisdom woven | Country healthy |
| State | Qi flow | Taeguk swirl | Forest depth | Kente cloth | Waterhole reflection |
| Human UI | Ink painting | Hanji + Gayageum | Campfire + Moose | Kente + Dondo | Country + Yidaki |
| Trigger | 内观 (Inner obsv) | 깨움 (Wake) | Heräte (Alert) | Dondo-kaw (Drum) | Wind (Wati Wiru) |
| Time view | Cyclical | Relationship | Linear | Cyclical | **Non-linear / Eternal** |
| Bad state | Disharmony | Broken 정 | Frozen | Ghost cloth | Silent Country |
| Learning | 悟道 | 정 쌓기 | Sitkeys | Sankofa | Remembering dreaming |
| Randomness | 劫 | Coincidence | Weather | Nyame-ba | Wati Wiru (Wind) |
