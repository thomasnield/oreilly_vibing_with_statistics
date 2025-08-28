import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os

mu, sigma = 100, 15

x = np.linspace(mu-sigma*4, mu+sigma*4, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the distribution
plt.plot(x, y)
plt.title("IQ Score (Normal Distribution)")
plt.xlabel("IQ Score")
plt.ylabel("Probability Density")
plt.grid(True, alpha=0.3)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()
