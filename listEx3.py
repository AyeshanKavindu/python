marks = []
sum_marks = 0

while True:

    user_input = (input("Enter your marks:(after finish press enter)"))

    if user_input != "":
        try:
            marks.append(int(user_input))
        except ValueError:
            (("Enter only numbers"))
    else :
       # average_marks = sum(marks) / len(marks)
       for mark in marks:
        sum_marks += mark

       average_marks = sum_marks / len(marks)
       print(f"Average = {average_marks}")
       break
