vowels = 'aeiou'

def transform_vowels(text, vowel):
    return ''.join([vowel if char in 'aeiouAEIOU' else char for char in text])

result = transform_vowels("I like to eat apples and bananas", 'a')
print(result)

def transform_vowels_v2(text, vowel):
    return ''.join([vowel if char.lower() in 'aeiou' else char for char in text])

result2 = transform_vowels_v2("I like to eat apples and bananas", 'a')
print(result2)
