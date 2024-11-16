def main():
    with open('gashlycrumb.txt') as f:
        lines = f.readlines()

        gashlycrumb_dict = {}
        for line in lines:
            letter, phrase = line.split(': ')
            gashlycrumb_dict[letter] = phrase.strip()

        letter = input('Enter a letter: ').upper()
        print(gashlycrumb_dict.get(letter, 'No such letter found.'))

if __name__ == '__main__':
    main()