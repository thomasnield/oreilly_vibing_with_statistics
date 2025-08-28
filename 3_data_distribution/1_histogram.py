import os

from matplotlib import pyplot as plt
import pandas as pd

X = pd.read_csv('../data/birdstrike.csv', usecols=["HEIGHT"]).dropna()

values, bins, bars = plt.hist(X, bins=30, edgecolor='white')
plt.xlabel("HEIGHT (Feet)")
plt.ylabel("# Bird Strikes")
plt.title('Height vs Bird Strike Incidents')
plt.margins(x=0.01, y=0.1)

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()