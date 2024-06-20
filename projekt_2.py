"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Josef Hubáček
email: jos.hubacek@gmail.com
discord: jose9990552
"""
import random
import time 

# Hra Bulls and Cows

separator = "-----------------------------------------------"
print("Hi there!")
print(separator)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(separator)

# Generování tajného čísla jako řetězec 4 číslic
digits = list("0123456789")  # seznam číslic 
random.shuffle(digits)   # zamícháme pořadí číslic
# Aby první číslice nebyla nula
if digits[0] == '0':
    digits[0], digits[1] = digits[1], digits[0] 
# vytvoříme tajné číslo ze prvních 4 číslic
secret_number = "".join(digits[:4])  
print(secret_number)

# Začátek časomíry
start_time = time.time()

# Inicializace počtu odhadů
guess_count = 0

while True:
    guess_number = input("Enter number: ")
    guess_count += 1
    # Validace čísla
    if len(guess_number) != 4:
        print("The number must have exactly 4 digits.")
        continue
    if not guess_number.isdigit():
        print("The input must contain only numerical characters.")
        continue
    if guess_number[0] == '0':
        print("The number must not start with zero.")
        continue
    if len(set(guess_number)) != 4:
        print("The input must not contain duplicates.")
        continue
    print(separator)

    # Počítání Bulls a Cows
    bulls = 0
    cows = 0
    for idx in range(4):
        if secret_number[idx] == guess_number[idx]:
            bulls += 1
        elif guess_number[idx] in secret_number:
            cows += 1

    # Tisk výsledků pro jednotné číslo
    if bulls == 1:
        bull_str = "Bull"
    else:
        bull_str = "Bulls"

    if cows == 1:
        cow_str = "Cow"
    else:
        cow_str = "Cows"
    print(f">>> {guess_number}")
    print(f"{bulls} {bull_str}, {cows} {cow_str}")
    print(separator)

    # Pokud uživatel uhodne 2 čísla 
    if bulls == 2:
        print("Correct, you've guessed 2 numbers!\nGood job.")
        print(separator)
        
    # Pokud uživatel uhodne 3 čísla 
    if bulls == 3:
        print("Correct, you've guessed 3 numbers already!\nThat's perfect.")
        print(separator)
        
    # Pokud uživatel uhodne všechny 4 čísla 
    if bulls == 4:
        # Konec časomíry
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        minutes = int(duration // 60)
        seconds = duration % 60
        print("Correct, you've guessed the right number in 4 guesses!\nThat's amazing.")
        print(separator)
        print(f"The duration was {minutes} minutes and {seconds} seconds.")
        print(f"Number of attempts: {guess_count}")
        break