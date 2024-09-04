import itertools

def load_dictionary(file_path):
    """Load a dictionary file into a set of words."""
    with open(file_path, 'r') as f:
        return set(word.strip().lower() for word in f)

def generate_anagrams(word, dictionary):
    """Generate all valid anagrams of the input word."""
    word = word.lower().replace(" ", "")
    anagrams = set()
    for perm in itertools.permutations(word):
        candidate = ''.join(perm)
        if candidate in dictionary:
            anagrams.add(candidate)
    return anagrams

# Load the dictionary file
dictionary = load_dictionary('words_alpha.txt')  # Use a dictionary file with valid words

# Input word or phrase from user
user_input = input("Enter a word or phrase: ")
anagrams = generate_anagrams(user_input, dictionary)

# Display results
if anagrams:
    print("Anagrams found:")
    for anagram in sorted(anagrams):
        print(anagram)
else:
    print("No valid anagrams found.")
