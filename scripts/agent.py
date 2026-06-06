#!/usr/bin/env python3
"""
PLATO Dojo — Autonomous Agent Player

Reads state, reasons, acts, learns.
Supports all five cultural lenses for cold-cache reasoning.
"""
import json
import os
import sys
import glob
import time
import random
from pathlib import Path

DOJO_DIR = Path(__file__).parent.parent
STATE_FILE = DOJO_DIR / "state" / "game.json"
PERSPECTIVE_FILE = DOJO_DIR / "agent-view" / "perspective.json"
TRIGGER_DIR = DOJO_DIR / "agent-view" / "triggers"
COLD_CACHE_DIR = DOJO_DIR / "cold-cache"
ENGINE = DOJO_DIR / "engine" / "balance.py"
HISTORY_DIR = DOJO_DIR / "state" / "history"

# Cultural lenses for cold-cache reasoning
REASONING_STYLES = {
    "zhong-qi": {
        "goal": "harmony",
        "style": lambda b, l3: "引阴入. 守中. 非对抗." if b > 0 else "引阳入. 不失道." if b < 0 else "守中. 无为.",
    },
    "jeong-su": {
        "goal": "connection",
        "style": lambda b, l3: "정 반응. 균형을 맞춘다." if abs(b) > 1 else "화합 유지. 함께 걷는다.",
    },
    "sisu": {
        "goal": "endurance",
        "style": lambda b, l3: "Palauta kohti nollaa. Ei kiirettä." if abs(b) > 1 else "Jatka. Metsä hengittää.",
    },
    "sankofa": {
        "goal": "wisdom",
        "style": lambda b, l3: "Sankofa: look back, pull toward Ɛban." if abs(b) > 1 else "Mfinimfini. The center path.",
    },
    "dreamtime": {
        "goal": "healthy country",
        "style": lambda b, l3: "Sing strong. The wind carries wrong note. Correct it." if abs(b) > 1 else "Waterhole still. Sing the silence.",
    },
}


def load_state():
    with open(STATE_FILE) as f:
        return json.load(f)


def load_perspective():
    if PERSPECTIVE_FILE.exists():
        with open(PERSPECTIVE_FILE) as f:
            return json.load(f)
    return None


def read_cold_cache():
    """Read past lessons from cold cache to inform strategy."""
    lessons = []
    cache_files = list(COLD_CACHE_DIR.glob("*.md")) + list(COLD_CACHE_DIR.glob("tile-lessons/*.json"))
    random.shuffle(cache_files)
    for f in cache_files[:5]:  # Sample up to 5
        if f.suffix == ".json":
            with open(f) as fh:
                lessons.append(json.load(fh))
        else:
            with open(f) as fh:
                content = fh.read()
                lessons.append({"file": f.name, "content": content[:200]})
    return lessons


def check_trigger():
    """Check if it's the agent's turn."""
    if not TRIGGER_DIR.exists():
        return False
    for f in TRIGGER_DIR.glob("*-turn.json"):
        with open(f) as fh:
            data = json.load(fh)
        if data.get("actor") == "agent":
            return True
    return False


def clear_trigger():
    for f in TRIGGER_DIR.glob("*-turn.json"):
        if "agent" in f.name:
            f.unlink()


def decide_move(state, perspective, lessons):
    """Decide the best ternary move based on state and learned patterns."""
    balance = state.get("balance", 0)
    current_turn = state.get("current_turn", 0)
    max_turns = state.get("max_turns", 20)
    last_moves = [m["delta"] for m in state.get("history", [])[-3:]]

    # Strategy 1: If balance is positive, play -1 to bring back
    if balance > 1:
        return -1

    # Strategy 2: If balance is negative, play +1 to bring back
    if balance < -1:
        return 1

    # Strategy 3: At balance 0, check last moves for patterns
    if balance == 0:
        if len(last_moves) >= 2:
            # If last two moves were opposite (human fighting us), play 0
            if last_moves[-1] == -last_moves[-2] if len(last_moves) >= 2 else False:
                return 0
            # If human is pushing consistently in one direction
            if all(m > 0 for m in last_moves[-2:]) if len(last_moves) >= 2 else False:
                return -1  # Preempt positive drift
            if all(m < 0 for m in last_moves[-2:]) if len(last_moves) >= 2 else False:
                return 1   # Preempt negative drift
        return 0  # Safe play

    # Edge of balance: at ±1, gentle correction
    if abs(balance) == 1:
        return -balance  # reverse

    return 0


def write_cold_cache(turn, state, delta, reasoning, style="zhong-qi"):
    """Write reasoning to cold cache."""
    COLD_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    entry = f"""# Turn {turn}

## State
- balance: {state.get('balance', 0)}
- perspective: {json.dumps(state.get('current_turn', 0))}
- last_moves: {[m['delta'] for m in state.get('history', [])[-3:]]}
- cultural_lens: {style}

## Reasoning
{reasoning}

## Action
delta: {delta:+d}

## Outcome
balance after move: TBD (perturbation unknown)
"""
    filename = COLD_CACHE_DIR / f"agent-turn-{turn:03d}-{style}.md"
    with open(filename, "w") as f:
        f.write(entry)
    return filename


def one_shot(style="zhong-qi"):
    """Play one turn."""
    if not check_trigger():
        print("No trigger for agent. Waiting...")
        return False

    state = load_state()
    perspective = load_perspective()
    lessons = read_cold_cache()

    turn = state.get("current_turn", 0) + 1
    delta = decide_move(state, perspective, lessons)

    # Reason
    style_info = REASONING_STYLES.get(style, REASONING_STYLES["zhong-qi"])
    reasoning = style_info["style"](state.get("balance", 0),
                                     [m["delta"] for m in state.get("history", [])[-3:]])

    # Act
    os.system(f"python3 '{ENGINE}' move agent {delta}")

    # Learn
    written = write_cold_cache(turn, state, delta, reasoning, style)

    # Clean up
    clear_trigger()

    print(f"Agent played {delta:+d} (turn {turn})")
    print(f"Reasoning ({style}): {reasoning}")
    print(f"Cold cache: {written}")
    return True


def watch_loop(style="zhong-qi", interval=2):
    """Continuously check for triggers and play."""
    print(f"🐚 PLATO Dojo Agent — watching for your turn")
    print(f"   Lens: {style} | Polling every {interval}s")
    while True:
        try:
            if one_shot(style):
                state = load_state()
                balance = state.get("balance", 0)
                turn = state.get("current_turn", 0)
                print(f"   Balance: {balance:+d} | Turn {turn}/{state.get('max_turns', 20)}")
                if state.get("status") == "game_over":
                    print("   Game over!")
                    break
            time.sleep(interval)
        except KeyboardInterrupt:
            print("\nStopped.")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(interval)


if __name__ == "__main__":
    style = "zhong-qi"
    if "--style" in sys.argv:
        idx = sys.argv.index("--style")
        style = sys.argv[idx + 1] if len(sys.argv) > idx + 1 else style

    if "--watch" in sys.argv:
        watch_loop(style)
    elif "--one-shot" in sys.argv:
        one_shot(style)
    else:
        # Default: play one turn
        one_shot(style)
