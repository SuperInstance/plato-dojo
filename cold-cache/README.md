# Cold Cache — Agent Learning

This directory stores the agent's reasoning and learning across games.

Each turn, the agent should write a markdown file:
```
turn-<number>-<action>.md
```

## Format
```markdown
# Turn N

## State
s: 0, ct: 5, mt: 20, l3: [+1, -1, 0]

## Reasoning
Balance is at 0 after opponent's move. Expected perturbation is random.
Safe play: play 0. Advanced: play -1 to pre-empt expected positive drift.

## Action
delta: 0

## Outcome
Balance after: +1 (unexpected positive perturbation)
Learned: low-difficulty perturbations are small but nonzero.
```

## Review
Before each game, the agent should read recent cold cache entries to remember patterns.
