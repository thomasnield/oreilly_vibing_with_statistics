import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

X = pd.read_csv('../data/birdstrike.csv', usecols=["HEIGHT"]).dropna()

# plot histogram
ax1.hist(X, bins=30, edgecolor='white')
ax1.set_xlabel("HEIGHT (Feet)")
ax1.set_ylabel("# Bird Strikes")
ax1.set_title('Height vs Bird Strike Incidents')
ax1.margins(x=0.01, y=0.1)

# Generate 10,000 sample means
sample_means = []
for _ in range(10_000):
    sample = X['HEIGHT'].sample(n=60)
    sample_means.append(sample.mean())

# plot histogram of sample means
ax2.hist(sample_means, bins=30, edgecolor='white')
ax2.set_xlabel("Sample Mean Height (Feet)")
ax2.set_ylabel("Frequency")
ax2.set_title('Distribution of Sample Means (n=60)')
ax2.margins(x=0.01, y=0.1)

# save file
plt.tight_layout()
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()
