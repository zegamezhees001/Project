import pandas as pd

file1 = pd.read_csv('mergefiledata.csv')
file2 = pd.read_csv(r"C:\Users\User\Desktop\ProjectPycharm\CollectData\Phueathai.csv")

merge = pd.concat([file1,file2])

df = pd.DataFrame({'Text':merge['Text']})
df.to_csv('PheuathaiNewfile.csv')