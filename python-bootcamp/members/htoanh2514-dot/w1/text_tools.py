import re
from collections import Counter


def word_count(text: str) -> dict:
  """Đếm tần suất xuất hiện của từ (bỏ qua dấu câu, không phân biệt hoa thường)."""
  text = text.lower()
  text = re.sub(r"[,.!?;:]", "", text)
  words = text.split()
  return dict(Counter(words))


def top_k(text: str, k: int) -> list:
  """Lấy K từ xuất hiện nhiều nhất.

  Sắp xếp giảm dần theo số lượng, nếu bằng nhau thì sắp xếp theo bảng chữ cái
  (tăng dần).
  """
  counter = word_count(text)
  sorted_words = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
  return [word for word, count in sorted_words[:k]]