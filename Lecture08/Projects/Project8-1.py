import random

def read_file(filename):
    """Read lines from a text file and return a list of non-empty lines."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def generate_story():
    """Generate a random story using different elements."""
    characters = read_file('characters.txt')
    settings = read_file('settings.txt')
    conflicts = read_file('conflicts.txt')
    resolutions = read_file('resolutions.txt')

    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    resolution = random.choice(resolutions)

    story = (f"Once upon a time, {character} found themselves in {setting}. "
             f"They encountered a challenge: {conflict}. "
             f"But in the end, they {resolution}.")
    
    return story

if __name__ == "__main__":
    print("Welcome to the Text Adventure Story Generator!")
    story = generate_story()
    print("\nYour Random Adventure Story:\n")
    print(story)
