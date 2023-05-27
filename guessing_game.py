import random
secret_num = random.randint(1, 100)
# print(secret_num)

level_pick = input("choose either easy or hard level: ")


def level():
    if level_pick == "hard":
        return 5
    elif level_pick == "easy":
        return 10
    else:
        return "choose again"


attempt = level()
my_guess = int(input("pick a number "))

while attempt > 0:
    print(f"you have {attempt} attempts remaining")
    if my_guess > secret_num:
        print(f"too high!")
        my_guess = int(input("guess the number again "))
        attempt -= 1
    elif my_guess < secret_num:
        print(f"too low")
        my_guess = int(input("guess the number again "))
        attempt -= 1
    else:
        print(f"you guessed correct")
        break

