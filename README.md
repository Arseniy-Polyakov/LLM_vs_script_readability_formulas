**LLM vs Script: the Comparison of English Texts Evaluation Methods**

This repo represents a code which is donу to compare two methods of counting readability formulas (traditional, script and generative) and finding an English text complexity level according to Common European Framework of Reference (CEFR). As for the practical part, a chat-bot which parses different types of media content (videos, audios, documents, a plain text) is done.  

Stack: 	
  1. Script approach: functional programming in Python (NLTK, regular expressions, self-made NLP functions) 	
  2. Generative approach: Qwen 2.5 (72 billion parameters), Hugging Face API, chain-of-thought prompting	
  3. Product: Telegram chat-bot (PyTelegramBotApi2, telebot). Video (Whisper API) audio (Whisper API, ffmpeg, pydub), documents (Tika and Java 7+ for .txt, .doc, .docx; PyPDF2 for .pdf)	
