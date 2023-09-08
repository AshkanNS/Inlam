import random
# ett program som kastar tärningar, 2 i de här fallet
print("Roll the dice!")
n = random.randint (1,6)
b = random.randint (1,6)
all = n + b
print(f"You rolled {n}, {b}")
print(f"You rolled total of: ", all)