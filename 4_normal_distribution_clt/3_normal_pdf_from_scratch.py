import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp, pi
import os

mu, sigma = 100, 15

def norm_pdf(x, mu, sigma):
    return (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sigma) ** 2)

x = np.linspace(mu-sigma*4, mu+sigma*4, 1000)

# y = norm.pdf(x, mu, sigma)
# make from scratch
y = [norm_pdf(_x, mu, sigma) for _x in x]

# Plot the distribution
plt.plot(x, y)
plt.title("IQ Score (Normal Distribution)")
plt.xlabel("IQ Score")
plt.ylabel("Probability Density")
plt.grid(True, alpha=0.3)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()
