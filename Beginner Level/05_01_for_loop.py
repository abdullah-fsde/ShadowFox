import random
rolls = 20
count_1 = 0
count_6 = 0
double_6_count = 0
previous_move = 0
for i in range(1,rolls+1):
    die = random.randint(1,6)
    print(f"Roll {i} : {die}")
    if die == 1:
        count_1 += 1
    elif die == 6:
        count_6 += 1
        if previous_move == 6:
            double_6_count += 1
        else:
            pass
    else:
        pass
    previous_move = die
print(f"You got 1 ,{count_1} times")
print(f"You got 6 ,{count_6} times")
print(f"You got double 6, {double_6_count} times")
print("Thanks for playing!")