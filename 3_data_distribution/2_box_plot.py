import os
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib import pyplot as plt
import pandas as pd

X = pd.read_csv('../data/birdstrike.csv', usecols=["SPEED"]).dropna()

sns.boxplot(X)
plt.title('Speed vs Bird Strike Incidents')

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.show()