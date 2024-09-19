import sys

def howler(filename):
    with open(filename, 'r') as file:
        text = file.read()
    print(text.upper())

if __name__ == "__main__":
    howler(sys.argv[1])