#!/usr/bin/python3

from nltk.corpus import stopwords
from nltk import pos_tag
from nltk import WordNetLemmatizer
from nltk import wordpunct_tokenize
import nltk
import string
from string import punctuation


class TextAnalysis:
    def __init__(self):
        pass

    def generate_tokens(self, data):
        words = [x.lower() for x in data]
        words = list(set(words))

        all_tokens = []
        for word in words:
            # Remove all punctuation
            # no_punc_word = word.translate(
            #     str.maketrans('', '', string.punctuation))
            
            # Remove all punctutation except hyphen(-)
            my_punctuation = punctuation.replace("-", "")
            no_punc_word = word.translate(
                str.maketrans('', '', my_punctuation))
            
            # tokens = nltk.word_tokenize(no_punc_word)
            tokens = pos_tag(nltk.word_tokenize(no_punc_word))
            # tokens = pos_tag(wordpunct_tokenize(no_punc_word)) #alternative tokenizer
            all_tokens.extend(tokens)

        # Lemmatize tokens to their base form
        wnl = WordNetLemmatizer()
        lemma_tokens = [wnl.lemmatize(x[0]) for x in all_tokens]

        # Remove stopwords
        filtered = [w for w in lemma_tokens if not w in stopwords.words(
            'english')]  # Tokens lemmatized

        all_filtered_tokens = list(set(filtered))

        return all_filtered_tokens
