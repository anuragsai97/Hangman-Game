import random

pics = ['''

  +---+
      |
      |
      |
      |
      |
=========''','''  

  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

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
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = {'Countries':'afghanisthan austria argentina bangladesh belgium cuba canada egypt france germany greece india iran iraq italy ireland iceland japan spain switzerland sweden zimbabwe'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid pentagon hexagon septagon octagon'.split(),
'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Sports':'Archery Basketball Football Swimming Cycling Golf Tennis Badminton Hockey Cricket Polo Wrestling Shooting Volleyball'.split(),
'Fruits':'apple orange lemon pear watermelon grape pineapple banana cantaloupe mango strawberry tomato guava'.split(),
'Animals':'monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard turkey turtle weasel whale wolf wombat zebra'.split()}

def get_word(word):
	word_key = random.choice(list(word.keys()))
	word_index = random.randint(0, len(word[word_key]) - 1)
	return [word[word_key][word_index], word_key]

def display(pics, wrong_guess, correct_guess, selected_word):
    print(pics[len(wrong_guess)])
    print()
    print('Missed letters:', end=' ')
    for letter in wrong_guess:
        print(letter, end=' ')
    print()

    blanks = '_' * len(selected_word)

    for i in range(len(selected_word)): 
        if selected_word[i] in correct_guess:
            blanks = blanks[:i] + selected_word[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end=' ')
    print()

def get_guess(guessed):
    while True:
        print('\nGuess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('\nPlease enter a single letter')
        elif guess in guessed:
            print('\nYou have already guessed that letter. Enter a different letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('\nPlease enter a Letter')
        else:
            return guess

def play_again():
    print('\nDo you want to play again? (yes or no)')
    return input().lower().startswith('y')
print('\n\t\t\t\tH A N G M A N')
wrong_guess = ''
correct_guess = ''
selected_word, key = get_word(words)
game_over = False

while True:

    print('\nThe word belongs to ' + key)
    display(pics, wrong_guess, correct_guess, selected_word)
    guess = get_guess(wrong_guess + correct_guess)
    if guess in selected_word:
        correct_guess = correct_guess + guess
        found_word = True
        for i in range(len(selected_word)):
            if selected_word[i] not in correct_guess:
                found_word = False
                break
        if found_word:
            print('\nCongratulations! You have won! The word is "' + selected_word + '"')
            game_over = True
    else:
        wrong_guess = wrong_guess + guess
        if len(wrong_guess) == len(pics) - 1:
            display(pics, wrong_guess, correct_guess, selected_word)

            print('\nYou have run out of guesses!\nThe number of wrong guesses are ' + str(len(wrong_guess)) + '\nThe number of correct guesses are ' + str(len(correct_guess)) + '\nThe correct answer was "' + selected_word + '"')

            game_over = True

    if game_over:
        if play_again():
            wrong_guess = ''
            correct_guess = ''
            game_over = False
            selected_word, key = get_word(words)
        else:
            break

