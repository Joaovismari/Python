import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
#exemplo uso do matplot
#x = [5,10,22,3,4.2,0,66,99]
#y = [1,-5,3,6,8,99,1,2]
#plt.plot(x,y)
#plt.show()
df = pd.DataFrame({'X':[0,1,2,3,4],
                   'Y':[2,3,5,10,15]})
plt.figure()
plt.suptitle('Regressão')
plt.plot(df['X'],df['Y'],'ro')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()




