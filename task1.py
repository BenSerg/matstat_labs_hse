import numpy as np
import matplotlib.pyplot as plt
plt.ecdf(arr := np.random.normal(size=1000), color='red', label='График ФP')
plt.show()
print(np.quantile(arr, q=float(input())))
