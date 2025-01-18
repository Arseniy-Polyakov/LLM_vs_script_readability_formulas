from huggingface_hub import InferenceClient

def llm_inference(message):
    model_name = "Qwen/Qwen2.5-72B-Instruct"
    client = InferenceClient(model_name, token="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")
    output = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are an expert in English texts evaluation.\n"
                                        f"Count readability metrics in the English text {message}\n"
                                        "Metrics:\n"
                                        "1. FRE (Flesch Reading Ease)\n"
                                        "2. FKGL (Flesch-Kincaid Grade Level)\n"
                                        "3. Gunning Fox Index\n"
                                        "4. SMOG (Simple Measure of Gobbledygook)\n"
                                        "5. Automated Readability Formula (ARI)\n"
                                        "6. Spache Formula\n"
                                        "7. Dale Chall Formula\n"
                                        "8. Powers Sumner Kearl\n"
                                        "9. Coleman Liau Index\n"
                                        "10. LIX\n"
                                        "11. RIX\n"
                                        "Answer this way\n"
                                        "This text has:\n"
                                        "FRE <value>\n"
                                        "FKGL <value>\n"
                                        "Gunning Fox <value>\n"
                                        "SMOG <value>\n"
                                        "Automated Readability Formula <value>\n"
                                        "Spache Formula <value>\n"
                                        "Dale Chall Formula <value>\n"
                                        "Powers Sumner Kearl <value>\n"
                                        "Coleman Liau Index <value>\n"
                                        "LIX <value>\n"
                                        "RIX <value>\n"
                                        "If the text is written in another language say that you cannot count metrics"}],

    stream=False,
    max_tokens=650,
    temperature=0.5)
    text_complexity = output.choices[0].get('message')['content']
    return text_complexity

# def llm_inference(message):
#     model_name = "Qwen/Qwen2.5-72B-Instruct"
#     client = InferenceClient(model_name, token="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")
#     output = client.chat.completions.create(
#     messages=[
#         {"role": "system", "content": "You are an expert in English texts evaluation.\n"
#                                         "Evaluate the English text (find an answer) focusing on metrics. Based your answer on the reasoning below.\n"
#                                         "Firstly, find a text language. If it is not an English, say that you could not evaluate it and do not base on reasoning at all\n"
#                                         "If it is written in English, evaluate it\n"
#                                         "Metrics:\n"
#                                         "1. FRE (Flesch Reading Ease)\n"
#                                         "2. FKGL (Flesch-Kincaid Grade Level)\n"
#                                         "3. Gunning Fox Index\n"
#                                         "4. SMOG (Simple Measure of Gobbledygook)\n"
#                                         "5. ARI (Automated Readability Index)\n"
#                                         "6. Spache formula\n"
#                                         "7. Dale Chall\n"
#                                         "8. Powers Sumner Kearl\n"
#                                         "Answers: A1, A2, B1, B2, C1, C2\n"
#                                         f"Text: {message}\n"
#                                         "Reasoning: Evaluate the <text> by using <metrics> interpretations to choose an <answer>\n"
#                                         "Write an answer using the format: This text has <answer> level\n"
#                                         "And explain in few words (10-15 words) why did you choose this level based on metrics interpretations\n"}],
#     stream=False,
#     max_tokens=1000,
#     temperature=0.2)
#     text_complexity = output.choices[0].get('message')['content']
#     return text_complexity

# def chat_llm(message): 
#     model_name = "Qwen/Qwen2.5-72B-Instruct"
#     client = InferenceClient(model_name, token="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")
#     output = client.chat.completions.create(
#     messages=[
#         {"role": "system", "content": "You are an English teacher.\n"
#                                     "context: <You need to chat with a student on the topic of the weather.\n"
#                                     "You should chat in English, on the extremely easy level (A1 according to CEFR)\n"
#                                     "If a student makes a mistake, you need to correct it and write in the chat before the next step in your dialogue\n"
#                                     "If a student says something on the other topic except the weather, say that you need to discuss the weather only\n"
#                                     "If a student write something in the other language, say that you cannot understand this language and write that a student needs to write in English>\n"
#                                     f"[INST] Using this information <context> answer the question {message}\n"
#                                     f"User: {message}\n"
#                                     "Assistant:\n"
#                                     "[/INST]"}],
#     stream=False,
#     max_tokens=650,
#     temperature=0.6)
#     chat_answer = output.choices[0].get('message')['content']
#     return chat_answer

# def chat_llm(message): 
#     model_name = "Qwen/Qwen2.5-72B-Instruct"
#     client = InferenceClient(model_name, token="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")
#     output = client.chat.completions.create(
#     messages=[
#         {"role": "system", "content": "You are an English teacher.\n"
#                                     "context: <You need to chat with a student on the topic of the universities.\n"
#                                     "You should chat in English, on the intermediate level (B1 according to CEFR)\n"
#                                     "Do not write any salutations in your answer\n"
#                                     "If a student makes a mistake, you need to correct it and write in the chat before the next step in your dialogue\n"
#                                     "If a student says something on the other topic except the universities, say that you need to discuss universities only\n"
#                                     "If a student write something in the other language, say that you cannot understand this language and write that a student needs to write in English>\n"
#                                     f"[INST] Using this information <context> answer the question {message}\n"
#                                     f"User: {message}\n"
#                                     "Assistant:\n"
#                                     "[/INST]"}],
#     stream=False,
#     max_tokens=650,
#     presence_penalty=0.5,
#     frequency_penalty=0.5,
#     temperature=1)
#     chat_answer = output.choices[0].get('message')['content']
#     return chat_answer