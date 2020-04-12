import re
import  pandas as pd
from pythainlp.tokenize import word_tokenize as wt
tweets= pd.read_csv('PhumchaiThai.csv')
def merge_text(text_array):
    temp = ""
    for data in text_array:
        temp += data + ' '
    return temp

# Cut word with re and word_tokenize
def handle_wt(txt):
    regx = r'https://t.co/\w+|RT\s@\w*\d*:|\n|\s|#|_|\u200b|[=]+\s[ก-๙]+\s[=]+|\n'  # regrx for handle url to split it.
    txt_ = merge_text(re.split(regx, txt))
    txt__ = merge_text(re.findall(r'[a-zA-Zก-๙]+', txt_, re.MULTILINE))
    text_raw = wt(txt__, engine='newmm')
    datas = list(filter(lambda x: x, text_raw))
    return datas


# Clean text
def clean_text(text):
    text = handle_wt(text)  # cut text to array
    texts = ' '.join(word.strip() for word in text if len(word) > 2)  # delete stopwors from text
    return texts

clean_texts=[clean_text(txt) for txt in tweets['Text']]

tweets = pd.DataFrame({'text' : clean_texts})
tweets.to_csv("CleanDataPhumchaiThai.csv")


