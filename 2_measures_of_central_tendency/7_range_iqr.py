import numpy as np

dining_tabs = [35, 47, 97, 103, 109, 135, 172, 194, 205, 225, 2100]
quartiles = np.percentile(dining_tabs, [25, 50, 75])
min, max = np.min(dining_tabs), np.max(dining_tabs)

print(f"Range: {max-min}")
# Range: 2065

print(f"Interquartile Range: {quartiles[2]-quartiles[0]}")
# Interquartile Range: 99.5