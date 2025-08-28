from scipy.stats import norm

mu, sigma = 10, 1
area = norm.cdf(11, mu, sigma) - norm.cdf(8, mu, sigma)

print(f"The probability the battery lasts between 8 and 11 hours is {100*area:.2f}%")