import os

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 0, 1
x = np.linspace(mu - sigma * 4, mu + sigma * 4, 1000)
y = norm.pdf(x, mu, sigma)

level_of_significance = 0.05

lower,upper = norm.ppf(level_of_significance / 2, mu, sigma), norm.ppf(1 - (level_of_significance / 2), mu, sigma)

A = 2 * norm.cdf(lower, mu, sigma)
print(f"Significant Area: {A:.2f}")

# Plot the distribution
plt.plot(x, y)

# Shade the area outside lower and upper
shade_x = x[(x <= lower)]
shade_y = norm.pdf(shade_x, mu, sigma)
plt.fill_between(shade_x, shade_y, alpha=0.5, color='#002d8b')

shade_x = x[(x >= upper)]
shade_y = norm.pdf(shade_x, mu, sigma)
plt.fill_between(shade_x, shade_y, alpha=0.5, color='#002d8b')

plt.title("Standard Normal Distribution ")
plt.xlabel("Standard Deviations (Z-values)")
plt.ylabel("Probability Density")
plt.grid(True, alpha=0.3)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()