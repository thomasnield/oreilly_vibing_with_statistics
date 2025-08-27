import os

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm, gaussian_kde

# Generate data for symmetrical distribution (normal)
symmetric_data = np.random.normal(loc=0, scale=1, size=1000)

# Generate data for skewed distribution (right-skewed using skewnorm)
skewed_data = skewnorm.rvs(a=5, size=1000)  # a > 0 for right skew

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot symmetrical distribution with histogram and KDE
ax1.hist(symmetric_data, bins=30, density=True, alpha=0.6, color='blue', label='Histogram')
kde_sym = gaussian_kde(symmetric_data)
x_sym = np.linspace(symmetric_data.min(), symmetric_data.max(), 1000)
ax1.plot(x_sym, kde_sym(x_sym), color='darkblue', linewidth=2, label='KDE')
ax1.set_title('Symmetrical Distribution (Normal)')
ax1.set_xlabel('Value')
ax1.set_ylabel('Density')
ax1.legend()

# Plot skewed distribution with histogram and KDE
ax2.hist(skewed_data, bins=30, density=True, alpha=0.6, color='red', label='Histogram')
kde_skew = gaussian_kde(skewed_data)
x_skew = np.linspace(skewed_data.min(), skewed_data.max(), 1000)
ax2.plot(x_skew, kde_skew(x_skew), color='darkred', linewidth=2, label='KDE')
ax2.set_title('Skewed Distribution (Right-Skewed)')
ax2.set_xlabel('Value')
ax2.set_ylabel('Density')
ax2.legend()

plt.tight_layout()

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()