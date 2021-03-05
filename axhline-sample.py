import numpy as np 
import matplotlib.pyplot as plt 
  
t = np.linspace(-10, 10, 100) 
sig = 1 / t 
  
plt.axhline(y = 0, color ="green", linestyle ="--") 
plt.axhline(y = 0.5, color ="green", linestyle =":") 
plt.axhline(y = 1.0, color ="green", linestyle ="--") 
  
plt.axvline(color ="black") 
  
plt.plot(t, sig, linewidth = 2,  
         label = r"$\sigma(t) = \frac{1}{x}$") 
  
plt.xlim(-10, 10) 
plt.xlabel("t") 
plt.title("Graph of 1 / x") 
plt.legend(fontsize = 14) 
  
plt.show() 