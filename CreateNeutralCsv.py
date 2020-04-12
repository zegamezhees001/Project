import  codecs
import pandas as pd
# # pos.txt
with codecs.open('neutral.txt', 'r', "utf-8") as f:
    lines = f.readlines()
listneu=[e.strip() for e in lines]
del lines

neu =['neu']*len(listneu)

df = pd.DataFrame({'X':listneu,
                  'Y':neu})
df.to_csv("Neu.csv")

