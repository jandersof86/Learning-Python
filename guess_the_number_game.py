# This is a game in which the user guesses the number.

import random, time

# The function that asks the player to guess a max of 6 times.
def the_guessing_game():
	secret_number = random.randint(1, 20)
	print("I'm thinking of a number between 1 and 20.")
	time.sleep(2)
	print("You have six chances to guess it correctly.")
	for user_guesses in range(1, 7):
		guess = int(input("Take a guess: "))

		if guess < secret_number:
			print("Too low.")
		elif guess > secret_number:
			print("Too high.")
		else:
			break # This condition is the correct guess.

	if guess == secret_number:
		print("Good job! " + str(secret_number) + " was the secret number!")
	else:
		print("Nope. The number I was thinking of was " + str(secret_number) + ".\n")

# The game loop:
while True:
	the_guessing_game()
	time.sleep(2)
	rematch = input("Play again (y/n)? ")
	if rematch == "n":
		break

