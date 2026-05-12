import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

tips = sns.load_dataset("tips")

plt.figure(figsize=(6, 4), facecolor="white")

sns.boxplot(x="day", y="total_bill", data=tips)

plt.title("Box Plot of Total Bill by Day")

plt.show()