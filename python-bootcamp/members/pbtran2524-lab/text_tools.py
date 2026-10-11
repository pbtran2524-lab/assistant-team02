from collections import Counter
import re
from typing import Dict, List, Tuple


def word_count(text: str) -> Dict[str, int]:
    
    text_lower = text.lower()
    cleaned_text = re.sub(r"[,.!?/;:\"'()\[\]{}]", "", text_lower)
    words = cleaned_text.split()
    return dict(Counter(words))


def top_k(text: str, k: int) -> List[Tuple[str, int]]:
   
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]


if __name__ == "__main__":
    user_text = input("Enter the text: ").strip()

    try:
        k = int(input("Enter the number of top words to retrieve (e.g., 3): ").strip())
    except ValueError:
        print("Invalid K, defaulting to K = 3.")
        k = 3

    print("\n--- RESULT ---")
    print("Word count:", word_count(user_text))
    print(f"Top {k}:", top_k(user_text, k))