# Save-A=a-Soul GNU-GPL v 3.0 last update 5/25/18
# ALPHA FINISHED
# Making sure the characters are all placed when someones guesses a letter
# 
#This is a new and improved hangman game in which you must guess as many words letter by letter.
#If you get a letter that is not in the word you lose one limb each time until you lose all limbs/Denver Wydermyer/
#Denver Wydermyer
#5/25/18

import time
import random

class Hangman():
    def __init__(self):
        print("Welcome to the revolutionary game: Save-a-Soul!")
        choice = input('''
    1. Play game
    2. How to play
    3. Quit
    pick number: ''') 
        if choice == "1":
            name = input("What is your name: ")
            print("Welcome, ", name +"!")
            self.game()
        elif choice == "2":
            name = input("What is your name: ")
            self.instruct(name)
        elif choice =='3':
            self.qt()
        else:
            print("That is not a correct input. Please pick one of the numbers 1-3.")
            self.__init__()

    def instruct(self,name):
        print('''  Hello ''' +name+'''! It seems that you do not know how to play this timeless game. Save-a-soul is a new and improved word game in which you must guess as many words letter by letter.
  If you get a letter that is not in the word you lose one limb each time until you lose all limbs. As long as you have some of your friends limbs on the hanging block,
  you can continue to guess words. The game will end when all the limbs have been taken by the mean Grim Reaper.Don't mess up too much and your friends limbs will remain on the block!''')
        time.sleep(15)
        self.game()
        
    def game(self):
        guessed = str()
        wrong = 0
        file1 = open("word_phrase.txt", "r").read().split()
        words = random.randint(0, len(file1))
        word = (file1[words])
        guessed_letters = len(word) * ['_']
        print(' '.join(guessed_letters))
        guess = str(input("Guess a letter: "))
        check = self.correct(guess,guessed,word,wrong,guessed_letters)
        guessed = guessed, guess
        
    def done(self,word,guess,guessed,wrong,guessed_letters):
        if  guessed_letters == :
                self.game()
        else:
            self.cont(word,guess,guessed,wrong,guessed_letters)
    def cont(self,word,guess,guessed,wrong,guessed_letters):
        while wrong < 6:
            guess = str(input("Guess a letter: "))
            check = self.correct(guess,guessed,word,wrong,guessed_letters)
            guessed = guessed, guess
            
    def correct(self,guess,guessed,word,wrong,guessed_letters):
        if guess == guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            if guess not in guessed:
                print("Correct")
                check = True
                self.process(check,word,guess,guessed,wrong,guessed_letters)
        elif guess not in word and len(guess) == 1 and guess in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
            if guess not in guessed:
                print("Incorrect!")
                check = False
                self.process2(check,word,guess,guessed,wrong,guessed_letters)
        else:
            print("Input one letter.")
            self.game()

    def process(self,check,word,guess,guessed,wrong,guessed_letters):
            if check == True:
                letters = len(word) * ['_']
                for position , letter in enumerate(word):
                    if letter == guess:
                        guessed_letters[position] = letter
                        print(' '.join(guessed_letters))
                        print("Yay! Your friends limb remain!")
                        self.done(word,guess,guessed,wrong,guessed_letters)
                        
    def process2(self,check,word,guess,guessed,wrong,guessed_letters):
            if check == False:
                print(' '.join(guessed_letters))
                print("Wrong letter!Your friends limbs are slowly being taken away!")
                wrong = wrong+1
                self.hung_grap(word,guess,guessed,wrong,guessed_letters)
                self.done(word,guess,guessed,wrong,guessed_letters)

    def hung_grap(self,word,guess,guessed,wrong,guessed_letters):
        if wrong == 0:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     / \     ")
            print ("|             ")
            
            self.cont(word,guess,guessed,wrong,guessed_letters)
        elif wrong == 1:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     /       ")
            print ("|             ")
            
            self.cont(word,guess,guessed,wrong,guessed_letters)
        elif wrong == 2:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|             ")
            print ("|             ")
            self.cont(word,guess,guessed,wrong,guessed_letters)
        elif wrong == 3:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|      ")
            print ("|             ")
            print ("|             ")
            self.cont(word,guess,guessed,wrong,guessed_letters)
        elif wrong == 4:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|      |      ")
            print ("|             ")
            print ("|             ")
            self.cont(word,guess,guessed,wrong,guessed_letters)
        elif wrong == 5:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
            self.cont(word,guess,guessed,wrong,guessed_letters)
        else:
            print ("________      ")
            print ("|      |      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
            print ("|             ")

            
            
            print ("The word was actually "+word+" ,so your friend has sadly been taken away completely!GREAT JOB *slow clapping*!GAME OVER!")
            self.__init__()
            file1.close()
    
    def qt(self):
        quit()
        
game = Hangman()


