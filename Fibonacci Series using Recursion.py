
def fibonacci(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)


terms = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
