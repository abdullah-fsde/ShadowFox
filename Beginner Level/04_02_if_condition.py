Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
print(Australia)
print(UAE)
print(India)
City = input("Enter the name of the city: ")
if City in Australia:
    print(f"{City} is in Australia")
elif City in UAE:
    print(f"{City} is in UAE")
elif City in India:
    print(f"{City} is in India")
else:
    print(f"{City} is not found in our database")