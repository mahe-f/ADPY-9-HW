# Program to calculate recurrence relation values

def recurrence(n):
    if n == 1:
        return 1
    else:
        return recurrence(n - 1) + n

n = int(input("Enter a number: "))

print("Output:", recurrence(n))