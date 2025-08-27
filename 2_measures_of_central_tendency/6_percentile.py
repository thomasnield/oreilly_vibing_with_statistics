import numpy as np

dining_tabs = [35, 47, 97, 103, 109, 135, 172, 194, 205, 225, 2100]
quartiles = np.percentile(dining_tabs, [25, 50, 75])

print("Quartiles:", quartiles)
# Quartiles: [100.  135.  199.5]

tertiles = np.percentile(dining_tabs, [33, 66])
print("Tertiles:", tertiles)
# Tertiles: [104.8 185.2]