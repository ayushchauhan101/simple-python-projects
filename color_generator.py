import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E', 'F']

random.shuffle(numbers)

answer = ['#']

for i in range(6):
    answer.append(numbers[i])

for i in answer:
    print(i, end='')