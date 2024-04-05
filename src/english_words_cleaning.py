import pandas as pd
import re
import nltk
from nltk.corpus import wordnet
from autocorrect import Speller
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

##### Remove repeated characters from dataset.
# Class for reductions iterative letters
class RepeatReplacer():
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'

    def replace(self, word):
        if wordnet.synsets(word):
            return word
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
            return self.replace(repl_word)
        else:
            return repl_word

# Remove repeated characters from dataset.
def reduce_repeated_characters(df):
    replacer = RepeatReplacer()
    replaced_words = []
    for word in df['Words']:
        replaced_word = replacer.replace(word)
        replaced_words.append(replaced_word)
        print(f"{word.ljust(20)}: Replaced with ---> '{replaced_word}'")
    df['Reduction Words'] = replaced_words

    print('Step Remove_Repeated_Characters completed ---> Reductioned repeated characters from dataset.')
    return df

    

##### Delete non-information words from dataset.
#Function for remove non-meaningful words from dataset.
def remove_non_meaningful_words(df):
    df['Meaning Words'] = df['Reduction Words'].apply(lambda x: '' if not wordnet.synsets(x) else x)
#     df = df[df['Meaning Words'] != '']  # Remove rows with empty words
    
    print('Step Delete_Non_Meaning_words completed ---> Remove non-meaningful words from dataset.')
    return df





##### Correcting words in dataset.
# Initialize spell checker
def correct_words(df):

    spell = Speller()

    # Auto-correct words
    df['Corrected Words'] = df['Meaning Words'].apply(spell)

    print('Step Correct_Words completed ---> Corrected words in dataset.')
    return df



# Initialize Porter Stemmer
def stemmed_words(df):

    stemmer = PorterStemmer()

    # Perform stemming
    df['Stemmed Words'] = df['Corrected Words'].apply(lambda x: stemmer.stem(x))

    print('Step Stemming completed ---> Stemmed words in dataset.')
    return df





# Download WordNet if not already downloaded
def lemmatized_words(df):

    nltk.download('wordnet')

    # Initialize WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Perform lemmatization
    df['Lemmatized Words'] = df['Stemmed Words'].apply(lambda x: lemmatizer.lemmatize(x))

    print('Step Lemmtization completed ---> Lemmatized words in dataset.')
    return df



# Dropping duplicated words from dataset
def unique_words(df):

    df['Unique Words'] = df['Lemmatized Words'][~df['Lemmatized Words'].duplicated(keep='first')]
    print(df)
    print('Step Delete_Duplicate_Words completed ---> Droped duplicated words from dataset.')

    return df




# fill new dataframe with unique words
def report_export_df(df):
    # Count of primary dataset
    count_total = df['Words'].count()
    # Count of NaN dataset (duplicated words) in 'Unique Words' column
    count_nan = df['Unique Words'].isna().sum()

    df_new = pd.DataFrame(df[~df['Unique Words'].isna()].loc[:,'Unique Words'])
    # Update indexes new dataframe
    df_new.reset_index(drop=True, inplace=True)
    # Export dataset to csv
    df_new.to_csv('output_Unique_Words_without_NaN.csv', index=False)
    print('Step final completed ---> Exported final csv file from dataset.')
    print(f'Count of first dataset is : {count_total} and count of duplicated words are : {count_nan} So final export csv conisist of : {count_total - count_nan} entities.')
    return df_new