#!/usr/bin/env python3
"""sum_avg.py: Retornar soma e média de cinco números"""

__author__      = "Wellington Chagas"
__copyright__   = "Open-source"

__license__ = "Free"
__version__ = "1.0"
__maintainer__ = "Wellington Chagas"
__email__ = "wlchagas@gmail.com"
__status__ = "Done"

from statistics import mean

numbers = []

for i in range(5):
    number = int(input("Entre com o %d° número inteiro: " % (i+1)))
    numbers.append(number)

# Calcular a média dos números
meanNumbers = mean(numbers)
# Calcular a soma dos números
sumNumbers = sum(numbers)
print("A média dos números inseridos é : ", meanNumbers )
print("A soma dos números inseridos é : ", sumNumbers )

# Transformação em string para permitir salvar em JSON
strNumbers = ', '.join(map(str,numbers))

# Salvar no arquivo 'results.txt'
with open("results.txt") as f:
    lines = sum(1 for _ in f)

record = ('{ "id" : '+str(lines+1)+', "inserted" : [ '+strNumbers+' ], "sum" :'
        ' '+str(sumNumbers)+', "average" : '+str(meanNumbers)+' }\n')

with open("results.txt", "a") as result_file:
    result_file.write(record)

