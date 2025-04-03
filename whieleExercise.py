correct_password = "ABCD"
number_attempts = 0


while number_attempts != 3:
    user_password = input("Enter your password \n")

    if user_password == correct_password :
        print("your password is correct")
        break
    else:
       number_attempts += 1
       if  number_attempts == 3:
           print("Your account has locked")


