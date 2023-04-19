import random 
from words import words
import string

unused_words = list()
used_words =  list()
word = ''

HANGMAN = [
    '_________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

def select_valid_word():
    selected_word = word 
    while ' ' in selected_word or selected_word == '':
        selected_word = random.choice(words)
    for i in selected_word:
        if i not in unused_words:
            unused_words.append(i)
    return str(selected_word)

def guess_letter(word):
    unguessed = list('_'*len(word))
    for i in range(len(word)):
        if word[i] == '-':
            unguessed[i] = '-'
    count, game_in_progress = 0, True
    print(''.join(unguessed))
    print('\n')
    while game_in_progress:
        inp = input('Guess a letter: ').lower()
        if inp in used_words:
            print('You have already chosen this letter. Try again')
        elif inp not in string.ascii_letters:
            print('Invalid input')
            print('Please try again')
            print('\n')
        elif inp not in unused_words:
            print('\n')
            print(f'{inp} is not in the word!')
            print(''.join(unguessed))
            print('\n')
            print('**************************')
            print('\n')
            print('\n'.join(HANGMAN[:count+1]))
            print('\n')
            print('**************************')
            count+=1         
        else:
            used_words.append(inp)
            if inp in unused_words:
                unused_words.remove(inp)
                print('\n')
                print(f'{inp} is a correct letter!')
                print('\n')
                letter_index = word.find(inp)
                while letter_index != -1:
                    unguessed[letter_index] = inp
                    letter_index = word.find(inp, letter_index+1) # remove while Trues, read about do while and while do loops and replace 71-77 with do while, rename k  
                print(''.join(unguessed))
                print('\n')

                if ''.join(unguessed) == word:
                    print(f'You Won! The word was {word}')
                    game_in_progress = False
                    
        if count == 7:
            game_in_progress = False
            print(f'You lost, the word was {word}')
                
guess_letter(select_valid_word())