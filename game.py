print("\nWelcome to ReDI Hangman game by Linda")
name = input("Please enter your name: ")
print("Hello " + name + " guess the randomly generated number or the hangman dies!")
print("The game is about to start!\n Let's play ReDI Hangman!")
import random
number=random.randint(1,20)
guess=int(input("Please type in your guess between 1 and 20:"))
while guess!=number:
  count = 0
  count = count +1
  if guess<=number:
        print("Your number was too low")
  else:
        print("Your number was too high")
        guess=int(input("Please try again..."))
print("Congratulations! you saved the hangman!")






