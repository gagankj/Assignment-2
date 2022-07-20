num = int(input("enter a number to find a factorial: "))
def factorial(a):
    if a == 1 or a == 0:
        return 1
    else:
       return a * factorial(a-1)

print(factorial(num))