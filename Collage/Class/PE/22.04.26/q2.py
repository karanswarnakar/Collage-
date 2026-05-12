import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

tips = sns.load_dataset("tips")

plt.figure(figsize=(6, 4), facecolor="white")

sns.barplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips
)

plt.title("Grouped Bar Plot of Total Bill by Day and Sex")

plt.show()