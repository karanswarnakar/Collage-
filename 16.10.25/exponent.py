

# Write a program to calculate the value of an exponential expression (a^b). The base and exponent will be input through the keyboard.

base = int(input("Enter base value: "));
exp = int(input("Enter exponent value: "));

result = base**exp;

print(f"Base {base} and Exponent {exp} is: {result}");
