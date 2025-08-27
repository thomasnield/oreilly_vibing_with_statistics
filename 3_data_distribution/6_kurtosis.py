import os

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde, uniform, t

# Generate data for platykurtic (low kurtosis, e.g., uniform distribution)
platykurtic_data = uniform.rvs(loc=-3, scale=6, size=1000)  # Centered around 0

# Generate data for mesokurtic (normal kurtosis, e.g., normal distribution)
mesokurtic_data = np.random.normal(loc=0, scale=1, size=1000)

# Generate data for leptokurtic (high kurtosis, e.g., Student's t with df=3)
leptokurtic_data = t.rvs(df=3, size=1000)  # Heavy tails

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

# Helper function to plot hist + KDE
def plot_dist(ax, data, title, color):
    ax.hist(data, bins=30, density=True, alpha=0.6, color=color, label='Histogram')
    kde = gaussian_kde(data)
    x = np.linspace(data.min(), data.max(), 1000)
    ax.plot(x, kde(x), color=f'dark{color}', linewidth=2, label='KDE')
    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()

# Plot each
plot_dist(ax1, platykurtic_data, 'Platykurtic (Low Kurtosis, Light Tails)', 'green')
plot_dist(ax2, mesokurtic_data, 'Mesokurtic (Normal Kurtosis)', 'blue')
plot_dist(ax3, leptokurtic_data, 'Leptokurtic (High Kurtosis, Heavy Tails)', 'red')

plt.tight_layout()
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()