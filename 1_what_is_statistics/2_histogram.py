import numpy as np
import matplotlib.pyplot as plt

# Generate believable data: 1000 samples from a normal distribution
# Mean = 0, Standard Deviation = 1
data = np.random.normal(loc=0, scale=1, size=1000)

# Create the histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Add labels and title for realism
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.5)

# Show the plot
plt.savefig(f'{__file__.replace('.py','')}.svg', transparent=True)

plt.show()