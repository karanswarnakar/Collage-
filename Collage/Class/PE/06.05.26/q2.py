import seaborn as sns
import matplotlib.pyplot as plt


iris = sns.load_dataset("iris")
corr_matrix = iris.drop(columns=['species']).corr()
plt.figure(figsize=(8,6))

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix of iris Dataset")
plt.show()


