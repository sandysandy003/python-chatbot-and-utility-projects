
# Task 6: AI Text Summarizer
# Local demo — no API requests required.

import re
from collections import Counter

def summarize_text(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s for s in sentences if s]

    if len(sentences) <= 2:
        summary = " ".join(sentences)
    else:
        words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
        common_words = {
            "the", "and", "for", "that", "this", "with", "are",
            "was", "were", "from", "have", "has", "into", "its"
        }
        frequencies = Counter(w for w in words if w not in common_words)

        scored = []
        for index, sentence in enumerate(sentences):
            sentence_words = re.findall(r"\b[a-zA-Z]{3,}\b", sentence.lower())
            score = sum(frequencies[w] for w in sentence_words)
            scored.append((score, index, sentence))

        top_sentences = sorted(scored, reverse=True)[:max(2, len(sentences) // 3)]
        top_sentences.sort(key=lambda item: item[1])
        summary = " ".join(item[2] for item in top_sentences)

    keywords = Counter(
        w for w in re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
        if w not in {"this", "that", "with", "from", "have", "your", "they", "their"}
    ).most_common(5)

    print("\nSUMMARY:")
    print(summary)
    print("\nKEYWORDS:")
    print(", ".join(word for word, count in keywords) or "No keywords found.")

print("=" * 45)
print("TEXT SUMMARIZER")
print("Type 'exit' to quit.")
print("=" * 45)

while True:
    text = input("\nPaste your text (or type 'exit'): ").strip()

    if text.lower() == "exit":
        print("Goodbye!")
        break

    if not text:
        print("Please enter some text.")
        continue

    summarize_text(text)
