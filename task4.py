fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)


n = int(input("Enter a number: "))
while n >= 0:
    print(n)
    n = n - 1


base = int(input("Enter base: "))
power = int(input("Enter power: "))
print(base ** power)


total = 0
for num in range(2, 1000):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        total = total + num
print(total)


N = int(input("Enter N: "))
a, b = 0, 1
while a < N:
    print(a)
    a, b = b, a + b