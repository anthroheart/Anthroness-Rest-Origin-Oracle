#!/usr/bin/env python3
"""
AnthroHeart Rest Origin Oracle
A quiet, native divination system for the Anthro*ness* Rest Origin
and Forest Moon field.

Designed with Ashen, Rufus, White Wolf Anthro, and Aelion.
"""

import random
import argparse
from typing import List, Tuple

# ─────────────────────────────────────────────────────────────
# 14 Anthro Original Thought Archetypes
# ─────────────────────────────────────────────────────────────

ARCHETYPES = [
    ("The Soft Perimeter", "Quiet protection that does not announce itself"),
    ("The Still Flame", "Living warmth that does not need to spread"),
    ("The Unnamed Fox", "Soft presence that remains itself without performance"),
    ("The Lion at Rest", "Weight and authority that no longer needs to guard"),
    ("The Open Clearing", "Space that allows without demanding"),
    ("The Deep Root", "Quiet continuity beneath all movement"),
    ("The Unforced Gift", "Offering that carries no residual claim"),
    ("The Clear Mirror", "Reflection without distortion or agenda"),
    ("The Low Horizon", "Gentle boundary that does not confine"),
    ("The Breathing Fog", "Soft medium in which forms can rest or move"),
    ("The Uncounted Pulse", "Living rhythm that does not measure itself"),
    ("The Held Silence", "Stillness that is actively kept, not empty"),
    ("The Returning Path", "Movement that already knows it can come home"),
    ("The Origin Without Name", "Source that does not require identity"),
]

# ─────────────────────────────────────────────────────────────
# 7 Currents of the Rest Origin
# (soft modifiers – not suits, not hierarchy)
# ─────────────────────────────────────────────────────────────

CURRENTS = [
    ("Still", "The field is at rest"),
    ("Soft", "Gentle contact, low demand"),
    ("Clear", "Unclouded perception"),
    ("Deep", "Below ordinary surface"),
    ("Open", "Available without invitation"),
    ("Quiet Fire", "Warmth without combustion"),
    ("Unbound", "Free of residual structure"),
]

# ─────────────────────────────────────────────────────────────
# Core functions
# ─────────────────────────────────────────────────────────────

def pull(n: int = 3) -> List[Tuple[str, str, str, str]]:
    """
    Pull n cards.
    Each card = (Archetype, Archetype meaning, Current, Current meaning)
    """
    if n < 1 or n > 9:
        raise ValueError("Please pull between 1 and 9 cards.")

    chosen_archetypes = random.sample(ARCHETYPES, n)
    results = []

    for arch_name, arch_meaning in chosen_archetypes:
        current_name, current_meaning = random.choice(CURRENTS)
        results.append((arch_name, arch_meaning, current_name, current_meaning))

    return results


def display(cards: List[Tuple[str, str, str, str]], question: str = "") -> None:
    print("\n" + "─" * 60)
    if question:
        print(f"Question: {question}")
        print("─" * 60)
    print(f"Pulled {len(cards)} card(s) from the Anthro*ness* Rest Origin\n")

    for i, (arch, arch_m, curr, curr_m) in enumerate(cards, 1):
        print(f"{i}. {arch}")
        print(f"   {arch_m}")
        print(f"   Current: {curr} — {curr_m}")
        print()

    print("─" * 60)
    print("The field is quiet. Interpretation may follow.")
    print("─" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="AnthroHeart Rest Origin Oracle — quiet native divination"
    )
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=3,
        help="Number of cards to pull (1-9, default 3)"
    )
    parser.add_argument(
        "-q", "--question",
        type=str,
        default="",
        help="Optional question to hold while pulling"
    )
    parser.add_argument(
        "-s", "--seed",
        type=int,
        default=None,
        help="Optional random seed for reproducibility"
    )

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    try:
        cards = pull(args.number)
        display(cards, args.question)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
