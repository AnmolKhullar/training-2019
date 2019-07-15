# pip install numpy and pip instal matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1.3 * np.pi, 0.1)
print("X:\n", x)
y = np.sin(x)
print("Y:\n", y)
plt.plot(x, y)
plt.show()
