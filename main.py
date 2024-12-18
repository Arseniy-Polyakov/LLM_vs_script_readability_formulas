import os
import time

import telebot
from telebot import types
from huggingface_hub import InferenceClient
from PyPDF2 import PdfReader 
import tika 
from tika import parser
from pydub import AudioSegment
import whisper

from llm_inference import llm_inference

TOKEN = "7449370256:AAFmTEcRnkkLwmNbs-9ZgKyHtXNUIMzSoww"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

#UNUSED CONTENT TYPES 
unused_content_types = ["animation", "game", "photo", "sticker", "location", "contact", "video_note", "venue", "dice", 
                        "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", 
                        "delete_chat_photo", "group_chat_created", "supergroup_chat_created", "channel_chat_created", 
                        "migrate_to_chat_id", "migrate_from_chat_id", "pinned_message", 
                        "invoice", "successful_payment", "connected_website", "poll",
                        "passport_data", "proximity_alert_triggered", "video_chat_scheduled", 
                        "video_chat_started", "video_chat_ended", "video_chat_participants_invited", 
                        "web_app_data", "message_auto_delete_timer_changed", "forum_topic_created", 
                        "forum_topic_closed", "forum_topic_reopened", "forum_topic_edited", 
                        "general_forum_topic_hidden", "general_forum_topic_unhidden", "write_access_allowed", 
                        "user_shared", "chat_shared", "story"]
#BOT'S ANSWERS
hello_answer = "Hello, my name is Joseph and I am a real Englishman. I could analyse your text in English and find its complexity level"
waiting_answer_document = "Wait a minute, I am reading the document..."
waiting_answer_text = "Just a second I am reading the text now..."
waiting_answer_voice = "Just a second, please, I am listening your voice..."
waiting_answer_video = "Just a second, please, I am watching your video..."
error_answer = "Sorry, I cannot parse this file. Choose an other file or write your text manually👇"
incorrect_format = """I am so sorry, but I can parse text documents (.pdf .doc .docx .txt) only. 
Please, use an other file extension or write a text manually or send me a voice or video message"""
other_content_types_answer = """I am sorry, but I cannot parse this format. 
Please write a text message or send me a file in .pdf .doc .docx or .txt format or send me a voice or video message"""
analysing_answer = "Analysing your answer..."

#PARSING COMMANDS
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, hello_answer)

#PARSING TEXT FILES (.PDF .DOC .DOCX .TXT)
@bot.message_handler(content_types=["document"])
def parsing_document(message):
    try:
        file_id = message.document.file_id
        file_info = bot.get_file(file_id) 
        downloaded_file = bot.download_file(file_info.file_path)
        file_path = message.document.file_name
        with open(file_path, "wb") as file:
            file.write(downloaded_file)
        base, extension = os.path.splitext(file_path)
        if extension == ".pdf":
            reader = PdfReader(file_path)
            final_text = [reader.pages[i].extract_text() for i in range(len(reader.pages))]
            final_text_str = " ".join(final_text)
            bot.reply_to(message, waiting_answer_document)
            bot.reply_to(message, llm_inference(final_text_str))
        elif extension == ".doc" or extension == ".docx" or extension == ".txt":
            parsed_data = parser.from_file(file_path)
            final_text = parsed_data["content"]
            bot.reply_to(message, waiting_answer_document)
            bot.reply_to(message, llm_inference(final_text))
        else:
            bot.reply_to(message, incorrect_format)
        os.remove(file_path)
    except:
        bot.reply_to(message, error_answer)
        os.remove(file_path)

#PARSING TEXT MESSAGES 
@bot.message_handler(content_types=["text"])
def parsing_text(message):
    bot.reply_to(message, waiting_answer_text)   
    bot.reply_to(message, llm_inference(message))  

#PARSING VOICE MESSAGES
@bot.message_handler(content_types=["voice"])
def parsing_voice(message):
    try:
        voice_id = message.voice.file_id
        file_info = bot.get_file(voice_id)
        downloaded_file = bot.download_file(file_info.file_path)
        timestamp = str(int(time.time()))
        file_path = f"audio_{timestamp}_{file_info.file_path.split('/')[-1]}"
        with open(file_path, "wb") as file:
            file.write(downloaded_file)
        audio = AudioSegment.from_file(file_path)
        output_file = "output.mp3"
        audio.export(output_file, format="mp3", bitrate="192k")
        os.remove(file_path)
    except:
        bot.reply_to(message, error_answer)
        os.remove(file_path)
    bot.reply_to(message, waiting_answer_voice)
    model = whisper.load_model("turbo")
    transcription = model.transcribe(output_file)
    os.remove(output_file)
    transcription_text = transcription["text"]
    bot.reply_to(message, analysing_answer)
    bot.reply_to(message, llm_inference(transcription_text))

#PARSING VIDEO MESSAGES
@bot.message_handler(content_types=["video"])
def parsing_video(message):
    file_id = message.video.file_id
    file_info = bot.get_file(file_id)
    downloaded_video = bot.download_file(file_info.file_path)
    timestamp = str(int(time.time()))
    file_path = f"video_{timestamp}_{file_info.file_path.split('/')[-1]}"
    with open(file_path, "wb") as file:
        file.write(downloaded_video)
    bot.reply_to(message, waiting_answer_video)
    model = whisper.load_model("turbo")
    transcription = model.transcribe(file_path)
    os.remove(file_path)
    transcription_text = transcription["text"]
    bot.reply_to(message, analysing_answer)
    bot.reply_to(message, llm_inference(transcription_text))

# PARSING ALL OTHER TYPES OF CONTENT
@bot.message_handler(content_types=unused_content_types)
def parsing_other_content_types(message):
    bot.reply_to(message, other_content_types_answer)
    
bot.infinity_polling(none_stop=True)
