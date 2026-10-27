a = 5
b = 10
a, b = b, a
print("a =", a, "b =", b)


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance =", d)


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


ch = input("Enter a character: ")
if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Not vowel")


marks = float(input("Enter marks: "))
if marks >= 90:
    print("A+")
elif marks >= 85:
    print("A")
elif marks >= 80:
    print("B+")
elif marks >= 75:
    print("B")
elif marks >= 70:
    print("C+")
elif marks >= 65:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")