import numpy as np
import matplotlib.pyplot as plt
a=np.random.randn(10000)
plt.hist(a,bins=40,facecolor="blue",edgecolor="black",alpha=0.5)
plt.show()

