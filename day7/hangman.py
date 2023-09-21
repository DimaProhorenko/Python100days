import random


words = ["python", "ruby", "flutter", "supernatural", "luke", "coding", "fuck"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lifes = len(stages)


def get_random_word(words_list):
    return random.choice(words_list)


def get_user_input():
    return input("Enter a letter you think is in the word: ").lower()


def print_blanks(word_list):
    print("".join(word_list))


def update_blanks(word, word_guessed, letter):
    is_correct = False
    for position in range(len(word)):
        if letter == word[position]:
            word_guessed[position] = letter
            is_correct = True

    if not is_correct:
        global lifes
        lifes -= 1


# def reduce_life():
#     lifes -= 1


def check_win(word):
    return not "_" in word


def check_loose():
    global lifes
    if lifes == 0:
        return True

    return False


def play():
    word = get_random_word(words)
    guessed_word = ["_"] * len(word)
    print(stages[lifes - 1])
    print_blanks(guessed_word)

    while True:
        guess = get_user_input()
        update_blanks(word, guessed_word, guess)
        print(stages[lifes - 1])
        print_blanks(guessed_word)

        if check_win(guessed_word):
            print("You won")
            break

        if check_loose():
            print("You lost")
            break


# print(word)
play()


# print(check_letter(guess, word))
