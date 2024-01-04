import random
from Hangmanwords import words
import string
from Hangmanvisuals import lives_visual_dict, save_visual_dict

def getvalidword(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = getvalidword(words)
    wordletters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7 

    while len(wordletters) > 0 and lives > 0:
            # letters used
            # ' '.join(['a', 'b', 'cd']) --> 'a b cd'

            print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
            print(lives_visual_dict[lives])

            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('Current word', ' '.join(word_list))
            user_letter = input('Guess again: ').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in wordletters:
                    wordletters.remove(user_letter)

                else:
                    lives = lives - 1
                    print("The letter is not in the word")

            elif user_letter in used_letters:
                print('You have already used that number. Type Again: ')

            else:
                print('Invalid Character.')
                
                
            
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YOU WIN. You guessed the word correctly: ', word.upper())

        print(save_visual_dict[lives])

      

if __name__ == '__main__':
    hangman()
  
