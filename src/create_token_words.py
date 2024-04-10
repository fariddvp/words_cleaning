import pandas as pd
import nltk
import re
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("stopwords")


def create_token_words():

    # Read raw dataset
    english_df = pd.read_csv('/home/farid/Documents/TAAV_vscode_prj/words_cleaning/src/english_dataset.csv', header=None)
    print(english_df)
    print('step 01: Dataframe read...')

    # Convert to string and lower casting
    english_df = english_df.to_string().lower()
    print('step 02: DataFrame converted to lower cased string.')


    # Remove new lines, tabs and white spaces
    clean_data = english_df.replace("\\n", " ") # remove new lines \n
    clean_data = clean_data.replace("\\t", " ") # remove tabs
    clean_data = re.sub(re.compile(r'\s+'), " ", clean_data) # remove white spaces
    print('step 03: Removed all new lines, tabs and white spaces from dataframe.')


    # Unicode characters
    clean_data = clean_data.encode("ascii", "ignore") 
    clean_data = clean_data.decode()
    print('step 04: Apply encode and decode with ASCII on dataframe.')


    # Remove URLs
    clean_data = re.sub(r'https?://[a-zA-Z0-9\.\/\-_?=;&]*', '', clean_data)
    print('step 05: Removed all URLs from dataframe.')


    # Remove HTML tags
    clean_data = re.sub(r'<[^>]+>', '', clean_data)
    print('step 06: Removed all HTML tags from dataframe.')


    # Remove unwanted digits
    unwanted_digit = ['0','1','2','3','4','5','6','7','8','9']
    for digit in unwanted_digit:
        clean_data = clean_data.replace(digit, "")

    print('step 08: Remove unwanted digits from dataframe.')


    # Remove spacial caracters and Punctuations
    unwanted_punc = ['"',"'","#" ,'=','@','&','%','.',',',':','\\','$','^','<','>','!','?','{','}',';','\n','\t','(',')','[',']','/','*','+','#','\u200c','\ufeff','-','_','|']
    for punc in unwanted_punc:
        clean_data = clean_data.replace(punc, "")

    print('step 09: Remove spacial caracters and Punctuations from dataframe.')


    # step1: tokenization
    tokens = word_tokenize(clean_data)
    # step2: remove capitalization tokens
    normal_tokens = []
    for token in tokens:
        normal_tokens.append(token.lower())
    # step3: remove stopwords
    clean_stop_words_tokens = []
    for token in normal_tokens:
        if token not in stopwords.words("english"): 
            clean_stop_words_tokens.append(token)
    
    print(f'step 10: Create a list of tokens with ({len(clean_stop_words_tokens)}) length of tokens.')


    # Write tokens to CSV
    csv_file_path = '/home/farid/Documents/TAAV_vscode_prj/words_cleaning/src/english_tokens.csv'
    with open(csv_file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for token in clean_stop_words_tokens:
            writer.writerow([token])

    
    print('step 11: Dataframe created with clean tokens and export a csv file as: english_tokens.csv')