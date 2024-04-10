from src.create_token_words import create_token_words
from src.english_words_cleaning import reduce_repeated_characters
from src.english_words_cleaning import remove_non_meaningful_words
from src.english_words_cleaning import correct_words, stemmed_words, lemmatized_words
from src.english_words_cleaning import unique_words, report_export_df, correct_words_final
import pandas as pd
import time



def main():

    # Create token words from raw text as csv file
    create_token_words()



    time.sleep(5)

    

    # Read data
    df = pd.read_csv('/home/farid/Documents/TAAV_vscode_prj/words_cleaning/src/english_tokens.csv', header=None)
    df.rename(columns={0: 'Words'}, inplace=True)

    
    ### 01--Remove repeated characters from dataframe
    df = reduce_repeated_characters(df)
    print(df.head(20))


    
    ### 02--Remove non-meaningful words
    df = remove_non_meaningful_words(df)
    print(df.head(20))

    
    ### 03--Correcting words in dataset
    df = correct_words(df)
    print(df.head(20))

    
    # Stemming words
    df = stemmed_words(df)
    print(df.head(20))

    
    # Lemmatize words
    df = lemmatized_words(df)
    print(df.head(20))

    
    # Correct again words
    df = correct_words_final(df)
    print(df.head(20))

    
    # Unique words
    df = unique_words(df)
    print(df.head(20))


    # Reporting and export
    df = report_export_df(df)
    print(df.head(20))




main()