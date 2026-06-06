#!/usr/bin/env python3
"""Ternary Balance Engine — the game logic for PLATO Dojo.

Rules:
- A balance value starts at 0
- Each turn, player picks -1, 0, or +1 (a trit)
- The balance is adjusted by that trit
- Random perturbations are added each turn (±1)
- Goal: keep balance as close to 0 as possible
- After max_turns, closest to 0 wins
"""

import json
import random
import sys
import os
from pathlib import Path

STATE_FILE = Path(__file__).parent.parent / "state" / "game.json"
PERSPECTIVE_FILE = Path(__file__).parent.parent / "agent-view" / "perspective.json"
TRIGGER_DIR = Path(__file__).parent.parent / "agent-view" / "triggers"
HISTORY_DIR = Path(__file__).parent.parent / "state" / "history"


def load_state():
    with open(STATE_FILE) as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def update_perspective(state):
    """Compress state to minimal token form for the agent."""
    perspective = {
        "s": state["balance"],       # current balance
        "t": state["target"],        # target (always 0)
        "ct": state["current_turn"], # current turn number
        "mt": state["max_turns"],    # max turns
        "l3": [m["delta"] for m in state["history"][-3:]],  # last 3 moves
        "d": state["difficulty"],
        "a": [-1, 0, 1],  # available moves
    }
    with open(PERSPECTIVE_FILE, "w") as f:
        json.dump(perspective, f, indent=2)


def create_trigger(whom):
    """Create a trigger file to wake the agent."""
    TRIGGER_DIR.mkdir(parents=True, exist_ok=True)
    trigger = {
        "type": "your_turn",
        "actor": whom,
        "timestamp": __import__("time").time(),
    }
    with open(TRIGGER_DIR / f"{whom}-turn.json", "w") as f:
        json.dump(trigger, f, indent=2)


def apply_move(state, actor, delta):
    """Apply a ternary move and random perturbation."""
    delta = max(-1, min(1, delta))  # clamp to valid trit

    # Random perturbation based on difficulty
    if state["difficulty"] == "easy":
        perturbation = random.choice([-1, 0, 0, 0, 1])
    elif state["difficulty"] == "medium":
        perturbation = random.choice([-1, -1, 0, 1, 1])
    else:
        perturbation = random.choice([-1, 1])

    old_balance = state["balance"]
    new_balance = old_balance + delta + perturbation

    move = {
        "turn": state["current_turn"] + 1,
        "actor": actor,
        "delta": delta,
        "perturbation": perturbation,
        "balance_after": new_balance,
        "game_id": state["game_id"],
    }

    # Save to history
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    turn_file = HISTORY_DIR / f"turn-{state['current_turn'] + 1:03d}.json"
    with open(turn_file, "w") as f:
        json.dump(move, f, indent=2)

    state["balance"] = new_balance
    state["current_turn"] += 1
    state["history"].append(move)

    # Calculate score (closer to 0 = better)
    if actor in state.get("players", {}):
        state["players"][actor]["score"] = abs(state["balance"]) * -1
    elif actor in state.get("agents", {}):
        state["agents"][actor]["score"] = abs(state["balance"]) * -1

    return state


def check_game_over(state):
    """Check if the game is over."""
    if state["current_turn"] >= state["max_turns"]:
        state["status"] = "game_over"
        # Determine winner
        p_score = state["players"]["player"]["score"]
        a_score = state["agents"].get("agent", {}).get("score", 0)
        if p_score > a_score:
            state["winner"] = "player"
        elif a_score > p_score:
            state["winner"] = "agent"
        else:
            state["winner"] = "tie"
        return True
    return False


def start_new_game(difficulty="easy", max_turns=20):
    """Initialize a new game."""
    state = {
        "game_id": f"ternary-balance-{random.randint(100, 999)}",
        "status": "playing",
        "balance": 0,
        "target": 0,
        "max_turns": max_turns,
        "current_turn": 0,
        "turn": "player",
        "players": {
            "player": {"name": "human", "score": 0},
        },
        "agents": {
            "agent": {"name": "plato-agent", "score": 0}
        },
        "history": [],
        "win_condition": "closest_to_zero_after_max_turns",
        "difficulty": difficulty,
        "modifiers": [],
        "version": 1,
    }
    save_state(state)
    update_perspective(state)
    create_trigger("player")
    return state


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: balance.py [new|move <agent> <delta>]")
        sys.exit(1)

    if sys.argv[1] == "new":
        diff = sys.argv[2] if len(sys.argv) > 2 else "easy"
        state = start_new_game(diff)
        print(f"Game started: {state['game_id']}")
        print(f"Difficulty: {diff}")

    elif sys.argv[1] == "move":
        state = load_state()
        actor = sys.argv[2]
        delta = int(sys.argv[3])
        state = apply_move(state, actor, delta)
        update_perspective(state)

        if actor == "player":
            state["turn"] = "agent"
            create_trigger("agent")
        else:
            state["turn"] = "player"
            create_trigger("player")

        save_state(state)
        print(f"Turn {state['current_turn']}: {actor} moved {delta:+d}, balance={state['balance']}")

        if check_game_over(state):
            save_state(state)
            print(f"Game over! Winner: {state.get('winner', 'unknown')}")
