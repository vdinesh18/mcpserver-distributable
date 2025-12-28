from typing import Iterable

#!/usr/bin/env python3
# /c:/mcp_tool_calling/test.py
# GitHub Copilot


def sort_alphabets(s: str) -> str:
    """
    Return all alphabetic characters from s, lowercased and arranged in sorted order.
    Uses counting sort over 26 letters for O(n) performance.
    """
    counts = [0] * 26
    base = ord('a')
    for ch in s:
        if ch.isalpha():
            idx = ord(ch.lower()) - base
            if 0 <= idx < 26:
                counts[idx] += 1
    parts = []
    for i, cnt in enumerate(counts):
        if cnt:
            parts.append(chr(base + i) * cnt)
    return ''.join(parts)

def sort_letters_preserve_nonletters(s: str) -> str:
    """
    Sort only the alphabetic characters in s (case-insensitive),
    keep non-letters in their original positions, and preserve
    original case for the letters as they are inserted back
    in sorted order by lowercase.
    """
    letters = [ch for ch in s if ch.isalpha()]
    letters.sort(key=lambda c: c.lower())
    it = iter(letters)
    return ''.join(next(it) if ch.isalpha() else ch for ch in s)

def _run_tests() -> None:
    # Basic tests for sort_alphabets
    assert sort_alphabets("") == ""
    assert sort_alphabets("bca") == "abc"
    assert sort_alphabets("a1c2b") == "abc"
    assert sort_alphabets("Hello, World!") == "dehllloorw"
    # Tests for sort_letters_preserve_nonletters
    assert sort_letters_preserve_nonletters("bca") == "abc"
    assert sort_letters_preserve_nonletters("a1c2b") == "a1b2c"
    assert sort_letters_preserve_nonletters("Hello, World!") == "deHll, loorW!"
    print("All tests passed.")

def main() -> None:
    _run_tests()
    examples = [
        "mcp_tool_calling",
        "bca",
        "a1c2b",
        "Hello, World!"
    ]
    for s in examples:
        print(f"input:    {s}")
        print(f"sorted:   {sort_alphabets(s)}")
        print(f"preserve: {sort_letters_preserve_nonletters(s)}")
        print("-" * 40)

if __name__ == "__main__":
    main()