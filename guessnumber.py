import random

ran_number = random.randint(0, 100)

while True:
    try:
        user_input = int(input("Guess the number: ")) 

        if user_input == ran_number:
            print(f"Yes, {ran_number} is the correct one!")
            break
        elif user_input < ran_number:
            print(f"Bigger number than {user_input}")
        else:  
            print(f"Smaller number than {user_input}")

    except ValueError:
        print("Invalid input, please enter only numbers.")
