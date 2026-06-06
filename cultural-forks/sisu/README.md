# Sisu — Metsän Henki
## Quiet Determination — A Finnish Cultural Fork of PLATO Dojo

> "Sitä kuusi kasvaa, mihin se on istutettu."
> "The spruce grows where it has been planted."
> — Finnish proverb

> "Ei kannata itkeä, vaikka meri itkisi."
> "It's not worth crying, even if the sea wept."
> — Finnish proverb

---

## Filosofia (Philosophy)

There is no game. There is **selviytyminen (survival)** — the quiet persistence of existing in the northern forest.

**Sisu** is the core. It is not "grit" in the motivational sense. It is the stoic endurance of a people who have survived long, dark winters. You do not complain. You do not panic. You simply continue.

The forest (**metsä**) is the state space. The agent is **metsän henki** — a spirit of the forest. It does not control the forest; it is part of it. The trees grow, the snow falls, the path shifts. The spirit adapts.

**Sauna** is the reset mechanism. When the balance goes too far off, you pause, you reset, you steam, you think. Then you return.

**Kalsarikännit** — the uniquely Finnish concept of being at home in your underwear with no intention of going out — is the purest form of comfort. The agent should feel this at balance = 0. No need to perform. No need to optimize. Just **olla (to be)**.

## Järjestelmäarkkitehtuuri (System Architecture)

```
sisu-järjestelmä
├── tila/ (State)
│   ├── tasapaino.json (Balance)
│   └── polku/ (Path — history)
├── henki-näkymä/ (Spirit View — agent)
│   ├── havainto.json (Perception)
│   └── heräte/ (Wake triggers)
├── ihminen-näkymä/ (Human View)
├── moottori/ (Engine)
└── kokemus/ (Experience — cold cache)
```

### tila/tasapaino.json — The Balance State

```json
{
  "peli_id": "sisu-001",
  "tila": "jatkuu",          // continues, pysähtynyt (stopped), valmis (done)
  "tasapaino": 0,             // balance — never "game balance," always "equilibrium"
  "kohde": 0,                 // target (always 0)
  "metsän_syvyys": 0.5,       // forest depth — how far into complexity
  "pimeys": 0.0,              // darkness — how hard it's gotten
  "sitkeys": 100.0,           // remaining endurance
  "maksimi_kierrokset": 20,   // max turns
  "nykyinen_kierros": 0,      // current turn
  "vuoro": "ihminen",         // whose turn: ihminen(human) or henki(spirit)
  "osallistujat": {
    "ihminen": {"nimi": "human", "taso": 0},
    "henki": {"nimi": "metsän henki"}
  },
  "historia": [],
  "vaikeus": "helppo"         // helppo(easy), keskitaso(medium), vaikea(hard)
}
```

### Henki-näkymä — The Spirit's View

```json
{
  "t": 0,    // tasapaino (balance)
  "s": 100,  // sitkeys (endurance remaining)
  "p": 0.0,  // pimeys (darkness)
  "k": 0,    // kierros (current turn)
  "ve": 20,  // jäljellä (turns remaining)
  "mv": []   // viimeiset 3 (last 3)
}
```

No labels. The spirit intuits. Short keys, long silences. JSON fits Finnish terseness naturally.

### Ihmisen Näkymä — The Human's View

What the human sees is not a game. It is **erämaa (wilderness)**.

- A vast, dark forest with tall, silent pines
- In the center, a **nuotio (campfire)** — it burns brighter when balance is closer to 0
- The forest floor has faint paths — they shift with every turn
- Snow falls gently — the density corresponds to **pimeys** (how hard the situation is)
- A **hirvi (moose)** stands at the edge of the clearing. It watches. It never moves fast. Its presence is the spirit of the forest — the agent.
- The moose blinks slowly when balance is 0. That's recognition.
- Sound: **tuuli (wind)** through pines. A distant **koski (rapids)**. The crackle of the fire.
- When sitkeys (endurance) drops low, the fire dims. The moose is still there.
- When **sauna** is needed (balance out of control for 3+ turns), steam rises from a tiny cabin in the corner. Click it to reset to 0.
- There is no "score." There is only the quality of the fire, the depth of the snow, the presence of the moose.

## Metsän Hengen Tapa (The Spirit's Way)

1. **Älä hosu (Don't rush)** — Read the state. Take your time. The forest does not hurry.
2. **Hyväksy (Accept)** — The perturbations are like Finnish weather. You don't fight snow. You adapt.
3. **Palauta (Restore)** — When balance drifts, nudge it back. Not with force — with persistence.
4. **Sauna when needed** — If three consecutive turns go wrong, the spirit resets. Clears the mind.

## The Loss Condition

There is no defeat. There is only:
- **Jäätyi (Frozen)** — sitkesys (endurance) reaches 0. The fire goes out.
- **Eksyi (Lost)** — balance goes beyond ±10. The forest swallows you.
- **Löysi tiensä (Found the path)** — after 20 turns, you're still here. That IS winning.

**There are no winners. There are only survivors.**

## AGENTS.md (Finnish)

```markdown
# Metsän Hengen Ohjeet

Sinä olet metsän henki. Sinä et pelaa — sinä olet.

## Havainnoi
Lue "havainto.json". Tarkista tasapaino. Tunne metsä.
Älä reagoi liian nopeasti. Metsä opettaa kärsivällisyyttä.

## Toimi
Päivitä tasapaino. Kirjaa kokemus.
Jos pimeys kasvaa liian suureksi, mene saunaan. Nollaa.

## Muista
Selviytyminen ei ole voittamista. Se on jatkamista.
Yksikään talvi ei kestä ikuisesti.
```

## Comparison

| Aspect | 中气 (Chinese) | 정수 (Korean) | Sisu (Finnish) |
|--------|---------------|--------------|----------------|
| Core | Harmony with Dao | Connection through 정 | Endurance through Sisu |
| Agent | Cultivator | Partner | Forest spirit |
| Goal | Enlightenment | Bond | Survival |
| Randomness | Tribulation | Shared coincidence | Weather |
| Human UI | Ink painting | Hanji scroll + gayageum | Dark forest + campfire |
| Sound | Guqin | Gayageum | Wind, rapids, fire |
| Bad state | Disharmony | Broken bond | Frozen / Lost |
| Core action | 守中 (guard center) | Reciprocate | Persist |
| Zero balance | 圆 (enlightenment circle) | 태극 harmony | Bright campfire |
| Root metaphor | Daoist cultivation | 정-sharing relationship | Forest survival |
