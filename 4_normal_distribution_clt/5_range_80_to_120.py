import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os

mu, sigma = 100, 15

x = np.linspace(mu-sigma*4, mu+sigma*4, 1000)
y = norm.pdf(x, mu, sigma)

lower = 80
upper = 120

shade_x = x[(x >= lower) & (x <= upper)]
shade_y = norm.pdf(shade_x, mu, sigma)
plt.fill_between(shade_x, shade_y, alpha=0.5, color='#002d8b')  #H

print(f"AREA BETWEEN {lower} AND {upper}: {norm.cdf(upper, mu, sigma) - norm.cdf(lower, mu, sigma):.4f}")

# Plot the distribution
plt.plot(x, y)
plt.title("IQ Score (Normal Distribution)")
plt.xlabel("IQ Score")
plt.ylabel("Probability Density")
plt.grid(True, alpha=0.3)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()



