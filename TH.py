import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TH_data = pd.read_csv("TH1.csv")
len(TH_data)
th= TH_data["th"]
mean=th.mean()
std=th.std()
def normfun(x,mu, sigma):     #定义正太函数
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf
x = np.arange(1, 4,0.1)
y = normfun(x, mean, std)

plt.plot(x,y, color='g',linewidth = 3)
plt.hist(th, bins =20, color = 'r',alpha=0.5,rwidth= 0.9)

plt.xlabel("TH")
plt.ylabel("Probability density")
plt.title("TH Distributation")
plt.show()
