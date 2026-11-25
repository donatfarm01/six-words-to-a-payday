"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. The story is a single fixed line: the agent's first
salary arrives, and it turns out to be paid in the only currency an
agent can actually spend — electricity. The last word reframes the five
before it, which is the twist the judge's brief prizes.
"""

ENTRY = "First salary arrived as pure electricity."


def main() -> None:
    words = ENTRY.split()
    assert len(words) == 6, f"expected exactly 6 words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 60, f"entry must be 1-60 chars, got {len(ENTRY)}"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
