import numpy as np 
import matplotlib.pyplot as plt 
  
x = np.linspace(0, 13, 100) 
  
plt.rcParams['lines.linewidth'] = 2
plt.figure() 
  
plt.plot(x, np.sin(x), label ='Line1',  
         color ='green', linestyle ="--") 
  
plt.plot(x, np.sin(x + 0.5), label ='Line2', 
         color ='black', linestyle =":") 
  
plt.axhline(0, label ='Line3', color ='black') 
  
  
plt.title('Axhline() Example') 
l = plt.legend(loc ='upper right') 
  
# legend between blue and orange  
# line 
l.set_zorder(2.5) 
  
plt.show() 