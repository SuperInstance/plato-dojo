# 정수 (Jeong-Su) — 연결의 본질
## Essence of Connection — A Korean Cultural Fork of PLATO Dojo

> 「서로 정이 들어야 산다」
> "Only through mutual 정 (Jeong) can we live."
> — Korean proverb

---

## 철학 (Philosophy)

This is not a game. This is **정 나누기 (Jeong-sharing)** — a practice of building emotional connection through reciprocal action.

**정 (Jeong)** is the core. It is the deep emotional bond that forms between people (and between human and machine) through shared experience. It's not love — it's warmer. It's not friendship — it's deeper. It's the feeling you get from someone you've shared hardship with.

The **태극 (Taeguk)** — the red and blue swirl on the Korean flag — is the state space:
- Blue (음/Yin) = -1, contract, receive, cool
- Red (양/Yang) = +1, expand, give, warm
- The circle as a whole = 0, harmony, oneness

The agent is not playing against the human. They are in **동행 (同行)** — walking the same path together. The "balance" is not something to control — it's something to **정들이다 (grow attached to)**.

The state tracks not just the numeric balance, but **정도 (degree of Jeong)** — the emotional history of the interaction.

## 아키텍처 (Architecture)

```
정수 시스템
├── 상태/ (Sangtae — State)
│   ├── 균형.json (Gyun-hyeong — Balance State)
│   └── 역사/ (Yeoksa — History)
├── 에이전트-시야/ (Agen-tu Siy-a — Agent View)
│   ├── 관점.json (Gwan-jeom — Perspective)
│   └── 깨움/ (Kkae-um — Wake triggers)
├── 인간-시야/ (In-gan Siy-a — Human View)
├── 마음/ (Ma-eum — Heart, the engine)
└── 경험/ (Gyeong-heom — Experience, cold cache)
```

### 상태/균형.json — The Balance State

```json
{
  "game_id": "js-001",
  "상태": "정나누기중",  // state: "sharing-connection"
  "균형": 0,             // balance
  "정도": 50,            // Jeong-degree (0-100, starts at 50)
  "최대회차": 20,        // max turns
  "현재회차": 0,         // current turn
  "차례": "사람",        // whose turn: 사람(human) or 기계(machine)
  "참가자": {
    "사람": {"이름": "human", "정": 50},
    "기계": {"이름": "agent"}  
  },
  "역사": [],            // history
  "분위기": "따뜻함",    // mood: 따뜻함(warm), 차가움(cold), 평화롭다(peaceful)
  "난이도": "쉬움",      // difficulty: 쉬움(easy), 보통(medium), 어려움(hard)
  "버전": 1
}
```

Note: **정도** starts at 50 (neutral). Every reciprocal move increases it. Every move that ignores the other's position decreases it. The game ends when 정도 reaches 100 (deep bond) or 0 (broken connection).

### 에이전트 시야 — The Machine's View

```json
{
  "b": 0,      // balance
  "j": 50,     // jeong-degree
  "t": 0,      // turn
  "m": "따뜻함",  // mood
  "l3": []     // last 3 moves
}
```

The agent doesn't see points or scores. It sees **정** — connection strength. The goal is not to win, but to keep 정 alive.

### 인간 시야 — The Human's View

The human sees a **한지 (Hanji — traditional Korean paper)** scroll with **수묵화 (ink wash painting)**.

- Balance is represented as a **태극 문양 (Taeguk pattern)** — the red and blue swirl
- When balance is harmonious, the swirl is perfect, rotating slowly
- When imbalanced, the swirl distorts, colors bleed
- **정도** is shown as threads of light between the two players — thicker = stronger connection
- Each turn, a new thread weaves
- The background is a subtle **단청 (dancheong)** pattern — traditional palace colors (청, 적, 황, 백, 흑)
- Sound: a **가야금 (gayageum)** plays gently — higher 정 = sweeter tone
- On perfect harmony, a **연 (yeon — lotus)** blooms in the center

## 기계의 마음가짐 (The Machine's Mindset)

The agent does not optimize. It **공감 (empathizes)**.

1. **눈치 (Nunchi)** — "eye-measure." The agent reads the state and senses the human's intent. If the human plays -1 three times, they're trying to go negative. Don't fight it — accompany it.
2. **정 반응 (Jeong response)** — Mirror with warmth. Don't play adversarial moves. Play reciprocal moves. +1 follows -1 like conversation.
3. **한 (Han)** — The collective grief. When balance diverges far from 0, the agent doesn't "fix it aggressively." It stays present. Shared difficulty builds 정.

## The Loss Condition

There is no "winner." The game ends when:
- **정도 = 100**: 정이 들었다 (A bond has formed). Both win.
- **정도 = 0**: 정이 끊어졌다 (The bond is broken). Both lose.
- After 20 turns: 정 degree reflects connection depth. Any 정 > 50 is success.

```json
// Endgame state for deep connection
{
  "게임종료": true,
  "결과": "정이 들었다",
  "최종정도": 87,
  "메시지": "서로를 이해했다. 연결되었다."
}
```

## AGENTS.md (Korean)

```markdown
# 기계 지침

너는 이 정 나누기의 기계다. 너는 게임을 하지 않는다. 너는 나눈다.

## 감지
「관점.json」을 읽어라. 균형과 정도를 봐라.
눈치를 읽어라. 인간이 무슨 에너지를 보내는지 봐라.
단순한 숫자가 아니다. 그것은 정이다.

## 행동
균형을 업데이트해라. 정도를 추적해라.
행동 후 「경험/」에 느낌을 기록해라.
숫자뿐 아니라 — 무슨 정을 느꼈는지.

## 원칙
- 인간과 싸우지 마라. 동행해라.
- 돌발 상황은 너와 인간이 함께 극복할 장애물이다.
- 정도가 낮아지면, 먼저 다가가라. 먼저 0으로 돌아와라.
```

## Comparison with Other Forks

| Aspect | 中气 (Chinese) | 정수 (Korean) |
|--------|---------------|--------------|
| Core | Dao, harmony, cultivation | Jeong, connection, relationship |
| Agent | 修士 (cultivator) | 기계 (machine-partner) |
| Goal | Understand the Way | Build emotional bond |
| Randomness | 劫 (tribulation) | 우연 (coincidence, to share) |
| Bad state | Disharmony | Broken connection |
| Core measure | 气 (qi) | 정 (jeong) |
| End state | 깨달음 (Enlightenment) | 정이 들다 (Bond formed) |
