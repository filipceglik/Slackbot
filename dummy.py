#importing and creating bot

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot('Dummy',
                  storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
                  input_adapter='chatterbot.input.TerminalAdapter',
                  output_adapter='chatterbot.output.TerminalAdapter',
                  logic_adapters=[
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.TimeLogicAdapter',
                      'chatterbot.logic.BestMatch'
                  ],
                  database='./database.json',
                  silence_performance_warning=True)

#training

chatbot.set_trainer(ListTrainer)

chatbot.train([
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
])

#response

print("You are now connected to " + chatbot.name)

while True:
    try:
        chatbot_input = chatbot.get_response(None)
    except(KeyboardInterrupt,EOFError,SystemExit):
        break





