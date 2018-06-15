#!/usr/bin/env python3
"""create_db.py: Automatização do script days_10.py e never_bought.py para quaisquer cidades"""

__author__      = "Wellington Chagas"
__copyright__   = "Open-source"

__license__ = "Free"
__version__ = "1.0"
__maintainer__ = "Wellington Chagas"
__email__ = "wlchagas@gmail.com"
__status__ = "Done"

import sys
import csv
from days_10 import days_bd
from never_bought import never_bought_city

if(len(sys.argv) > 2 or len(sys.argv) == 1):
    # Verifica se a chamada do script está correta
    sys.exit('Argumentos não válidos,'
            +'\nUso: \'python3 create_db.py "city"\''
            +'\nCaso a cidade informada não existe, você será informado!')

cities = []
with open('database/users.csv',newline='') as csvfile:
    # Armazena todas as cidades existentes para análise
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row.get('city') not in cities):
            cities.append(row.get('city'))

if(sys.argv[1] not in cities):
    # Armazena em um '.txt' todas as cidades que são possíveis analisar, 
    # caso a cidade informada não exista no banco
    with open('logs/cidades.txt','w+') as cities_log:
        for city in cities:
            cities_log.write(city+'\n')
    sys.exit('A cidade informada não existe,'
            +'\num arquivo chamado "cidades.txt" será criado no /diretório_atual/logs/,'
            +'\nconsulte neste arquivo as cidades existentes !')
else:
    # Cria as saídas e informa onde encontrá-las
    never_bought_city(sys.argv[1])
    days_bd(sys.argv[1])
    sys.exit('Verifique na pasta /db_review se foram criados os seguintes arquivos:'
             +'\n [1] - '+sys.argv[1]+'_never_bought.csv'
             +'\n [2] - '+sys.argv[1]+'_10_days.csv'
             +'\nCaso ocorra algum erro, entre em contato com :'
             +'\n'+__maintainer__+' pelo e-mail: '+__email__)