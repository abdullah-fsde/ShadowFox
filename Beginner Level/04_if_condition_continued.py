Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
print(Australia)
print(UAE)
print(India)
City_1 = input("Enter the name of the city: ")
City_2 = input("Enter the name of another city: ")
if City_1 and City_2 in Australia:
    print(f"Both cities are in Australia")
if City_1 and City_2 in UAE:
    print(f"Both cities are in UAE")
if City_1 and City_2 in India:
    print(f"Both cities are in India")
else:
    print("They don't belong to the same country")