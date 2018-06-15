#!/usr/bin/env python3
"""palindrome.py: Verificar se a sequência de caracteres é palindromo"""

__author__      = "Wellington Chagas"
__copyright__   = "Open-source"

__license__ = "Free"
__version__ = "1.0"
__maintainer__ = "Wellington Chagas"
__email__ = "wlchagas@gmail.com"
__status__ = "Done"

def verify_palindrome(word):
    # Verificar se é palindromo
    if(word == word[::-1]):
        return True
    return False

word = str(input("Entre com sua palavra: ")).lower()
# Retirar espaços, caracteres especiais, aceitar apenas alfa-numericos
formatted_word = ''.join(c for c in word if c.isalnum())
palindrome = verify_palindrome(formatted_word)
print(palindrome)

# Salvar em 'results.txt'
with open("results.txt") as f:
    lines = sum(1 for _ in f)

record = ('{ "id" : '+str(lines+1)+', "word" : "'+word+'", "palindrome" : '+str(palindrome)+' }\n')

with open("results.txt", "a") as result_file:
    result_file.write(record)

