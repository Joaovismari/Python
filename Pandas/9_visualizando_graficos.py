import pandas as pd
import numpy as np
import matplotlib as plt

arr = np.arange(10)

serie_1 = pd.Series(arr)

print(serie_1.plot())