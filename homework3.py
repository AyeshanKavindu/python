user_numbers = set()
while True:
    if len(user_numbers) >= 7:
        break
    try:
        user_input = int(input(f"Enter a number {len(user_numbers)+1}/7: "))
        if user_input in user_numbers:
            print("You already entered that number.")
        else:
            user_numbers.add(user_input)
    except ValueError:
        print("Please enter only numbers.")

print("\nYour lottery numbers are:")
for number in user_numbers:
    print(number)


winning_numbers = {10, 25, 32, 41, 43, 45, 50}


matched_numbers = user_numbers.intersection(winning_numbers)
match_count = len(matched_numbers)

for win_number in winning_numbers:
    print(win_number)

print(f"You matched {match_count} numbers!")

if match_count == 3:
    print("You win $4!")
elif match_count == 4:
    print("You win $15!")
elif match_count == 5:
    print("You win $200!")
elif match_count == 6:
    print("You win $30,000!")
elif match_count == 7:
    print("YOU WIN $5,000,000!")
else:
    print("Sorry, no prize")
