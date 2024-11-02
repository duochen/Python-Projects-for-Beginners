from collections import Counter
import matplotlib.pyplot as plt

def count_characters(text):
    return Counter(text)

counts = count_characters("I like to eat apples and bananas")
plt.bar(counts.keys(), counts.values())
plt.show()
