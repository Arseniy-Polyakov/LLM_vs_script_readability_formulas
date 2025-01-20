import re
import json
import nltk

def script_metrics(text): 
    def syllables_counting(word):
        vowels = ["a", "o", "e", "y", "u", "i"]
        digrafs_and_trigrafs = ["ai", "ay", "ea", "ee", "ei", "ey", "oa", "oe", "oo", "ou", 
                    "ua", "ue", "ui", "uy", "eau", "aye", "iou"]
        vowels_count = len([symbol for symbol in word if symbol in vowels])
        digrafs_and_trigrafs_count = len([item for item in digrafs_and_trigrafs if item in word])
        limitations = ["the", "he", "she", "me", "we", "cafe", "apostrophe", "cliche"]
        final_count = vowels_count - digrafs_and_trigrafs_count
        if word.endswith("e") and word not in limitations: 
            final_count -= 1
        if word.startswith("y"): 
            final_count -= 1
        return final_count


    def flesch_reading_ease(text):
        sentences = nltk.sent_tokenize(text)
        text = re.sub(r"[^A-Za-z ]", "", text)
        words = nltk.word_tokenize(text)
        syllables = sum([syllables_counting(word) for word in words])
        FRE = round(206.835 - (1.015*(len(words)/len(sentences))) - (84.6*(syllables/len(words))), 2)
        return FRE

    def flesch_kincaid_readability_index(text):
        sentences = nltk.sent_tokenize(text)
        text = re.sub(r"[^A-Za-z ]", "", text)
        words = nltk.word_tokenize(text)
        syllables = sum([syllables_counting(word) for word in words])
        FKGL = round(0.39*(len(words)/len(sentences)) + (11.8*syllables/len(words)) - 15.59, 2)
        return FKGL

    def gunning_fog_index(text):
        sentences = nltk.sent_tokenize(text)
        text = re.sub(r"[^A-Za-z ]", "", text)
        words = nltk.word_tokenize(text)
        complex_words = [word for word in words if syllables_counting(word) >= 3]
        FOG = round((0.4*((len(words)/len(sentences))) + (100*(len(complex_words)/len(words)))), 2)
        return FOG

    def simple_measure_of_gobbledygook(text):
        text = re.sub(r"[^A-Za-z ]", "", text)
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
        text = re.sub(r"[^A-Za-z ]", "", text)
        words = nltk.word_tokenize(text)
        characters = re.sub(r"[^A-Za-z]", "", text)
        ARI = round(4.71*(len(characters)/len(words)) + 0.5*(len(words)/len(sentences)) - 21.43, 2)
        return ARI 

    def spache_formula(text):
        with open("text_evaluation_telegram/spache_words.txt", "rt", encoding="utf-8") as file:
            spache_words = file.read().split()
        sentences = nltk.sent_tokenize(text)
        text = re.sub(r"[^A-Za-z ]", "", text)
        words = nltk.word_tokenize(text)
        average_sentence_length = round(len(words) / len(sentences), 2) 
        unique_unfamiliar_words = [word for word in words if word not in spache_words]
        percent_unfamiliar_words = (len(unique_unfamiliar_words) * 100) / len(words)
        spache = round((0.121*average_sentence_length) + (0.082*percent_unfamiliar_words) + 0.659, 2)
        return spache

    def dale_chall(text):
        with open("text_evaluation_telegram/dale_chall.txt", "rt", encoding="utf-8") as file:
            dale_chall = file.read().split()
        sentences = nltk.sent_tokenize(text)
        text = re.sub(r"[^A-Za-z ]", "", text)
        words = nltk.word_tokenize(text)
        complex_words = [word for word in words if word not in dale_chall]
        dale_chall = round(0.1579*(100*(len(complex_words)/len(words)) + 0.0496*(len(words)/len(sentences))), 2)
        return dale_chall

    def powers_sumner_kearl(text):
        sentences = nltk.sent_tokenize(text)
        text = re.sub(r"[^A-Za-z ]", "", text)
        words = nltk.word_tokenize(text)
        average_sentence_length = round(len(words)/len(sentences), 2)
        syllables = sum([syllables_counting(word) for word in words]) 
        powers_sumner_kearl = round((0.0778*average_sentence_length) + (0.0455*syllables) + 2.7971, 2)
        return powers_sumner_kearl

    def coleman_liau_index(text):
        sentences = nltk.sent_tokenize(text)
        text = re.sub(r"[^A-Za-z ]", "", text)
        words = nltk.word_tokenize(text)
        letters = [len(word) for word in words]
        average_letters = sum(letters) / (len(words) / 100)
        average_sentences = len(sentences) / (len(words) / 100)
        coleman_index = round((0.0588*average_letters) - (0.296*average_sentences) - 15.8, 2)
        return coleman_index 

    def lix(text): 
        sentences = nltk.sent_tokenize(text)
        text = re.sub(r"[^A-Za-z ]", "", text)
        words = nltk.word_tokenize(text)
        long_words = [word for word in words if len(word) >= 7]
        words_per_sentence = [len(nltk.word_tokenize(sentence)) for sentence in sentences]
        average_number_words_per_sentence = sum(words_per_sentence) / len(words_per_sentence)
        lix = round((len(long_words) * 100 / len(words)) + average_number_words_per_sentence, 2)
        return lix

    def rix(text):
        sentences = nltk.sent_tokenize(text)
        text = re.sub(r"[^A-Za-z ]", "", text)
        words = nltk.word_tokenize(text)
        long_words = [word for word in words if len(word) >= 7]
        rix = round(len(long_words) / len(sentences), 2)
        return rix

    metrics = json.dumps({
        "FRE": flesch_reading_ease(text), 
        "FKGL": flesch_kincaid_readability_index(text),
        "Gunning Fog Index": gunning_fog_index(text), 
        "SMOG": simple_measure_of_gobbledygook(text), 
        "ARI": automated_readability_index(text),
        "Spache Formula": spache_formula(text), 
        "Dale Chall": dale_chall(text),
        "Powers Sumner Kearl": powers_sumner_kearl(text), 
        "Coleman Liau Index": coleman_liau_index(text), 
        "LIX": lix(text), 
        "RIX": rix(text)})
    
    return metrics