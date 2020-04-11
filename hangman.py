# Imports from a library a bunch of random words and stores it in the variable "word"
from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()
word = word.strip()

# Function to replace the hidden letters with the right letters if guessed
def checkLetter(letter, word, hidden_word):
    for c in word:
        if c == letter:
            hidden_word[word.index(c)] = c
            word[word.index(c)] = '*'
    return "".join(hidden_word)

#Introduces and welcomes the game and player
name = input("Enter your name: ")
print ("\nHello, " + name + ", welcome to Hangman")
print ("\nInstructions: You will be given a length of asterisks-this is how long the word is!. Then you will be given your guesses left, out of 7, and \nthen an opportunity to enter your guess. If correct, the letter will replace where its supposed to go in the asterisked word, \nbut if incorrect, you will decrease in your guesses left and will recieve an incorrect message.")

# hides the word with asterisks and prints
print ("\n\nthis is your word!")
hidden_word = ""
for char in word:
    hidden_word = hidden_word + "*"
print (hidden_word + " --> It is " + str(len(word))+ " letters")
set = set([])

# Guesses counter for how many times player can guess
guesses = 10

# Makes the word and the hidden word arrays in order to be processed later on
word_list = list(word)
hidden_word_list = list(hidden_word)

# Executes hangman if guesses are under 6
while guesses > 0 and '*' in hidden_word_list:
    print ("You have " + str(guesses) + " incorrect guesses left!")
    guess = str((input("Your Guess: ")))
    if guess == " " or guess == "":
        print("\n\nYou need to enter in a letter.\nTry Again.\n\n" +str("".join(hidden_word_list)) + " --> It is " + str(len(word))+ " letters")
    elif guess in set:
        for letter in set:
            if letter == guess:
                print ("\n\nYou already Guessed this --> Here are all of your guesses: " + str(set))
                print ("Try Again.\n\n" + str("".join(hidden_word_list)) + " --> It is " + str(len(word))+ " letters")
    elif guess in word:
        set.add(guess)
        print ("\nYou got it.\nGo Again\n")
        print (checkLetter(guess, word_list, hidden_word_list))
    else:
        set.add(guess)
        guesses = guesses - 1
        print ("\nThat's Not It")
        print ("Try Again.\n\n"+ str("".join(hidden_word_list)) + " --> It is " + str(len(word))+ " letters")
else:
    if "*" in hidden_word_list:
        print("You Lose! The word was " + word)
    else:
        print("Congrats! You got the word in under 10 incorrect guesses!")
