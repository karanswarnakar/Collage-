

# Write a program to calculate Ramesh’s gross salary. His basic salary is input through the keyboard. DA is 40% of basic salary, HRA is 20% of basic salary, and MA is Rs.300.

bs = int(input("Enter Basic Salary: "));
da = bs*(40/100);
hra = bs*(20/100);
ma = 300;
gross = bs + da + hra + ma;
print(f"Gross Salary is {gross}");