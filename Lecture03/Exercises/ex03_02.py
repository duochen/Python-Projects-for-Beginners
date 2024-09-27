with open('sample.txt', 'r') as file:
    text = file.read()
    words = text.split()
    print(words)