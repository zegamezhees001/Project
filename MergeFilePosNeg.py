import pandas as pd

Pos= pd.read_csv('Pos2.csv')
Neg = pd.read_csv('Neg2.csv')
Neu = pd.read_csv('Neu.csv')

Merge = pd.concat([Pos,Neg,Neu])

df = pd.DataFrame({'X':Merge['X'],
                  'Y':Merge['Y']})
df.to_csv("MergeTextNewFile2.csv")
