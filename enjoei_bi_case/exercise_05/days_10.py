#!/usr/bin/env python3
"""days_10.py: Encontrar produtos da cidade 'x', que foram anunciados a 10 dias com preço > 100"""

__author__      = "Wellington Chagas"
__copyright__   = "Open-source"

__license__ = "Free"
__version__ = "1.0"
__maintainer__ = "Wellington Chagas"
__email__ = "wlchagas@gmail.com"
__status__ = "Done"

import csv
from datetime import datetime,timedelta

# Definir o formato da data conforme o banco de dados
datetimeFormat = "%Y-%m-%d %H:%M:%S.%f"

# Definir a data inicial para comparação (utilizando a data informada no texto do exercicio 'a')
initialDate = datetime.strptime("2017-03-22 00:00:00.000000",datetimeFormat) - timedelta(days=10)

def build_dict(seq, key):
    # Construção de uma indexação das informações armazenadas, facilitar acesso a informação
    return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))

def include_pipe(list):
    # Construção de elementos de uma lista para string com pipes para separação
    return '|'.join(map(str,list))

def days_bd(city):
    user_from = []
    data = []

    # Nome do arquivo com as informações geradas
    csv_output = city+'_10_days.csv'

    with open("database/users.csv",newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Caso o usuário seja da cidade, armazenar o seu ID e criar seu Dict
            if(row.get('city') == city):
                test_id = row.get('id')
                if(test_id not in user_from):
                    user_from.append(test_id)
                    user = { 'id' : test_id, 'products' : { 'id' : [], 'price' : [] } }
                    data.append(user)
        info_by_id = build_dict(data,key='id')

    with open("database/products.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Verificar se a criação da venda do produto foi feita a mais de 10 dias
            # armazenar informações caso o usuário seja da cidade e o preço seja maior ou igual a 100 reais
            try:
                created_at = row.get('created_at')
                verifyDate = datetime.strptime(created_at,datetimeFormat)
                if(verifyDate < initialDate):
                    user_id = row.get('user_id')
                    if(user_id in user_from):
                        price = float(row.get('price'))
                        if(price >= 100):
                            update = info_by_id.get(user_id)
                            update.get('products').get('id').append(row.get('id'))
                            update.get('products').get('price').append(row.get('price'))
            except ValueError:
                pass
                        
    with open('db_review/'+csv_output,'w',newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter=',')
            writer.writerow(['user_id','products_id','prices'])
            for reg in data:
                products = include_pipe(reg['products']['id'])
                prices = include_pipe(reg['products']['price'])
                if(prices != '' and products != ''):
                    writer.writerow([reg['id'], products, prices])