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

def isUniqueChars(st):
 
    char_set = [False] * 128
    for i in range(0, len(st)):
 
        val = ord(st[i])
        if char_set[val]:
            return False
 
        char_set[val] = True
 
    return True
 
def select_valid_word():
    while True:
        word = random.choice(words)
        
        if ' ' not in word and '-' not in word and isUniqueChars(word) :
            for i in word:
                if i not in unused_words:
                    unused_words.append(i)
            return str(word)

def guess_letter(word):
    unguessed = list('-'*len(word))
    print('\n')
    print(''.join(unguessed))
    print('\n')
    count = 0
    while True:
        inp = input('Guess a letter: ')
        if inp in used_words:
            print('You have already chosen this letter. Try again')
        elif inp not in string.ascii_letters:
            print('Invalid letter')
        elif inp not in unused_words:
            print('\n')
            print(f'{inp} is not in the word!')
            print(''.join(unguessed))
            print('\n')
            print('\n'.join(HANGMAN[:count+1]))
            print('\n')
            count+=1
            if count == 7:
                print(f'You lost, the word was {word}')
                break
        else:
            used_words.append(inp)
            if inp in unused_words:
                unused_words.remove(inp)
                k = word.index(inp)
                unguessed[k] = inp
                print('\n')
                print(f'{inp} is a correct letter!')
                print('\n')
                print(''.join(unguessed))
                print('\n')
                if unused_words == []:
                    print(f'You Won! The word was {word}')
                    break
                
guess_letter(select_valid_word())