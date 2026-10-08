n = input("n = ")
sum = 0
f = 1

for i in range(1, int(n) + 1):
    f *= i
    sum += f

print(f"Sum of factorials: {sum}")