import os
import numpy as np
from scipy.stats import gaussian_kde
from matplotlib import pyplot as plt
import pandas as pd

X = pd.read_csv('birdstrike.csv', usecols=["HEIGHT"]).dropna()

data = X['HEIGHT'].values

values, bins, bars = plt.hist(data, bins=60, edgecolor='white')
plt.xlabel("HEIGHT (Feet)")
plt.ylabel("# Bird Strikes")
plt.title('Height vs Bird Strike Incidents')
plt.margins(x=0.01, y=0.1)

# Add KDE approximation, scaled to match histogram counts
kde = gaussian_kde(data)
x_kde = np.linspace(bins.min(), bins.max(), 1000)
bin_width = bins[1] - bins[0]
y_kde = kde(x_kde) * len(data) * bin_width
plt.plot(x_kde, y_kde, color='red', linewidth=2, label='KDE')
plt.legend()

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()