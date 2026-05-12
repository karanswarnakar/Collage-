import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("darkgrid")
tips= sns.load_dataset("tips")
plt.figure(figsize=(8,6))

sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Destribution of Total bills across Different")
plt.show()




