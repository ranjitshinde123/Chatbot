# # #imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
# #create chatbot
chatbot=ChatBot('bot')
trainer=ChatterBotCorpusTrainer(chatbot)

trainer.train(r'C:\Users\DELL\PycharmProjects\numberplate\venv\Lib\site-packages\chatterbot_corpus\data\english')

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run(host="0.0.0.0")

# from chatterbot import ChatBot
# # import time
#
# from chatterbot.trainers import ChatterBotCorpusTrainer
#
# chatbot=ChatBot('bot')
# trainer=ChatterBotCorpusTrainer(chatbot)
#
# trainer.train(r'C:\Users\DELL\PycharmProjects\numberplate\venv\Lib\site-packages\chatterbot_corpus\data\english')
# while True:
#     query=str(input(">>"))
#     print(chatbot.get_response(query))
#     if 'exit' in query:
#         break