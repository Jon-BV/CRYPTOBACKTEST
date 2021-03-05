import numpy as np
import pandas as pd
import statsmodels
from statsmodels.tsa.stattools import coint
import seaborn
import matplotlib.pyplot as plt


np.random.seed(107)

X_returns = np.random.normal(0, 1, 100)
X = pd.Series(np.cumsum(X_returns), name='X') + 50

some_noise = np.random.normal(0, 1, 100)
Y = X + 5 + some_noise
Y.name = 'Y'
pd.concat([X, Y], axis=1).plot()

(Y-X).plot()
plt.axhline((Y-X).mean(), color='red', linestyle='--')
plt.show()
# ==========End
