

number = int(input("Enter a number: "))


num_str = str(number)
power = len(num_str)

armstrong_sum = sum(int(digit) ** power for digit in num_str)

if number == armstrong_sum:
    print(number, "is an Armstrong number.")
else:
    print(number, "is NOT an Armstrong number.")
