from scipy.stats import norm

alpha = .05

Z_left = norm.ppf(alpha / 2)
Z_right = norm.ppf(1 - (alpha / 2))

print(f"Z_left: {Z_left:.2f}")
print(f"Z_right: {Z_right:.2f}")

# Z_left: -1.96
# Z_right: 1.96