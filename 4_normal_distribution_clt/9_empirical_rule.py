from scipy.stats import norm

mu, sigma = 100, 15

for i in range (1,4):
    lower, upper = mu-i*sigma, mu+i*sigma
    area = norm.cdf(upper, mu, sigma) - norm.cdf(lower, mu, sigma)
    print(f"{area*100:.2f}%: of people have an IQ between {lower:.1f} and {upper:.1f} points.")

# 68.27%: of people have an IQ between 85.0 and 115.0 points.
# 95.45%: of people have an IQ between 70.0 and 130.0 points.
# 99.73%: of people have an IQ between 55.0 and 145.0 points.