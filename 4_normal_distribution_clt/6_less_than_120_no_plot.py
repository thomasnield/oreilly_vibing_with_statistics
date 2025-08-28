from scipy.stats import norm

mu, sigma = 100, 15
upper = 120

# AREA LESS THAN 120: 0.9088
print(f"AREA LESS THAN {upper}: {norm.cdf(upper, mu, sigma):.4f}")
