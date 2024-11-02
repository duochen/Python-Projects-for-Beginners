char_map = {
    'a': 'e', 'b': 'i', 'c': 'o', 'd': 'u', 'e': 'a',
    'f': 'b', 'g': 'c', 'h': 'd', 'i': 'f', 'j': 'g',
    'k': 'h', 'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l',
    'p': 'm', 'q': 'n', 'r': 'o', 's': 'p', 't': 'q',
    'u': 'r', 'v': 's', 'w': 't', 'x': 'u', 'y': 'v', 'z': 'w'
    # Continue for all alphabet letters
}

def telephone_game(text, char_map):
    return ''.join([char_map.get(c, c) for c in text])

result = telephone_game("hello world", char_map)
print(result)

def telephone_game_v2(text, char_map):
    new_text = ''
    for char in text:
        if char.isupper():
            new_text += char_map.get(char.lower(), char).upper()
        else:
            new_text += char_map.get(char, char)
    return new_text

result2 = telephone_game_v2("hello world", char_map)
print(result2)
