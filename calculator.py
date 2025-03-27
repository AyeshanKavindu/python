first_num = float(input("Your first number:"))
second_num = float(input("Your second number:"))
operation = input("What is your operation?")

if (operation == "+") :
    answer = first_num + second_num
elif (operation == "-"):
    answer = first_num - second_num
elif (operation == "/" and second_num == 0):
    answer = "Error"
elif (operation == "/" and second_num > 0):
    answer = first_num / second_num
else:
    answer = first_num * second_num

print(f"{answer}")
