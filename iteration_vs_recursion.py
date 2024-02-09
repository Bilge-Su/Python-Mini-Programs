def iterative_factorial(n):
    num = abs(n)
    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    return factorial
print(iterative_factorial(3))

def recursive_factorial(n):
    num = abs(n)
    if num == 1 : return num
    else : return num * recursive_factorial(n - 1)
print(recursive_factorial(5))