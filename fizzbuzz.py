# print fizz if divisible by 3
# print buzz if divisible by 5
# print fizzbuzz if divisible by both 3 and 5

for x in range(1, 101):
    if x % 15 == 0:
        print("Fizzbuzz")
    elif x % 5 == 0:
        print("Fizz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)
