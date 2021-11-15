from flask import Flask, request, jsonify
from wabot import WABot
import json

application = app = Flask(__name__)

@app.route('/', methods=['POST'])
def home_view(): 
        return "<h1>Welcome to ISM-Whatsapp micro-service</h1>"

@app.route('/whatsapp', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = WABot(request.json)
        return bot.processing()

if(__name__) == '__main__':
    app.run(debug=True)