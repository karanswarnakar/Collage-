

# Write a program to calculate the final volume of a gas using the ideal gas law. Initial volume, initial pressure, initial temperature, final pressure, and final temperature will be input through the keyboard.

ap = float(input("Enter the initial pressure: "))
avol = float(input("Enter the initial volume: "))
atem = float(input("Enter the initial temperature: "))

fp = float(input("Enter the final pressure: "))
fvol = float(input("Enter the final temperature: "))
result = (ap* avol* atem)/ (fp* fvol)
print(f"The final volume of the gas is: {result}")