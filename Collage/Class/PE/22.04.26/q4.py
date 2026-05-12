import matplotlib.pyplot as plt

classes = ["Class A", "Class B", "Class C", "Class D"]
boys = [20, 25, 30, 35]
girls = [15, 20, 25, 30]

plt.figure(figsize=(6, 4), facecolor="white")

plt.bar(classes, boys, label="Boys")
plt.bar(classes, girls, bottom=boys, label="Girls")

plt.xlabel("Classes")
plt.ylabel("Number of Students")
plt.title("Stacked Bar Chart of Boys and Girls")

plt.legend()

plt.show()