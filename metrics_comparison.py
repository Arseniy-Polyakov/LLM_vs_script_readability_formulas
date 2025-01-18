import re
import nltk
from readability import Readability

with open("text_evaluation_script/input_text.txt", "rt", encoding="utf-8") as file:
    text = file.read()

text = re.sub(r"[^A-Za-z0-9\. ]", "", text)
text_segmented = nltk.sent_tokenize(text)

readability = Readability(text)
metrics = {
    "FKGL (Flesch-Kincaid Grading Level)": readability.flesch_kincaid().score, 
    "FRE (Flesch Reading Ease)": readability.flesch().score,
    "FOG (Gunning Fog Index)": readability.gunning_fog().score,
    "CLI (Colemam Liau Index)": readability.coleman_liau().score,
    "DCR (Dale Cale Readability)": readability.dale_chall().score,
    "ARI (Automated Readability Index)": readability.ari().score,
    "Linsear Write": readability.linsear_write().score,
    "SMOG (Simple measure of Goodylegook)": Readability(" ".join(text_segmented)).smog(all_sentences=True).score,
    "Spache": readability.spache().score
}


print(metrics)