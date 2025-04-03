total = 0
while True:
    try:
        input_number = int(input("Enter your numbers, to stop Enter 0: "))

        if input_number == 0:
            print(f"Your Total is {total}")  
            break
        else:
            total += input_number 
    except ValueError:
        print("invalid, please enter only numbers")
