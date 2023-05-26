import math

bill = int(input(("what is the bill amount? ")))
people = int(input(("how many people you want to split the bill into? ")))
tip_percentage = int(input(("choose the tip percentage: ")))

split_bill = bill / people
print(f"The split amount before tip is {int(split_bill)} each.")

new_tip = split_bill * (0.01 * tip_percentage)
print(f"The tip per person must be {math.ceil(new_tip)}.")

final = int(split_bill) + int(new_tip)

print(f"The total amount to be paid by everyone must be {final}")