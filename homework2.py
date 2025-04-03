max_attempts = 5
user_attempts = 0

while user_attempts < max_attempts:
    user_attempts += 1
    user_answer = input("What is the capital city of Japan?\n")
    
    if user_answer.lower() == "tokyo":
        print("Correct answer!")
        break
    else:
        print(f"Incorrect answer. Attempt {user_attempts}/{max_attempts}")
        
        if user_attempts >= max_attempts:
            print("You reached the max attempts.")