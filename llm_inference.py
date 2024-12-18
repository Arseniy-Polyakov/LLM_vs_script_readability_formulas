from huggingface_hub import InferenceClient

def llm_inference(message):
    model_name = "Qwen/Qwen2.5-72B-Instruct"
    client = InferenceClient(model_name, token="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")
    output = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are an expert in English texts evaluation.\n"
                                        "Evaluate the English text (find an answer) focusing on metrics. Based your answer on the reasoning below.\n"
                                        "Firstly, find a text language. If it is not an English, say that you could not evaluate it and do not base on reasoning at all\n"
                                        "If it is written in English, evaluate it\n"
                                        "Answers: A1, A2, B1, B2, C1, C2\n"
                                        f"Text: {message}\n"
                                        "Metrics:\n"
                                        "1. The number of sentences in the text\n"
                                        "2. The number of words in the text\n"
                                        "3. The number of long words (3 syllables and more)\n"
                                        "4. The number of syllables in the text\n"
                                        "5. FRE\n"
                                        "6. FKGL\n"
                                        "7. LIX\n"
                                        "8. SMOG\n"
                                        "Reasoning: Use FRE, FKGL, LIX and SMOG interpretations to choose an answer\n"
                                        "If the text is not written in English, write an answer using the format: This text is not written in English\n"
                                        "If the text is written in English, write an answer usig the format: This text has <answer> level\n"
                                        "And explain in few words (10-15 words) why did you choose this level based on FRE, FKGL, LIX and SMOG interpretations\n"}],
    stream=False,
    max_tokens=650,
    temperature=0.5)
    text_complexity = output.choices[0].get('message')['content']
    return text_complexity