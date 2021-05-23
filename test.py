import pandas as pd
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
df1 = pd.DataFrame(a, index=['row1','row2','row3'],columns=list('ABC'))

df2 = df1.copy()
df1 = df1[~df1['A'].isin([1])]
print(df1)

print("-------------------------")
cols = [ x for i, x in enumerate(df2.columns) if df2.iat[0,i]==3]

print(cols)

df2 = df2.drop(cols, axis=1)
print(df2)
