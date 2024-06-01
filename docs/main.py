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
        return "Correcto, adivinaste el number!"

# Function to player shift
def player_shift(secret_number):
    while True:
        try:
            entry = input("Introduce tu suposición (1-100) o escribe 'Salir' ")
            entry = entry.lower()
            
            if entry == "salir":
              return None
            guess = int(entry)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Error: La suposición debe estar entre 1 y 100.")
        except ValueError:
            print("Error: Debes introducir un número entero.")

# Function for computer shift
"""def computer_shift(secret_number):
    return random.randint(1, 100)"""

def computer_shift(secret_number, min_number=1, max_number=100):

    guess = (min_number + max_number) // 2  # Calcular la suposición media
    print(f"La computadora adivina: {guess}")
    result = check_riddle(secret_number, guess)
    print(f"result: {result}")  # print the result
    return guess


# Feature for main game
def play():
    secret_number = generate_secret_number()
    print("Bienvenido al juego Adivina el Número!")

    min_number = 1
    max_number = 100
    remaining_attempts = 10
    player_assumptions = [] # list to store player guesses
    while remaining_attempts > 0:
        print(f"Te quedan {remaining_attempts} intentos.")

        guess = player_shift(secret_number)
        if guess is None:
            print("Has salido del juego")
            return guess
        
        player_assumptions.append(guess) # Add assumptions to the list
        result = check_riddle(secret_number, guess)
        print(result)
        
        computer_guess = computer_shift(secret_number, min_number=1, max_number=100)
        result_ordenador = check_riddle(secret_number, computer_guess)
        print(f"La computadora adivina: {computer_guess} ({result_ordenador})")

        if result == "Correcto, adivinaste el number!":
            print("**Supuestas de la jugadora:**")
            for supocision in player_assumptions:
                print(f" - {supocision}")
            break # End the loop if the answer is no yes

        remaining_attempts -= 1

    else:
        print(f"Lo siento! No pudiste adivinar el número en 10 intentos. El número secreto era {secret_number}.")
    
    while True:
        play_de_nuevo = input("¿Deseas play de nuevo? (si/no): ").lower()
        if play_de_nuevo != "si":
            break  # Exit the loop if the answer is not "yes"
    

if __name__ == "__main__":
    play()
