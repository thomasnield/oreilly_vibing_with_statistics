from math import sqrt
from scipy.stats import norm

# Given data
mu = 355.0 # Alleged population mean
n = 40  # Sample size
x_bar = 353  # Sample mean
s = 6 # Sample standard deviation
alpha = 0.05  # Significance level, .95 level of confidence

# Calculate z test value
z_stat = (x_bar - mu) / (s / sqrt(n))

# Calculate the critical Z value
critical_z = norm.ppf(1 - (alpha / 2))

print("Population mean: ", mu)
print("Sample mean: ", x_bar)
print("Sample standard deviation: ", s)
print("Sample size: ", n)
print("Level of confidence: ", 1 - alpha)
print("Level of significance: ", alpha)
print("z-statistic: ", z_stat)
print("Critical value: ", critical_z)

# Does Z fall in the critical region?
if -critical_z <= z_stat <= critical_z:
    print("Decision: Fail to reject the null hypothesis. "
          "The sample does not provide enough evidence the mean is different.")
else:
    print("Decision: Reject the null hypothesis. "
          "The sample provides enough evidence the mean is different.")
