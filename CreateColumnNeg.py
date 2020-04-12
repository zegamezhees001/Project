import  codecs
import pandas as pd
with codecs.open('neg1.txt', 'r', "utf-8") as f:
    lines = f.readlines()
listneg=[e.strip() for e in lines]
f.close() # ปิดไฟล์
neg1=['neg']*len(listneg)

df = pd.DataFrame({'X':listneg,
                  'Y':neg1})
df.to_csv("Neg1.csv")

