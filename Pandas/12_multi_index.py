import numpy as np
import pandas as pd

a_arr = np.arange(20).reshape(5,4)
a_df = pd.DataFrame(a_arr)
print(a_df)

a_tuples = ([('A',0),('A',1),('B',2),('B',3),('B',4)])
a_index = pd.MultiIndex.from_tuples(a_tuples,names=['first','second'])#names dos index
print(a_index)

a2_df = pd.DataFrame(a_arr,index=a_index)#cria 'n' indices utilizando um multiindice como index
print(a2_df)