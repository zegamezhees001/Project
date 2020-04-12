import  codecs
import pandas as pd
# # pos.txt
with codecs.open('pos1.txt', 'r', "utf-8") as f:
    lines = f.readlines()
listpos=[e.strip() for e in lines]
del lines

pos1=['pos']*len(listpos)

df = pd.DataFrame({'X':listpos,
                  'Y':pos1})
df.to_csv("Pos1.csv")

