#!/usr/bin/env python3
"""shuffle_word.py: Embaralhar e retornar uma palavra inserida"""

__author__      = "Wellington Chagas"
__copyright__   = "Open-source"

__license__ = "Free"
__version__ = "1.0"
__maintainer__ = "Wellington Chagas"
__email__ = "wlchagas@gmail.com"
__status__ = "Done"

from random import sample

def shuffle_word(word):
    # Embaralhar a palavra inserida utilizando o 'sample'
    shuffled_word = sample(word,len(word))
    shuffled_word = ''.join(shuffled_word)
    return shuffled_word

word = str(input("Entre com sua palavra: ")).lower()
word_list = list(word)
shuffled_word = shuffle_word(word_list)
print(shuffled_word)

# Salvar em 'results.txt'
with open("results.txt") as f:
    lines = sum(1 for _ in f)

record = ('{ "id" : '+str(lines+1)+', "word" : '+word+', "shuffled_word" : '+shuffled_word+' }\n')

with open("results.txt", "a") as result_file:
    result_file.write(record)

