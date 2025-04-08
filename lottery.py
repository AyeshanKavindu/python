user_number = set()

while len(user_number) < 7:
  try:
      number = int(input("Enter a number:"))

      if number in user_number:
          print("The number already there!")
      else:
          user_number.add(number)
  except ValueError:
      print("please input only numbers")

for numbers in user_number:
    print(numbers)

