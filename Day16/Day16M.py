import matplotlib.pyplot as plt
import numpy as np

N = 500
x = np.random.rand(N)
y = np.random.rand(N)
colors = (0, 1, 0)
area = np.pi * 3

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
