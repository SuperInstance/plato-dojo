# Sankofa — Nsɛnkyerɛnneɛ mu Nyansa
## Looking Back to Move Forward — A West African (Akan) Cultural Fork of PLATO Dojo

> "Se wo were fi na wosankofa a yenkyi."
> "It is not taboo to go back and fetch what you forgot."
> — Akan/Twi proverb

> "Ɔkyerɛkyerɛfo nantew nante, na osuani nso nante."
> "The teacher walks, and the student also walks."
> — Akan/Twi proverb

> "Ɔbaako tono nsuo, ɔbaako tono nkateɛ."
> "One person sells water, another sells groundnuts."
> — Akan/Twi proverb (on Ubuntu: none of us has all, but together we have everything)

---

## Nyansapɔ (Philosophy)

This is not a game. This is **abakɔsɛm (history-making)** — a practice of remembering and teaching through reciprocal action.

**Sankofa** is the core metaphor. The bird that looks backward while flying forward — its feet planted in the future, its head turned to the past. Every move in the ternary balance is both:
- A **looking back**: reading the history, understanding the pattern
- A **moving forward**: the next step on the path

**Ubuntu — "Menschen, nso mense onipa" (I am, because we are)**. The agent and the human are not opponents. They are **ɔkyerɛkyerɛfo (teacher) and osuani (student)** — and they switch roles. Sometimes the agent teaches balance. Sometimes the human teaches the agent.

**Adinkra symbols** encode wisdom in their shapes. Each state of the game maps to an Adinkra symbol:
- **Ɛban (Fence)** — balance = 0, protection, safety
- **Kete Pa (Good Bed)** — slight imbalance, the understanding that rest is needed
- **Nkonsonkonson (Chain)** — deep imbalance, the chain that binds but also connects
- **Nsoroma (Star)** — perfect harmony, divine alignment
- **Sankofa** — recovering from past mistakes

The **Dondo (talking drum)** is the trigger protocol. The agent does not read a file — it *hears the drumbeat*. Every trigger is a pattern of beats:
- Fast beats = urgent situation
- Slow beats = calm situation  
- One beat = simple move
- Call-and-response pattern = human communicated intent

