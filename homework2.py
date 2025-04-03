attempt = 0

while attempt < 5:
    user_inputs = input("What is the capital city of Japan? ")

    if user_inputs == "tokyo" or user_inputs == "Tokyo":
        print("Correct answer!")
        break
    else:
        attempt += 1  
        print(f"Incorrect! You have {5 - attempt} more chance")

if attempt == 5:
    print("You've used all 5 attempts. The correct answer is Tokyo.test")


