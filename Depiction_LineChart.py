import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
y=np.sin(x)
z=np.sin(x**2)
plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="blue",linewidth="2")
plt.plot(x,z,"b--",label="$sin(x^2)$")
plt.title("Function Between sin(x) and sin(x^2)")
plt.ylim(-1.2,1.2)
plt.legend(loc=1)
plt.show()