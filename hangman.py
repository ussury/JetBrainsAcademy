import random

print('H A N G M A N')


def start_game():
    invite = input('Type "play" to play the game, "exit" to quit: ')
    if invite == 'exit':
        return None
    else:
        return game()


def game():
    word_list = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
    symbols_list = list('-' * len(word_list))
    symbols_set = set()
    count = 8

    def end_game(coll):
        if '-' in coll:
            print('You are hanged!\n')
        else:
            print('You guessed the word!\nYou survived!\n')

    while count > 0:
        if '-' not in symbols_list:
            break
        print('\n', ''.join(symbols_list))
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should input a single letter')
        elif letter in symbols_set:
            print('You already typed this letter')
        elif not letter.isalpha() or letter == letter.upper():
            print('It is not an ASCII lowercase letter')
        elif letter not in word_list:
            print('No such letter in the word')
            count -= 1
        else:
            for (index, el) in enumerate(word_list):
                if el == letter:
                    symbols_list.pop(index)
                    symbols_list.insert(index, letter)
        symbols_set.add(letter)

    end_game(symbols_list)
    start_game()


start_game()
