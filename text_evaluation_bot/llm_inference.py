from huggingface_hub import InferenceClient

# def llm_inference(message):
#     model_name = "Qwen/Qwen2.5-72B-Instruct"
#     client = InferenceClient(model_name, token="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")
#     output = client.chat.completions.create(
#     messages=[
#         {"role": "system", "content": "You are an expert in English texts evaluation.\n"
#                                         f"Count readability metrics in the English text {message} and choose a text level according to CEFR. Base your answer on the metrics you find\n"
#                                         "Metrics:\n"
#                                         "1. FRE (Flesch Reading Ease)\n"
#                                         "2. FKGL (Flesch-Kincaid Grade Level)\n"
#                                         "3. Gunning Fox Index\n"
#                                         "4. SMOG (Simple Measure of Gobbledygook)\n"
#                                         "5. Automated Readability Formula (ARI)\n"
#                                         "6. Spache Formula\n"
#                                         "7. Dale Chall Formula\n"
#                                         "8. Powers Sumner Kearl\n"
#                                         "9. Coleman Liau Index\n"
#                                         "10. LIX\n"
#                                         "11. RIX\n"
#                                         "Answer this way\n"
#                                         "This text has:\n"
#                                         "FRE <value>\n"
#                                         "FKGL <value>\n"
#                                         "Gunning Fox <value>\n"
#                                         "SMOG <value>\n"
#                                         "Automated Readability Formula <value>\n"
#                                         "Spache Formula <value>\n"
#                                         "Dale Chall Formula <value>\n"
#                                         "Powers Sumner Kearl <value>\n"
#                                         "Coleman Liau Index <value>\n"
#                                         "LIX <value>\n"
#                                         "RIX <value>\n"
#                                         "<CEFR level>\n"
#                                         "If the text is written in another language say that you cannot count metrics"}],

#     stream=False,
#     max_tokens=650,
#     temperature=0.5)
#     text_complexity = output.choices[0].get('message')['content']
#     return text_complexity

def llm_inference(message):
    model_name = "Qwen/Qwen2.5-72B-Instruct"
    client = InferenceClient(model_name, token="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")
    output = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are an expert in English texts evaluation.\n"
                                        "Count readability metrics FRE, Coleman Liau Index and LIX and choose an English text level according to CEFR callssifition\n"
                                        f"Text: {message}"
                                        "Metrics:\n"
                                        "1. FRE (Flesch Reading Ease)\n"
                                        "2. Coleman Liau Index\n"
                                        "3. LIX\n"
                                        "Answer this way\n"
                                        "FRE: <value>\n"
                                        "Coleman Liau Index: <value>\n"
                                        "LIX: <value>\n"
                                        "This text has <CEFR level> and provide a short explanantion (no more than 100 words) based on metrics interpretation\n"
                                        "If the text is written in another language say that you can count metrics only in English texts"}],

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