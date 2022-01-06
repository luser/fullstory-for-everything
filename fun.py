import json
import random
from pyinflect import getInflection 

nouns = json.load(open('nouns.json'))['nouns']
adjs = json.load(open('adjs.json'))['adjs']

def get_one():
  word = random.choice(nouns)
  plural = getInflection(word, tag='NNS')
  if plural:
    word = plural[0]
  if random.random() < 0.3:
    word = random.choice(adjs) + ' ' + word
  return word.title()

print(f'FullStory for {get_one()}')

