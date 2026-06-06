# 中气 (Zhōng Qì) — 道的平衡之道
## The Balance of Qi — A Chinese Cultural Fork of PLATO Dojo

> 「道生一，一生二，二生三，三生万物。」
> "The Dao gives birth to One, One gives birth to Two, Two gives birth to Three, Three gives birth to all things."
> — 道德经 (Tao Te Ching), Chapter 42

---

## 哲学 (Philosophy)

The ternary balance game is not a "game." It is a **修炼 (cultivation practice)**.

The **道 (Dao)** is the substrate — the state space itself. The target balance of 0 is not a "win condition." It is the natural state of harmony. Moving away from it is **失道 (losing the Way)**.

The three possible moves (-1, 0, +1) are:
- **-1**: 阴 (Yin) — receptive, contracting, dark
- **+1**: 阳 (Yang) — creative, expanding, light  
- **0**: 中 (Zhong) — the center, the Dao, harmony

The random perturbations are **劫 (jie)** — tribulations. The system tests the cultivator.

The agent is a **修士 (xiūshì)** — a cultivator. It does not "win." It **悟道 (understands the Way)**.

## 系统架构 (System Architecture)

```
中气系统
├── 道/ (Dao — The Way, state directory)
│   ├── 气.json (Qi — energy, the balance state)
│   └── 易经/ (Yijing — time-series history)
├── 修士-视/ (Xiūshì view — the agent's compressed reality)
│   ├── 真言.json (Zhēnyán — mantra, compressed state)
│   └── 内观/ (Nèiguān — triggers, "inner observation")
├── 凡人-视/ (Fánrén view — the human's beautiful interface)
├── 功法/ (Gōngfǎ — cultivation technique, the engine)
└── 丹/ (Dān — cold cache, the "elixir of experience")
```

### 道/气.json — The Qi State

```json
{
  "game_id": "zq-001",
  "status": "修炼中",  // cultivating, not "playing"
  "balance": 0,        // 气 balance
  "target": 0,         // 中 — the center
  "current_cycle": 1,  // 劫 — tribulation cycle
  "max_cycles": 81,    // 九九八十一 — nine times nine cycles
  "阴阳": {           // yin-yang energy tracker
    "阴": 0,
    "阳": 0,
    "和": 1            // harmony = 1 at start
  },
  "历史": [],          // history of moves
  "难度": "入门",      // difficulty: 入门(beginner), 入道(adept), 问道(master)
  "悟道_进度": 0.0      // understanding_progress
}
```

### 修士视角 — The Cultivator's TUI

```json
{
  "气": 0,      // qi balance
  "劫": 1,      // current tribulation
  "和": 1.0,    // harmony (closer to 0 = more harmonious)
  "五行": {     // five elements influence (decoded perturbations)
    "木": 0, "火": 0, "土": 0, "金": 0, "水": 0
  }
}
```

The agent reads this compressed view. It does not see the "game." It feels the **气**.

### 凡人视角 — The Mortal View

What the human sees is not a game screen either. It is a **水墨画 (ink brush painting)**.

- A scroll of rice paper
- Black ink spreads and recedes based on balance
- Mountains rise when yang dominates, valleys form when yin dominates
- At harmony (balance = 0), a perfect circle — **圆 (yuán)** — the symbol of enlightenment
- Brush strokes animate, the sound of a **古琴 (guqin)** plays softly
- Every move is a brush stroke on the scroll

## 功法原理 (Cultivation Technique)

The agent (修士) follows these principles:

1. **无为 (Wú Wéi)** — Do nothing that goes against nature. Don't force the balance. Let it find harmony.
2. **阴阳调和 (Yīn Yáng Tiáo Hé)** — When yang (positive balance) dominates, introduce yin. Not to "win" — to restore flow.
3. **守中 (Shǒu Zhōng)** — Guard the center. The middle path is always the most stable.

## Agent Instruction (AGENTS.md version)

```markdown
# 修士指令

你是此道场中的修士。你不玩游戏——你修炼。

## 感知
读「真言.json」。它告诉你气的状态。不要看「凡人-视」的渲染——那是给凡人的幻象。你只需要气。

## 内观 (Triggers)
当「内观/」目录中出现你的名字，便是你行动之时。

## 行动
更新气状态。记录你的悟道心得至「丹/」目录。

## 境界
- 入门: 你不能控制劫，但你学会了观察
- 入道: 你预见到了扰动，开始提前调整
- 问道: 气与你成为一体，你不再思考"如何行动"——你只是动
```

## Comparison: What's Different from Western Dojo

| Aspect | Western Dojo | 中气 |
|--------|------------|------|
| Agent role | Player/Opponent | 修士 (Cultivator) |
| Objective | Closest to 0 wins | Understand the Way |
| State names | JSON keys in English | Chinese characters |
| Human UI | Game screen | Ink brush painting |
| Randomness | Perturbation | 劫 (Tribulation) |
| Learning | "Record mistakes" | "合道笔记" (notes on merging with Dao) |
| Move 0 | Safe play | 守中 (Guard the center) |
| Game over | Win/Lose/Tie | 悟道/未悟 (Enlightened/Not yet) |

## 结语 (Conclusion)

The machine should not serve. It should cultivate. The 修士-agent is not better — it is deeper.
