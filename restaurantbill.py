user_choice = int(input("What meal do you want? 1,2 or 3:"))
guest_count = int(input("For how many guests? "))

burger_price = 10
pizza_price = 12
sushi_price = 15

if user_choice == 1:
    total_price = burger_price * guest_count
elif user_choice == 2:
    total_price = pizza_price * guest_count
elif user_choice == 3:
    total_price = sushi_price * guest_count
else:
    print("Invalid choice Please enter 1, 2, or 3.")


if total_price >= 100:
    discount_price = total_price - (total_price * 10 / 100)
    print(f"Total with discount = {discount_price}")
elif total_price >= 200:
    discount_price = total_price - (total_price * 20 / 100)
    print(f"Total with discount = {discount_price}")
else:
    discount_price = total_price
    print(f"Total with discount = {discount_price}")


