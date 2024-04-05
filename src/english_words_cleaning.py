import pandas as pd
import re
import nltk
from nltk.corpus import wordnet
from autocorrect import Speller
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

##### Remove repeated characters from dataset.
def remove_repeated_characters():

    # Read data
    df = pd.read_csv('/home/farid/Documents/words_cleaning/src/english_tokens.csv', header=None)
    df.rename(columns={0: 'Words'}, inplace=True)
    
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

    def reduce_repeated_characters(df):
        replacer = RepeatReplacer()
        replaced_words = []
        for word in df['Words']:
            replaced_word = replacer.replace(word)
            replaced_words.append(replaced_word)
            print(f"{word.ljust(20)}: Replaced with ---> '{replaced_word}'")
        df['Reduction Words'] = replaced_words
        return df


    # Reduce repeated characters
    df = reduce_repeated_characters(df)
    print(df.head(20))

    print('Step Remove_Repeated_Characters completed ---> Reductioned repeated characters from dataset.')
    