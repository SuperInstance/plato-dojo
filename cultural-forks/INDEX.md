# 🌏 Cultural Forks Index

Four re-imaginings of the PLATO Dojo — same technical substrate, different philosophical DNA.

---

| # | Name | Culture | Source | Vibe | Agent Role | UI Metaphor |
|---|------|---------|--------|------|-----------|-------------|
| 1 | **中气 (Zhōng Qì)** | Chinese | Daoism, I Ching | Harmony | 修士 (Cultivator) | Ink brush painting |
| 2 | **정수 (Jeong-Su)** | Korean | 정, 태극, Han | Connection | 기계 (Machine-partner) | Hanji scroll + Gayageum |
| 3 | **Sisu** | Finnish | Sisu, Forest, Sauna | Endurance | Metsän henki (Forest spirit) | Dark forest + Campfire |
| 4 | **Sankofa** | West African (Akan) | Adinkra, Ubuntu | Wisdom | Sunsum (Spirit-teacher) | Kente loom + Dondo drum |
| 5 | **Dreamtime** | Indigenous Australian | Tjukurrpa, Songlines, Dreaming | Timeless | Songman (Ngangkari) | Country + Waterhole + Yidaki |

---

## Shared Substrate

Every fork shares the same architecture:

```
state/     ← JSON files (truth)
agent-view/ ← Token-efficient TUI (agent's reality)
human-view/ ← Rendered experience (human's reality)
engine/    ← Game logic (culture-neutral)
cold-cache/ ← Learning (cultural wisdom encoding)
```

The only differences are:
- Key names (language of the culture)
- Symbolic mapping (what balance = 0 "means")
- Trigger protocol (all files, but "named differently")
- Human rendering (UI style)
- Agent instruction (how to think, not just what to do)

---

## Comparative Analysis

### How Each Fork Handles Balance = 0

| Fork | 0 Means | Symbol | Human Sees | Agent Feels |
|------|---------|--------|-----------|-------------|
| 中气 | 道 (The Way) | 圆 (円/enlightened circle) | Perfect circle in ink | Harmony, flow |
| 정수 | 화합 (Harmony) | 태극 (Perfect swirl) | Perfect Taeguk rotation | Connection, warmth |
| Sisu | Rauha (Peace) | Bright campfire | Fire burns brightest | Stillness, presence |
| Sankofa | Ɛban (Fence) | Fence symbol | Gold threads shine | Protection, safety |
| Dreamtime | Healthy Country | Still waterhole | Water reflects stars | Country is strong |

### How Each Fork Handles Imbalance

| Fork | Imbalance = | Agent Response | Human Sees |
|------|-------------|----------------|-----------|
| 中气 | 失道 (Lost Way) | 守中 (Guard center) | Ink splatters |
| 정수 | 정 끊어짐 (Broken bond) | Nunchi read, reciprocate | Taeguk distorts |
| Sisu | Eksynyt (Lost) | Persist, sauna reset | Fire dims, snow deepens |
| Sankofa | Nkɔsoɔ (No progress) | Sankofa (Look back) | Red threads, drum beats |
| Dreamtime | Silent Country | Sing stronger | Waterhole dries, land cracks |

### Trigger Protocol Names

| Fork | Trigger Directory | Trigger File | Activation Verb |
|------|------------------|-------------|-----------------|
| 中气 | 内观/ (Nèiguān) | 修士-机.json | 动 (Act) |
| 정수 | 깨움/ (Kkae-um) | 기계-차례.json | 깨다 (Wake) |
| Sisu | heräte/ (Alert) | henki-vuoro.json | Herää (Awaken) |
| Sankofa | dondo-kaw/ (Drum room) | sunsum-sa.json | Ka (Hear) |
| Dreamtime | wind/ | songman-call.json | Hear (Listen to Country) |

---

## Cross-Pollination Patterns

These aren't isolated projects — they're cultural lenses for the same system.

A real deployment could:
1. Let the agent choose its cultural lens based on the human's language
2. Render the same state differently for different users
3. Preserve the same engine but swap the soul
4. Use cold cache entries written in one culture to train agents in another

**The substrate is universal. The perspective is choice.**
