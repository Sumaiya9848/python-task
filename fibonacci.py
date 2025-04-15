def generate_fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a, end =" ")
        a,b = b, a + b
generate_fibonacci(5)