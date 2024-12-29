import re
import nltk

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

def flesch_reading_ease(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    syllables = sum([syllables_counting(word) for word in words])
    FRE = round(206.835 - 1.015*(len(words)/len(sentences)) - 84.6*(len(syllables)/len(words)), 2)
    return FRE

def flesch_kincaid_readability_index(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    syllables = sum([syllables_counting(word) for word in words])
    FKGL = round(0.39*(len(words)/len(sentences)) + 11.8*(len(syllables)/len(words)) - 15.59, 2)
    return FKGL

def gunning_fox_index(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    complex_words = [word for word in words if syllables_counting(word) >= 3]
    FOX = round(0.4*(len(words)/len(sentences)) + 100*(len(complex_words)/len(words)), 2)
    return FOX

def simple_measure_of_gobbledygook(text):
    words = nltk.word_tokenize(text)
    complex_words = [word for word in words if syllables_counting(word) >= 3]
    root = round(len(complex_words)**0.5, 0)
    part = root % 10
    if part < 5:
        rounded_ten = root - part
    else:
        rounded_ten = root + part
    SMOG = 3 + rounded_ten
    return SMOG

def automated_readability_index(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    characters = re.sub(r"[^A-Za-z]", "", text)
    ARI = 4.71*(len(characters)/len(words)) + 0.5*(len(words)/len(sentences)) - 21.43
    return ARI 

def spache_formula(text):
    with open("spache_words.txt", "rt", encoding="utf-8") as file:
        spache_words = file.read().split()
    sentences = nltk.sent_tokenize(text)
    words = nltk.sent_tokenize(text)
    average_sentence_length = round(len(words) / len(sentences), 2) 
    unique_unfamiliar_words = [word for word in words if word not in spache_words]
    percent_unfamiliar_words = (len(unique_unfamiliar_words) * 100) / len(words)
    spache = round(0.121*average_sentence_length + 0.082*percent_unfamiliar_words + 0.659, 2)
    return spache

def dale_chall(text):
    with open("dale_chall.txt", "rt", encoding="utf-8") as file:
        dale_chall = file.read().split()
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    complex_words = [word for word in words if word not in dale_chall]
    dale_chall = 0.1579*(100*(len(complex_words)/len(words)) + 0.0496*(len(words)/len(sentences)))
    return dale_chall

def powers_sumner_kearl(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    average_sentence_length = round(len(words)/len(sentences), 2)
    syllables = sum([syllables_counting(word) for word in words]) 
    powers_sumner_kearl = round(0.0778*(average_sentence_length) + 0.0455*(syllables) + 2.7971, 2)
    return powers_sumner_kearl

# def coleman_liau_index(text):
#     sentences = nltk.sent_tokenize(text)
#     words = nltk.word_tokenize(text)
#     res_words = []
#     for i in range(100):
#         res_words.append()
                         
