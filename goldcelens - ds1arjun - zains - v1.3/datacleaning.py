import pandas as pd         ### import pandas ###
import re                   ### import regex ###
import sqlite3              ### import sqlite3 ###

db = sqlite3.connect('celens.db', check_same_thread=False)
db.text_factory = bytes
mycursor = db.cursor()
q_kamusalaiii = "select * from kamusalaiii"
t_kamusalaiii = pd.read_sql_query(q_kamusalaiii, db)

def lowercase(text):
    return text.lower()

def remove_unnecessary_char(text):
    text = re.sub('\n',' ', text)
    text = re.sub('rt',' ', text)
    text = re.sub('user',' ', text)
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))',' ',text)
    text = re.sub('  +',' ', text)
    return text

def remove_nonaplhanumeric(text):
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)
    text = re.sub('  +',' ', text) 
    return text

alaiii_dict_map = dict(zip(t_kamusalaiii['alay'], t_kamusalaiii['cleaned']))            ### zip menyatukan value dengan index yang sama ###
def normalize_alaiii(text):
    for word in alaiii_dict_map:
        return ' '.join([alaiii_dict_map[word] if word in alaiii_dict_map else word for word in text.split(' ')])

"""
for word in text.split(' '):
    if word in alaiii_dict_map:
        return(' '.join([alaiii_dict_map[word])
    else:
        return(' '.join(word)
"""

### untuk proses klining data ###
def preprocess(text):
    text = lowercase(text) # 1
    text = remove_unnecessary_char(text) # 2
    text = remove_nonaplhanumeric(text) # 3
    text = normalize_alaiii(text) # 4
    return text


### untuk proses file CSV ###
def process_csv(input_file):
    first_column = input_file.iloc[:, 0]
    print(first_column)

    for tweet in first_column:
        tweet_clean = preprocess(tweet)
        query_tabel = "insert into tweet (tweet_kotor,tweet_bersih) values (?, ?)"
        val = (tweet, tweet_clean)
        mycursor.execute(query_tabel, val)
        db.commit()
        print(tweet)


### untuk proses text ###
def process_text(input_text):
    try: 
        output_text = preprocess(input_text)
        return output_text
    except:
        print("text is unreadable...")
