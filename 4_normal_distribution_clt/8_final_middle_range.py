from scipy.stats import norm

mu, sigma = 100, 15

middle_area = norm.cdf(120, mu, sigma) - norm.cdf(80, mu, sigma)

# AREA: 0.8176
print(f"AREA: {middle_area:.4f}")

