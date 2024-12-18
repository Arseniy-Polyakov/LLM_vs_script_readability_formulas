import re
import logging
import nltk
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
input_text = input("Write your text here...")

#PREPRPOCESSING 
text_preprocessed = re.sub(r"[\W\- ]", "", input_text)
text_preprocessed = text_preprocessed.lower()
text_tokenized = nltk.word_tokenize(text_preprocessed)
text_lemmatized = [lemmatizer.lemmatize(token) for token in text_tokenized]

#GENERAL STATISTICS
sentences = nltk.sent_tokenize(input_text)
sentences_count = len(sentences)
words_count = len(text_lemmatized)

with open("stopwords.txt", "rt", encoding="utf-8") as file:
    file = file.read()
    stopwords = file.split()

words_without_stopwords = [word for word in text_lemmatized if word not in stopwords]
words_without_stopwords_count = len(words_without_stopwords)

average_words_per_sent = round(words_count / sentences_count, 2)
average_words_without_stopwords_per_sent = round(words_without_stopwords_count / sentences_count, 2)

data_general = {"Sentences": sentences_count, 
                             "Words": words_count, 
                             "Words without stopwords": words_without_stopwords_count, 
                             "Words per sentence": average_words_per_sent, 
                             "Words without stopwords per sentence": average_words_without_stopwords_per_sent}

#PHONOLOGICAL LEVEL
def syllables_counting(word):
    vowels = ["a", "o", "e", "y", "u", "i"]
    digrafs_and_trigrafs = ["ai", "ay", "ea", "ee", "ei", "ey", "oa", "oe", "oo", "ou", 
            "ow", "ua", "ue", "ui", "uy", "eau", "iou", "aye", "iou"]
    vowels_count = len([symbol for symbol in word if symbol in vowels])
    digrafs_and_trigrafs_count = len([item for item in digrafs_and_trigrafs if item in word])
    limitations = ["he", "she", "me", "we", "cafe", "apostrophe"]
    final_count = vowels_count - digrafs_and_trigrafs_count
    if word.endswith("e") and word not in limitations: 
        final_count -= 1
    return final_count

syllables_count = sum([syllables_counting(word) for word in words_without_stopwords])
average_syllables_per_word = syllables_count / words_without_stopwords_count
average_syllables_per_sent = syllables_count / sentences_count
one_syllable_count, two_syllables_count, three_syllables_count, four_syllables_count, more_syllables_count = 0, 0, 0, 0, 0
syllables = {"1-syllable": one_syllable_count, 
             "2-syllables": two_syllables_count, 
             "3-syllables": three_syllables_count, 
             "4-syllables": four_syllables_count, 
             "5 and more syllables": more_syllables_count}

for word in words_without_stopwords:
    if syllables_counting(word) == 1: 
        syllables["1-syllable"] += 1
    elif syllables_counting(word) == 2:
        syllables["2-syllables"] += 1
    elif syllables_counting(word) == 3:
        syllables["3-syllables"] += 1
    elif syllables_counting(word) == 4:
        syllables["4-syllables"] += 1
    else:
        syllables["5 and more syllables"] += 1

logging.info(syllables)

