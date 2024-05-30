import random

# Generate secret number
def generate_secret_number():
    return random.randint(1, 100)

# Function to check the guess
def check_riddle(secret_number, guess):
    if guess < secret_number:
        return "Muy bajo"
    elif guess > secret_number:
        return "Muy alto"
    else:
        return "Correcto, adivinaste el numero!"

