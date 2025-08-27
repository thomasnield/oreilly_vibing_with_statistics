import numpy as np
from math import sqrt

temps = [79,75,68,85,60,65,81,71,75,73,
      79,80,61,84,72,69,82,81,58,63,
      77,83,80,80,88,76,67,73,80,81,82]

def variance(data: [int]):
  # calculate mean
  mean = sum(data) / len(data)

  # sum all the squared differences
  squared_diffs = 0
  for x in data:
      squared_diffs += (x - mean) ** 2

  # take the average of the squared differences
  return squared_diffs / (len(data) - 1)

# just take the square root of variance
def standard_deviation(data: [int]):
  return sqrt(variance(data))

# Standard Deviation:  7.942941683069641
print("Standard Deviation: ", standard_deviation(temps))

# From NumPy: 7.94294168306964
print("From NumPy: ", np.std(temps, ddof=1))
