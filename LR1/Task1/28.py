numbers = []

for r in range(3):
    a = str(input())
    n = 0
    for i in range(1, 5):
        b = a * i
        n += int(b)
    numbers.append(n)
for num in numbers:
    print(num)