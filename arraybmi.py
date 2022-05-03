import numpy as np
import matplotlib.pyplot as plt
h1=np.array([1.83,1.76,1.69,1.86,1.77,1.73])
w1=np.array([86,74,59,95,80,68])
bmi1=w1/h1**2
print(bmi1)
plt.boxplot(bmi1)
plt.show()