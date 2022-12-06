import random
import nltk
import conf

BOT_CONFIG = conf.config

def clean(text):
  return ''.join([simbol for simbol in text.lower() if simbol in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '])

def match(example, text):
  return nltk.edit_distance(clean(text), clean(example)) / len(example) < 0.4

def get_intent(text):
  for intent, value in BOT_CONFIG['intents'].items():
    for example in value['examples']:
      if match(example, text):
        return random.choice(value['responses'])
  return 'Я ничего не понял :с'

question = input()
answer = get_intent(question)
print(answer)

while question != 'выход':
  question = input()
  answer = get_intent(question)
  print(answer)