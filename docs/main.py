import random

# Generate secret number
def generate_secret_number():
    return random.randint(1, 100)
# Function to check the guess
def check_guess(secret_number, input):
    if secret_number > input:
        return "El número secreto es mayor que la entrada.", False
    elif secret_number < input:
        return "El número secreto es menor que la entrada.", False
    else:
        return "Correcto, adivinó el número!", True
# Function to player shift
def player_shift():
    while True:
        try:
            entry = input("Introduce tu suposición (1-100) o escribe 'Salir': ")
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

def get_max(a, b):
    if a > b:
        return a - 1
    else: 
        return b - 1

def get_min(a, b):
    if a < b:
        return a + 1
    else: 
        return b + 1

# Feature for main game
def play():
    while True:
        secret_number = generate_secret_number()
        print("Bienvenido al juego Adivina el Número!")
        print(f"Se adivina el: {secret_number}")
        min_number = 1
        max_number = 100
        remaining_attempts = 10  # Initialize remaining attempts
        is_game_over = False
        player_assumptions = []  # List to store player guesses
        computer_assumptions = []  # List to store computer guesses
        computer_guess = random.randint(min_number, max_number)
        computer_result = ""
        while remaining_attempts > 0 and not is_game_over:
            print("#########################################")
            print(f"Te quedan {remaining_attempts} intentos.")
            # Decrement attempts after player's turn
            remaining_attempts -= 1
            player_guess = player_shift()
            if player_guess is None:
                print("Has salido del juego")
                return player_guess
            # Add player guess to the list        
            player_assumptions.append(player_guess)
             # Add computer guess to the list   
            computer_assumptions.append(computer_guess)                        
            player_result, is_player_winner = check_guess(secret_number, player_guess)
            print(f"El jugador adivina: {player_guess}. {player_result}")
            computer_result, is_computer_winner = check_guess(secret_number, computer_guess)
            print(f"La computadora adivina: {computer_guess}. {computer_result}")
            if is_player_winner:
                print("**Ganó el jugador:**")
                print("**Supuestos del jugador:**")
                for assumption in player_assumptions:
                    print(f" - {assumption}")
                is_game_over = True
            if is_computer_winner:
                print("**Ganó el computador:**")
                print("**Supuestos del computador:**")
                for assumption in computer_assumptions:
                    print(f" - {assumption}")
                is_game_over = True
            if player_guess < secret_number and computer_guess < secret_number:
                computer_guess = random.randint(get_max(player_guess,computer_guess), 100)
            elif player_guess > secret_number and computer_guess > secret_number:
                computer_guess = random.randint(1, get_min(player_guess,computer_guess))
            elif (player_guess > secret_number and computer_guess < secret_number) or (player_guess < secret_number and computer_guess > secret_number):
                computer_guess = random.randint(get_min(player_guess, computer_guess), get_max(player_guess, computer_guess))                      
        else:
            if remaining_attempts == 0 and not is_game_over:
                print(f"Lo siento! No pudiste adivinar el número en 10 intentos. El número secreto era {secret_number}.")
                play_again = input("¿Deseas jugar de nuevo? (si/no): ").lower()
                remaining_attempts = 10
                if play_again != "si":
                    break
            elif is_game_over:
                print("El juego ha terminado")
                play_again = input("¿Deseas jugar de nuevo? (si/no): ").lower()
                if play_again == "si":
                    remaining_attempts = 10
                    is_game_over = False
                else:
                    break
if __name__ == "__main__":
    play()