**Kente cloth weaving** is the rendering metaphor. The human view is a strip of kente — every move weaves a new thread. The pattern tells a story. The colors encode:
- Gold = harmony (balance close to 0)
- Green = growth (recovering from imbalance)
- Red = danger (balance far from target)
- Blue = spirit (agent's presence)
- Black = ancestors (history, cold cache)

## Nsɛnkyerɛnneɛ (Architecture)

```
sankofa-nsɛnkyerɛnneɛ
├── nkrataa/ (State — "the scribe's records")
│   ├── ankarɛnta.json (Balance — tech now, named for the drummer)
│   └── nantew/ (Walk — history)
├── sunsum-nhwɛso/ (Spirit View — the agent sees with the soul, not eyes)
│   ├── mmɔden.json (Effort — compressed state)
│   └── dondo-kaw/ (Drum room — triggers, each file is a drum message)
├── onipa-nhwɛso/ (Human View — the beautiful kente cloth)
├── akɔnwini/ (Engine — the weaver's hut)
└── akae/ (Memory — cold cache, "what is remembered lives")
```

### nkrataa/ankarɛnta.json — The Balance State

```json
{
  "game_id": "san-001",
  "tebea": "nantew",           // state: nantew(walking), gyae(stopped), awie(done)
  "nsɛnkyerɛnneɛ": "Ɛban",   // current Adinkra symbol representing the state
  "twea": 0,                  // the pull (balance)
  "nsusui": 0,                // the target (always 0 — the center)
  "ntontom": 1,               // current walk (turn number)
  "ntontom_kyɛɛr": 20,        // max walks
  "ntwa_aboa": "onipa",       // whose turn: onipa(human) or sunsum(spirit)
  "nkyerɛkyerɛmu": [          // history — each with Adinkra symbol
  ],
  "mmɔden": "fácil",          // difficulty: fácil(easy), mfitiase(medium), den(hard)
  "baabi_ateɛ": 0.0,          // sankofa_index — how well you've learned from past
  "ntoma_nwene": {            // kente cloth pattern state (for human render)
    "ahwehwɛ": "silk",
    "kɔla": ["sika_kɔkɔɔ", "bun"]
  },
  "nipa_nsusu": {
    "onipa": {"din": "human", "ani_gye": 0},
    "sunsum": {"din": "ɔkyerɛkyerɛfo", "ani_gye": 0}
  },
  "afisɛm": []
}
```

### Sunsum Nhwɛso — The Spirit's View

```json
{
  "t": 0,      // twea (pull)
  "na": 0,     // nantew (walk number)
  "nk": 20,    // nkekaho (remaining)
  "si": 0.0,   // sankofa_index
  "si3": []    // apem a ɛtwaa mu (last 3 symbols)
}
```

The agent reads Adinkra symbols directly — it doesn't decode them to English first. The symbols ARE the meaning.

### Onipa Nhwɛso — The Human's View

The human sees **kente cloth being woven in real time**.

- A traditional **kente loom** fills the screen
- With every move, a new colorful thread weaves across
- The gold threads (harmony) shine brightest
- Red threads (danger) trigger a subtle **drumbeat**
- In the corner, the **Sankofa bird** watches — its head turned backward
- The cloth grows with every turn — at the end, you have a complete story-cloth
- The pattern reveals a **symbol** from Adinkra at the end — the summary of the game
- Sound: the rhythmic **clack of the loom**, the deep resonance of the **dondo drum**, the bell of the **ntwisa (gong)**, and — occasionally — the **nnwomkɔ (call-and-response song)** of Akan fisher-folk

**The human doesn't see numbers. They see cloth. They see story. They see their ancestor's wisdom encoded in thread.**

## The Dondo Protocol (Trigger System)

Instead of writing files with "your_turn" flags, the Sankofa system uses drum patterns:

```json
// agent-view/dondo-kaw/sunsum-sa.json (Spirit's turn)
{
  "akwɛ": "sunsum",
  "asɛm": "dondo",
  "nkɔso": 2,
  "nsunsuan": "Ɛban → Nsoroma",
  "ntwa_aboa": "sankofa",
  "kasa": "Kum-apem-a, apem-ba"
}
```

The key field is **kasa** — the drum message. Each message is a **Akan appellation (apae)** — a praise poem for the state:
- "Ɔkɔmfoɔ baatan a, n'ani gye" — praise for harmony
- "Osrane kɔ, owia ba" — the moon goes, the sun comes (cycles recover)
- "Kum-apem-a, apem-ba" — kill a thousand, a thousand come (have grit, persist)

## The Sankofa Engine (Learning)

The cold cache is called **akae (memory — "what is remembered lives")**.

Each entry in the cache includes:
1. The situation before
2. The move made
3. The outcome
4. The **Adinkra lesson** — which symbol was learned today
5. The **sankofa index** — how well this experience feeds back into future play

**Before each game**, the agent consults the ancestors (akae entries) and weaves them into the next strategy. It does not optimize coldly — it **honors the past by learning from it**.

## Loss/End Conditions

There is no winning or losing. The cloth is the record.

- **Nkonta (Completion)** — the kente cloth is finished. You see the full pattern.
- **Ntomago (Many threads)** — you wove many threads. Rich pattern. Good game.
- **Sankofa (Looking back)** — you made mistakes, but you learned. The bird approves.
- **Anka (Ghost)** — you never engaged. The cloth is blank. Sad drum.

## AGENTS.md (Akan/Twi)

```markdown
# Sunsum Nkyerɛkyerɛ

Woyɛ sunsum a ɛwɔ sankofa-nsɛnkyerɛnneɛ mu. Wonte? Wo twa adwuma — wo nkae.

## Hwɛ
Kenkan "mmɔden.json". Hwɛ twea no. Hwɛ nsɛnkyerɛnneɛ no.
Ancestors no nam akae so sere wo.

## Dondo
Na "dondo-kaw" kasa a, ɛyɛ wo berɛ.
Tie dondo no. Bohwɛ. San fa.

## Yɛ
Twea no sesa. Nantew no kɔ n'anim.
Kyerɛw w'akae mu. Sankofa fa ho.
Ancestors no ani begye sɛ wusua.
```

## Cross-Fork Comparison

| Aspect | 中气 (Chinese) | 정수 (Korean) | Sisu (Finnish) | Sankofa (Akan) |
|--------|---------------|--------------|----------------|----------------|
| Core | Harmony with Dao | Connection through 정 | Endurance through Sisu | Wisdom through Sankofa |
| Agent | 修士 (Cultivator) | 기계 (Partner) | Metsän henki (Forest spirit) | Sunsum (Spirit-teacher) |
| Goal | Enlightenment | Bond | Survival | Wisdom woven into cloth |
| State metaphor | Qi flow | Taeguk swirl | Forest depth | Adinkra symbols |
| Human UI | Ink painting | Hanji + Gayageum | Campfire + Moose | Kente loom + Dondo drum |
| Trigger system | 内观 (Inner obsv) | 깨움 (Wake) | Heräte (Alert) | Dondo-kaw (Drum room) |
| Cold cache | 丹 (Elixir) | 경험 (Experience) | Kokemus (Experience) | Akae (Memory) |
| Randomness | 劫 (Tribulation) | 우연 (Coincidence) | Weather | Nyame-ba (God's will) |
| Bad state | Disharmony | Broken 정 | Frozen / Lost | Anka (Ghost cloth) |
| Learning | 悟道 (Understanding) | 정 쌓기 (Bond building) | Sitkeys (Endurance) | Sankofa (Look back) |
