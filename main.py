# from src.create_token_words import create_token_words
from src.english_words_cleaning import remove_repeated_characters
import pandas as pd
import time



def main():

    # Create token words from raw text as csv file
    create_token_words()


    time.sleep(10)


    
    ### Remove repeated characters from dataframe
    remove_repeated_characters()
    

    

    








main()