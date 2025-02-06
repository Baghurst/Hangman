#Hangman Exercise
#The player should get 7 lives
#You need one string to hold the secret word
#You need one string of blank spaces or underscores to hold the valid characters as they are entered

word = "monday"
lifes = 7
entered_letters = ""
print('_'*len(word))
success = '_'*len(word)
guess = input("Guess a letter: ").lower()
entered_letters = entered_letters + guess
while lifes > 0:
    if guess in word:
        locationOfLetterInWord = word.find(guess)
        success = success[0:locationOfLetterInWord]+guess+success[locationOfLetterInWord+1:]
        print(f"Well done! {guess} is in the word: ",success)
        print(f"You have {lifes} lifes left!")
    elif guess not in word:
        print(f"Sorry, {guess} is not in the word, try again!")
        lifes =  lifes - 1
        print(f"You have {lifes} lifes left!")
    if word == success:
        print("Congratulations! YOU WON!!!")
        break
    guess = input("Guess a letter: ").lower()
    while guess in entered_letters:
       guess = input("Guess a letter: ").lower() 
    entered_letters = entered_letters + guess
else:
    print("GAME OVER! You have 0 lifes left!")
    
    











