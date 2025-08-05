justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
#problem 1
members = len(justice_league)
print(f"There are {members} members in Justice league")
#problem 2
justice_league.append("Bat Girl")
justice_league.append("Night Wing")
print(f"New members are added to the team ,so the new team is {justice_league}")
#problem 3
position = justice_league.index("Wonder Woman")  
rearrange = justice_league.pop(position)              
justice_league.insert(0, rearrange)
print(f"The leader of the team has changed the team goes like {justice_league}")
#problem 4
superman_position = justice_league.index("Superman")
superman = justice_league.pop(superman_position)
flash_position = justice_league.index("Flash")
justice_league.insert(flash_position + 1, superman)
print(f"Due to conflicts between Aquaman and Flash we had to bring Superman in between them so the team is like {justice_league}")
#problem 5
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League Team:", justice_league)
#problem 6
justice_league.sort()
print("The team is now alphabetically arranged",justice_league)
Leader = justice_league[0]
print("The leader of the Justice League is :", Leader)