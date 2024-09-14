word = input("Enter a word: ")
article = "an" if word[0].lower() in 'aeiou' else "a"
print(f"Ahoy! {article} {word} off the larboard bow!")
