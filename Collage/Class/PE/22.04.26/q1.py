import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

tips = sns.load_dataset("tips")

plt.figure(figsize=(15, 4), facecolor="white")

plt.subplot(1, 3, 1)
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Violin Plot of Total Bill by Day")

plt.subplot(1, 3, 2)
sns.swarmplot(x="day", y="total_bill", data=tips)
plt.title("Swarm Plot of Total Bill by Day")

plt.subplot(1, 3, 3)
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Bar Plot of Total Bill by Day")

plt.tight_layout()
plt.show()