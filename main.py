from src.create_token_words import create_token_words
import pandas as pd
import time



def main():

    # Create tokrn words from raw text as csv file
    create_token_words()

    
    time.sleep(10)


    # Read clean dataframe with clean tokens
    df = pd.read_csv('/home/farid/Documents/words_cleaning/src/english_tokens.csv', header=None)
    df.rename(columns={0: 'Words'}, inplace=True)
    print(df)


    






main()