total_workout_count = 100
count_per_set = 10
your_workout_count = 0
remainig_sets = 0
while your_workout_count <= total_workout_count:
    your_workout_count += count_per_set
    print(your_workout_count)
    if your_workout_count == total_workout_count:
            print("COngratulations! You have completed the workout")
            break
    answer = input("Are you tired? (yes/y) / (no/n)\n")
    if answer == "yes" or answer== "y":
        answer_2 = input("Do you want to skip the remaining sets? (yes/y) / (no/n)\n")
        if answer_2 == "yes" or answer_2=="y":
            break
        elif answer_2 == "no" or answer_2 =="n":
            continue
        else:
            print("Enter a valid choice")
    elif answer == "no" or answer=="n":
        remainig_sets = total_workout_count - your_workout_count
        print(f"{remainig_sets} jumping jacks are remaining")
    else:
        print("Enter a valid choice")
print(f"You completed a total of {your_workout_count} jumping jacks")