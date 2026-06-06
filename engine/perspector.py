#!/usr/bin/env python3
"""Perspector — render game state through any cultural lens.

Usage:
  python3 engine/perspector.py                    # Show all perspectives
  python3 engine/perspector.py zhong-qi           # Show one lens
  python3 engine/perspector.py --watch            # Auto-refresh
"""

import json
import sys
import time
from pathlib import Path

STATE_FILE = Path(__file__).parent.parent / "state" / "game.json"
FORK_DIR = Path(__file__).parent.parent / "cultural-forks"
HISTORY_DIR = Path(__file__).parent.parent / "state" / "history"

LENSES = {
    "zhong-qi": {
        "name": "中气 (Zhōng Qì) — Chinese",
        "keys": {"balance": "气", "target": "道", "current_turn": "劫数", "difficulty": "难度"},
        "symbol": lambda b: "圆" if b == 0 else ("阳" if b > 3 else ("阴" if b < -3 else "中")),
        "action_map": {-1: "阴", 0: "中", 1: "阳"},
        "summary": lambda s: f"气={s['balance']:+d}  和={'✓' if abs(s['balance']) < 2 else '✗'}  {LENSES['zhong-qi']['symbol'](s['balance'])}"
    },
    "jeong-su": {
        "name": "정수 (Jeong-Su) — Korean",
        "keys": {"balance": "균형", "target": "목표", "current_turn": "회차", "difficulty": "난이도"},
        "symbol": lambda b: "태극" if b == 0 else ("양(🔥)" if b > 2 else "음(💧)"),
        "action_map": {-1: "음-정", 0: "화합", 1: "양-정"},
        "summary": lambda s: f"균형={s['balance']:+d}  정도=—  {LENSES['jeong-su']['symbol'](s['balance'])}"
    },
    "sisu": {
        "name": "Sisu — Finnish",
        "keys": {"balance": "tasapaino", "target": "kohde", "current_turn": "kierros", "difficulty": "vaikeus"},
        "symbol": lambda b: "nuotio🔥" if abs(b) < 2 else ("lumi❄️" if b > 0 else "suo🫧"),
        "action_map": {-1: "miinus-yksi", 0: "nolla", 1: "plus-yksi"},
        "summary": lambda s: f"tasapaino={s['balance']:+d}  {LENSES['sisu']['symbol'](s['balance'])}"
    },
    "sankofa": {
        "name": "Sankofa — Akan/West African",
        "keys": {"balance": "twea", "target": "nsusui", "current_turn": "nantew", "difficulty": "mmɔden"},
        "symbol": lambda b: "Ɛban🛡️" if b == 0 else ("Nsoroma⭐" if abs(b) < 3 else "Nkonsonkonson⛓️"),
        "action_map": {-1: "ɛna", 0: "mfinimfini", 1: "agya"},
        "summary": lambda s: f"twea={s['balance']:+d}  {LENSES['sankofa']['symbol'](s['balance'])}"
    },
    "dreamtime": {
        "name": "Dreamtime — Indigenous Australian",
        "keys": {"balance": "song", "target": "songline", "current_turn": "walk", "difficulty": "walkabout"},
        "symbol": lambda b: "💧" if b == 0 else ("🌏" if abs(b) < 3 else "🏜️"),
        "action_map": {-1: "low-didge", 0: "silence", 1: "high-beat"},
        "summary": lambda s: f"song={s['balance']:+d}  Country={'strong 💧' if abs(s['balance']) < 2 else 'fair 🌏' if abs(s['balance']) < 5 else 'weak 🏜️'}  {LENSES['dreamtime']['symbol'](s['balance'])}"
    }
}


def load_state():
    with open(STATE_FILE) as f:
        return json.load(f)


def render_lens(state, lens_name):
    lens = LENSES[lens_name]
    history = state.get("history", [])
    last_moves = [m["delta"] for m in history[-3:]]

    print(f"\n{'='*50}")
    print(f"  {lens['name']}")
    print(f"{'='*50}")

    # Core state
    for eng_key, local_key in lens["keys"].items():
        val = state.get(eng_key, "?")
        print(f"  {local_key}: {val}")

    # Symbol
    print(f"  Symbol: {lens['symbol'](state.get('balance', 0))}")

    # Last moves
    if last_moves:
        mapped = [lens["action_map"].get(m, f"{m:+d}") for m in last_moves]
        print(f"  Last moves: {' → '.join(mapped)}")

    # Summary line
    print(f"  ▸ {lens['summary'](state)}")


def render_all():
    try:
        state = load_state()
    except FileNotFoundError:
        print("No game state found. Start a game first:")
        print("  python3 engine/balance.py new easy")
        return

    print(f"\n  Game: {state.get('game_id', '?')}  |  Turn: {state['current_turn']}/{state['max_turns']}")
    print(f"  Raw balance: {state['balance']:+d}")

    for lens_name in LENSES:
        render_lens(state, lens_name)

    print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        lens = sys.argv[1]
        if lens == "--watch":
            try:
                while True:
                    render_all()
                    print("--- Watching (Ctrl+C to stop) ---")
                    time.sleep(2)
            except KeyboardInterrupt:
                print("\nStopped.")
        elif lens in LENSES:
            state = load_state()
            render_lens(state, lens)
        else:
            print(f"Unknown lens: {lens}")
            print(f"Available: {', '.join(LENSES.keys())}")
    else:
        render_all()
