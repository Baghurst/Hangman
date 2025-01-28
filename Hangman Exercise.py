#Hangman Exercise
#The player should get 7 lives
#You need one string to hold the secret word
#You need one string of blank spaces or underscores to hold the valid characters as they are entered

word = "Monday"
lifes = 7
#print(word[0], word[5])
print('_'*len(word))
guess = input("Guess a letter: ").lower()
while lifes > 0:
    if guess in word:
        print(f"Well done! {guess} is in the word!")
        print(f"You have {lifes} lifes left!")
    elif guess not in word:
        print(f"Sorry, {guess} is not in the word, try again!")
        lifes =  lifes - 1
        print(f"You have {lifes} lifes left!")
    #if lifes == 0:
        #print(f"GAME OVER! Your have {lifes} lifes left!")
    guess = input("Guess a letter: ").lower()
else:
    ("GAME OVER! You have 0 lifes left!")
    
    
    





































