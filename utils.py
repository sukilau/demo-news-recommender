import re
from bs4 import BeautifulSoup
import jieba


def build_stopwords(filepath):
    '''
    Load customized stopwords.txt
    Return a dictionary of stopwords
    '''
    with open(filepath,'r') as file:
        return set([line.strip() for line in file])
    
    
def clean_text(text_array, stopwords):
    '''
    Remove html tags, symbols, letters a-z A-Z, numbers
    Perform chinese word segmentation
    Remove stopwords 
    Return list of cleaned text
    '''
    cleaned_text_array = []
    for i in range(len(text_array)):
        raw_text = text_array[i]
        cleaned_text = BeautifulSoup(raw_text, 'html5lib').get_text()  
        chinese_only = re.sub('[0-9a-zA-Z\xa0\r\n\t\u3000\u2000-\u206F\u2E00-\u2E7F\!#$%&()*+,\-.\/:;<=>?@\[\]^_`{|}~]','',cleaned_text)
        words = list(jieba.cut(chinese_only, cut_all=False))
        words = [word for word in words if str(word) not in stopwords]
        cleaned_text_array.append(' '.join(words))

    return cleaned_text_array