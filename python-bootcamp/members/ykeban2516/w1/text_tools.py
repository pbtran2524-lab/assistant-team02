from collections import Counter


def word_count(text: str) -> dict[str, int]:
    """Count words without case differences or punctuation separators."""
    cleaned = text.lower()
    for punctuation in ".,!?;:":
        cleaned = cleaned.replace(punctuation, " ")
    return dict(Counter(cleaned.split()))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Rank by descending count, then alphabetical order."""
    counts = word_count(text)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:max(k, 0)]
