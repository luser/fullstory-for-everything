#!/usr/bin/env python3

import json
import random
from pyinflect import getInflection

nouns = json.load(open('nouns.json'))['nouns']
adjs = json.load(open('adjs.json'))['adjs']

plural_nouns = [getInflection(word, tag='NNS') for word in nouns]
all_words = {
  'nouns': [n[0].title() for n in plural_nouns if n],
  'adjs': [a.title() for a in adjs]
}
with open('words.json', 'w') as f:
  json.dump(all_words, f)

