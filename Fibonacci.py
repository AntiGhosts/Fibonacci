def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev = [0, 1]
        for i in range(2, n+1):
            curr = prev[0] + prev[1]
            prev[0] = prev[1]
            prev[1] = curr
        return curr

n = int(input("Enter the number of Fibonacci sequence elements you want to calculate: "))
print("The Fibonacci sequence is: ")
for i in range(n):
    print(fibonacci(i), end = ", ")
