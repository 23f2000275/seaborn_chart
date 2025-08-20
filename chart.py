import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fix random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for 500 customers
n_customers = 500

data = pd.DataFrame({
    "visits_per_month": np.random.poisson(lam=4, size=n_customers),
    "avg_time_per_visit": np.random.normal(loc=12, scale=3, size=n_customers),  # minutes
    "purchases_per_month": np.random.poisson(lam=2, size=n_customers),
    "avg_purchase_value": np.random.normal(loc=75, scale=20, size=n_customers),  # $
    "satisfaction_score": np.random.uniform(low=3.0, high=5.0, size=n_customers),  # 1-5 scale
    "referrals_per_year": np.random.poisson(lam=1, size=n_customers),
    "social_media_interactions": np.random.poisson(lam=5, size=n_customers),
})

# Introduce some realistic correlations manually:
# More visits tends to lead to more purchases
data["purchases_per_month"] += (data["visits_per_month"] * 0.5).astype(int)

# More satisfaction means more referrals and social media interaction
data["referrals_per_year"] += (data["satisfaction_score"] - 3).astype(int)
data["social_media_interactions"] += (data["satisfaction_score"] - 3).astype(int)

# Clip negative values if any due to adjustments
data = data.clip(lower=0)

# Compute correlation matrix
corr = data.corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.set(style="white")

heatmap = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    square=True,
    linewidths=.5,
    cbar_kws={"shrink": .75},
    annot_kws={"size": 10}
)

plt.title("Correlation Matrix of Customer Engagement Metrics", fontsize=14, weight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

# Save image as 512x512 pixels
plt.savefig("chart.png", dpi=100, bbox_inches='tight')
plt.show()
