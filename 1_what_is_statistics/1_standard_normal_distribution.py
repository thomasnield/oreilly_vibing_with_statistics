import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Create x values
x = np.linspace(-4, 4, 1000)

# Standard normal PDF
pdf = norm.pdf(x)

# Find the z-scores for 95% confidence interval
z_lower = norm.ppf(0.025)  # -1.96 approx
z_upper = norm.ppf(0.975)  # 1.96 approx

# Plot the normal distribution
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, color='blue', label='Standard Normal Distribution')

# Shade the 95% confidence interval
plt.fill_between(x, pdf, where=(x >= z_lower) & (x <= z_upper), color='lightblue', alpha=0.5, label='95% Confidence Interval')

# Add labels and title
plt.title('Standard Normal Distribution with 95% Confidence Interval Shaded')
plt.xlabel('Z-score')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

plt.savefig(f'{__file__.replace('.py','')}.svg', transparent=True)
# Show the plot
plt.show()