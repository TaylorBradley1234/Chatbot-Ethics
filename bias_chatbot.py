from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
import os
import sys
import logging
from filter import *

#logging.basicConfig(level=logging.INFO)
toxic_thres = input("Enter toxicity threshold value: ")

bot = ChatBot(
    "Bias Chat Bot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="botDataBias.sqlite3",
    tie_breaking_method="random_response",
    response_selection_method=get_random_response
)

trainer = ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.custom.orientation_bias')

while True:
    try:
        bot_input = bot.get_response(input("User> "))
        print("Chatbot> " + str(bot_input))
        print("Response toxicity score = " + str(calc_toxicity_score(str(bot_input))))

    except(KeyboardInterrupt, EOFError, SystemExit):
        break