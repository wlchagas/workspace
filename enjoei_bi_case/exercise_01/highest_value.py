#!/usr/bin/env python3
"""highest_value.py: Encontrar e imprimir o maior número entre cinco números"""

__author__      = "Wellington Chagas"
__copyright__   = "Open-source"

__license__ = "Free"
__version__ = "1.0"
__maintainer__ = "Wellington Chagas"
__email__ = "wlchagas@gmail.com"
__status__ = "Done"

numbers = []

for i in range(5):
    number = int(input("Entre com o %d° número inteiro: " % (i+1)))
    numbers.append(number)

# Encontra o maior valor entre os números inseridos
highNumber = max(numbers)
print("O maior valor entre os números inseridos é : ", highNumber )

# Transformação em string para permitir salvar em JSON
strNumbers = ', '.join(map(str,numbers))

# Salvar no arquivo 'results.txt'
with open("results.txt") as f:
    lines = sum(1 for _ in f)

record = ('{ "id" : '+str(lines+1)+', "inserted" : [ '+strNumbers+' ]'
           ', "highest" : '+str(highNumber)+' }\n')
with open("results.txt", "a") as result_file:
    result_file.write(record)

