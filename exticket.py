adults = 10
children = 8
small_children = 5

user_age = int(input("What is your age? "))

if user_age >= 18:
    print(f"Price = {adults}$")
elif user_age >= 4 and user_age < 18 :
    print(f"Price = {children}$")
else:
    print(f"Price = {small_children}$")

