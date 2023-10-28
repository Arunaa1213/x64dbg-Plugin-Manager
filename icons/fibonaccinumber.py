def generate_fibonacci(n):
    fib_numbers = [0, 1]

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_numbers

    while len(fib_numbers) < n:
        next_number = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_number)

    return fib_numbers

n = int(input("Enter the number of Fibonacci numbers to generate: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci sequence of the first", n, "numbers:", fibonacci_sequence)
