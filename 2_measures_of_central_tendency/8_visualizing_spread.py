import os

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

mu1, sigma1 = 10, 1.5
mu2, sigma2 = 15, 2.5

# Plot normal distribution curve

x_line = np.linspace(mu1 - sigma1 * 4, mu2 + sigma2 * 4, 1000)
y1 = norm.pdf(x_line, mu1, sigma1)
y2 = norm.pdf(x_line, mu2, sigma2)
plt.plot(x_line, y1)
plt.plot(x_line, y2)

# Add labels and show
plt.ylabel("Probability Density")
plt.grid(True, alpha=0.3)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()
