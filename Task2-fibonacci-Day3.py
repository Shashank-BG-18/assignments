# Fibonacci using recursion

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get number of terms from user
n = int(input("Enter the number of terms you want in the Fibonacci series: "))
if n<=0:
    print("You must enter a positive number\n")
else:
    print("Fibonacci series:")
    print("-"*20)
    for i in range(n):
        print(fibonacci(i), end=' ')
