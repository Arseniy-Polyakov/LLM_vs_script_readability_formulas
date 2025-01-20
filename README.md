⚡LLM vs Script: the Comparison of English Texts Evaluation Methods	
This repo represents a code which is done for the research of comparison two methods (traditional, script and generative) in counting readability formulas and finding an English complexity text level according to Common European Framework of Reference (CEFR). As for the practical part a chat-bot whcih parses different types of media content (videos, audios, documents, a plain text) is done	
Stack: 	
💻Script approach: functional programming in Python (NLTK, regular expressions, self-made NLP functions) 	
✨Generative approach: Qwen 2.5 (72 billion parameters), Hugging Face API, chain-of-thought prompting	
📲Product: Telegram chat-bot (PyTelegramBotApi2, telebot). Video (Whisper API) audio (Whisper API, ffmpeg, pydub), documents (Tika and Java 7+ for .txt, .doc, .docx; PyPDF2 for .pdf)	
