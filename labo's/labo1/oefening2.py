from collections import Counter
file = open("namen.txt", "r")
data = file.read()
words = data.split()
counts = Counter(words)
print(counts)