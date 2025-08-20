import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data (e.g., correlation matrix)
data = np.random.rand(10, 10)

plt.figure(figsize=(5.12, 5.12), dpi=100)  # 512x512 pixels

# Create heatmap
sns.heatmap(data, cmap='viridis')

# Save figure as 512x512 PNG
plt.savefig("chart.png", dpi=100)
plt.close()
