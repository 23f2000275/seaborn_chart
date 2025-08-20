import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# Set figure size in inches to get 512x512 pixels (dpi=100 => 5.12 inches)
plt.figure(figsize=(5.12, 5.12), dpi=100)

# Create a simple Seaborn scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")

# Save the figure as PNG with exact size
plt.savefig("chart.png", dpi=100)
plt.close()
