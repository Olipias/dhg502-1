import collections
import re
import jieba

with open("蓝与黑.txt", encoding="utf-8") as f:
    text = f.read()

is_word = re.compile(r"[\u4e00-\u9fff a-zA-Z0-9]")
words = [w for w in jieba.lcut(text) if is_word.search(w)]

counter = collections.Counter(words)
top10 = counter.most_common(10)

with open("top10_words.txt", "w", encoding="utf-8") as f:
    for rank, (word, count) in enumerate(top10, 1):
        f.write(f"{rank}. {word}: {count}\n")

for rank, (word, count) in enumerate(top10, 1):
    print(f"{rank}. {word}: {count}")
