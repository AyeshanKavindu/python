import random

ran_number = random.randint(0, 100)

while True:
    try:
        user_input = int(input("Guess the number: ")) 

        if user_input == ran_number:
            print(f"Yes, {ran_number} is the correct answer!")
            break
        else:
            print("Try again!")

    except ValueError:
        print("Invalid input, please enter only numbers.")
