

# Write a program to calculate the total wall area of a rectangular room (excluding. floor and ceiling) and the cost of painting it. Length, width, height, and cost per square unit will be input through the keyboard.

l = int(input("Enter length of room: "));
w = int(input("Enter width  of room: "));
h = int(input("Enter height of room: "));
costPerUnit = int(input("Enter cost per square unit of room: "));

wall_area = 2 * h * (l+w);
total_cost = wall_area*costPerUnit;

print(f"Total area floor\\ceiling: {wall_area}");
print(f"Total Cost: {total_cost}")