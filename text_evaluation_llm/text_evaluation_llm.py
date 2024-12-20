from huggingface_hub import InferenceClient

model_name = "Qwen/Qwen2.5-72B-Instruct"

client = InferenceClient(model_name, token="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")

def llm_inference(user_sample):
    output = client.chat.completions.create(
    messages=[
              {"role": "system", "content": "You are an expert in english texts complexity evaluation.\n"
                                            "Evaluate the text focusing on metrics.\n"
                                            f"Text: {user_sample}\n"
                                            "Metrics:\n"
                                            "General information:\n"
                                            "1. The number of sentences in the text\n"
                                            "2. The number of words in the text\n"
                                            "3. The number of words (without stopwords) in the text\n"
                                            "4. The average number of words in the sentence\n"
                                            "5. The average number of words (without stopwords) in the text\n"
                                            "Phonological level:\n" 
                                            "1. The number of syllables in the text\n"
                                            "2. The average number of syllables in the word\n"
                                            "3. The average number of syllables in the sentence\n"
                                            "4. The number of 1-syllable, 2-syllable, 3-syllable and 4-syllable words in the text\n"
                                            "5. The average number of 1-syllable, 2-syllable, 3-syllable and 4-syllable words in the sentence\n"
                                            "Grammatical level:\n"
                                            "1. The number of nouns in the text. Do not write nouns\n"
                                            "2. The number of adjectives in the text. Do not write adjectives\n"
                                            "3. The number of verbs in the text. Do not write verbs\n"
                                            "4. The number of adverbs in the text. Do not write adverbs\n"
                                            "5. The number of pronouns in the text. Do not write pronouns\n"
                                            "7. The number of numerals in the text. Do not write numerals\n"
                                            "8. Text descriptivity: the number of adjectives divide to the whole number of all words in the text\n"
                                            "9. Text nominativity: the number of nouns divide to the whole number of all words in the text\n"
                                            "Lexical level:\n"
                                            "1. The number of A1, A2, B1, B2, C1 words in the text\n"
                                            "2. The average number of A1, A2, B1, B2, C1 words in the sentences\n"
                                            "3. The number of A1, A2, B1, B2, C1 collocations in the text\n"
                                            "4. The average number of A1, A2, B1, B2, C1 collocations in the sentences\n"
                                            "5. Type token ratio (TTR): TTR = (N / total words)\n"
                                            "where N - the number of all unique words in the text\n"
                                            "total words - the number of all words in the text.\n" 
                                            "For intanse: N = 120, total words = 240.\n" 
                                            "TTR = N / total words = 120 / 240 = 0.5\n"
                                            "6. Root Type Token Ratio (RTTR)\n"
                                            "7. Corrected Type Token Ratio (CTTR)\n"
                                            "Topic modeling:\n"
                                            "Name top 5 topics in the text\n"
                                            "Statistical metrics:\n"
                                            "1. Flesh Reading Ease (FRE)\n"
                                            "2. Flesh-Kincaid Grade Level (FKGL)\n"
                                            "3. LIX (Läsbarhetsindex)\n"
                                            "4. SMOG (Simple Measure of Gobbledygook)\n"
                                            "Write all metrics and a text level according to CEFR (A1, A2, B1, B2, C1, C2) based on these metrics\n"
                                            "If it is a text on another language, say that you could not evaluate it\n"
                                            "Extract named entities (personal names, toponyms, organizations) and write them seperately\n"
                                            "Present the result in a json format"}],
          stream=False,
          max_tokens=1000,
          temperature=0.5
          )
    return output.choices[0].get('message')['content']

text = input("Write your text here...")
print(llm_inference(text))
