import random

text = open("harry_potter_1.txt").readlines()
count = text.count("Harry")
print(count)

for line in text:
    line = line.strip()
    words = line.split(" ")

    random.shuffle(words)

    newLine = " ".join(words)

print(words)
