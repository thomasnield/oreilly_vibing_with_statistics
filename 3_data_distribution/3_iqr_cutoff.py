from numpy import percentile
import pandas as pd

# Get SPEED column, remove missing values
X = pd.read_csv('../data/birdstrike.csv', usecols=["SPEED"]).dropna()

# these would bound the box
q25 = percentile(X, 25)
q75 = percentile(X, 75)

iqr = q75 - q25

# Box range: 120.00 - 165.00
print(f"Box range: {q25:.2f} - {q75:.2f}")

# these would bound the whiskers
k = 1.5
cut_off = iqr * k
lower = q25 - cut_off
upper = q75 + cut_off

# Whisker range: 52.50 - 232.50
print(f"Whisker range: {lower:.2f} - {upper:.2f}")