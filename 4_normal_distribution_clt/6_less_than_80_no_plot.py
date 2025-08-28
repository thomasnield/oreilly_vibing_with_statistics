from scipy.stats import norm

mu, sigma = 100, 15
upper = 80

# AREA LESS THAN 80: 0.0912
print(f"AREA LESS THAN {upper}: {norm.cdf(upper, mu, sigma):.4f}")
