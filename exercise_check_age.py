user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

if user_age < 18:
    print("Our game is not suitable for players under the age of 18.")
else:
    print(f"Welcome to our website {user_name}!")

