workingday = int(input("Enter total number of working days"))
absent = int(input("Enter number of days  absent"))

percentage=(workingday-absent)/workingday*100

print("Your attendance is ",percentage)
if percentage <75 :
     print("You are not eligible for exams")
else:
     print("You are eligible for writing exam")