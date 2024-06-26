"""
projekt_2.py: second project for Engeto Online Python Academy
author: Josef Hubáček
email: jos.hubacek@gmail.com
discord: jose9990552
"""
import random
import time 

def print_intro():
    """
    Vypíše uvítaní do hry.
    """
    separator = "-----------------------------------------------"
    print("Hi there!")
    print(separator)
    print("I've generated a random 4-digit number for you.\nLet's play a Bulls and Cows game.")
    print(separator)

def generate_secret_number():
    """
    Vygeneruje náhodné čtyř-místné číslo, které nezačíná nulou a nemá duplicity.
    """
    digits = list("0123456789")  
    random.shuffle(digits)   
    if digits[0] == '0':
        digits[0], digits[1] = digits[1], digits[0] 
    secret_number = "".join(digits[:4])  
    return secret_number

def validate_guess(guess_number):
    """
    Kontrola vstupu od uživatele.
    """
    if len(guess_number) != 4:
        print("The number must have exactly 4 digits.")  # Kontrola délky čísla
        return False
    if not guess_number.isdigit():
        print("The input must contain only numerical characters.")  # Kontrola numerických znaků
        return False
    if guess_number[0] == '0':
        print("The number must not start with zero.")  # Kontrola nezačínání nulou
        return False
    if len(set(guess_number)) != 4:
        print("The input must not contain duplicates.")  # Kontrola duplicitních číslic
        return False
    return True

def count_bulls_and_cows(secret_number, guess_number):
    """
    Počítání bulls and cows.
    """
    bulls = 0
    cows = 0
    for idx in range(4):
        if secret_number[idx] == guess_number[idx]:
            bulls += 1
        elif guess_number[idx] in secret_number:
            cows += 1
    return bulls, cows

def print_result(guess_number, bulls, cows):
    """
    Výpis bull/bulls a cow/cows podle počtu.
    """
    separator = "-----------------------------------------------"
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

def print_final_message(guess_count, start_time):
    """
    Výpis zprávy při uhodnutí.
    Výpočet času.
    """
    separator = "-----------------------------------------------"
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    minutes = int(duration // 60)
    seconds = round(duration % 60, 2)

    if guess_count == 4:
        print("Correct, you've guessed the right number in 4 guesses!\nThat's amazing.")
    else:
        print(f"Correct, you've guessed the right number in {guess_count} guesses.")
    print(separator)
    print(f"The duration was {minutes} minutes and {seconds} seconds.")
    print(f"Number of attempts: {guess_count}. Great game! Bye!")

def play_bulls_and_cows():
    """
    Hlavní funkce k hraní hry.
    """
    print_intro()
    secret_number = generate_secret_number()
    
    start_time = time.time()
    guess_count = 0

    while True:
        guess_number = input("Enter number: ")
        guess_count += 1

        if not validate_guess(guess_number):
            continue
        
        bulls, cows = count_bulls_and_cows(secret_number, guess_number)
        print_result(guess_number, bulls, cows)

        if bulls == 4:
            print_final_message(guess_count, start_time)
            break
        elif bulls == 2:
            print("Correct, you've guessed 2 numbers!\nGood job.")
            print("-----------------------------------------------")
        elif bulls == 3:
            print("Correct, you've guessed 3 numbers already!\nThat's perfect.")
            print("-----------------------------------------------")

# Start the game
play_bulls_and_cows()