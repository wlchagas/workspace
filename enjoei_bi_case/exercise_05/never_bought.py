#!/usr/bin/env python3
"""never_bought.py: Usuários que nunca compraram de alguma cidade especificada"""

__author__      = "Wellington Chagas"
__copyright__   = "Open-source"

__license__ = "Free"
__version__ = "1.0"
__maintainer__ = "Wellington Chagas"
__email__ = "wlchagas@gmail.com"
__status__ = "Production"

import csv
from random import randint

def build_dict(seq, key):
    # Construção de uma indexação das informações armazenadas, facilitar acesso a informação
    return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))

def include_pipe(list):
    # Construção de elementos de uma lista para string com pipes para separação
    return '|'.join(map(str,list))

def twelve_rec(list):
    # Criação de 12 recomendações aleatórias com preços abaixos de 100 reais para usuários
    temp = []
    for _ in range(11):
        temp.append(list[randint(0,len(list)-1)])
    return include_pipe(temp)

def never_bought_city(city):
    user_city = []
    buyers = []
    data = []
    recommended = []
    negated_buyers = set()

    # Nome do arquivo com as informações geradas
    csv_output = city+'_never_bought.csv'

    with open('database/users.csv',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Guardar o ID de todos os usuários da cidade
            if(row.get('city') == city):
                user_city.append(row.get('id'))

    with open('database/transactions.csv',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Guardar o ID de todos os usuários que compraram da cidade
            if(row.get('seller_id') in user_city): 
                negated_buyers.add(row.get('buyer_id'))
    with open('database/transactions.csv',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Se o usuário nunca tiver comprado da cidade, armazenar o seu ID e criar seu Dict
            if(row.get('buyer_id') not in negated_buyers):
                buyers.append(row.get('buyer_id'))
                buyer = {'id' : row.get('buyer_id'), 'products' : {'id' : [], 'price' : []} }
                data.append(buyer)

        info_by_id = build_dict(data,key='id')

    with open("database/products.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Verificar se o usuário está entre possíveis compradores
            #  -> Se estiver: verificar se o preço do produto é acima de 100 reais, 
            #                 caso seja, guardar o produto
            #  -> Se não estiver: verificar se o preço do produto é abaixo de 
            #                     100 reais e armazenar como possivel recomendação
            if(len(row.get('id')) < 10):
                user_id = row.get('user_id')
                if(user_id in buyers):
                    price = float(row.get('price'))
                    if(price >= 100):
                        update = info_by_id.get(user_id)
                        update.get('products').get('id').append(row.get('id'))
                        update.get('products').get('price').append(price)
                else:
                    price = float(row.get('price'))
                    if(price < 100):
                        recommended.append(row.get('id'))
                
    with open('db_review/'+csv_output,'w',newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter=',')
            writer.writerow(['user_id','products_id','prices','recommended'])
            for reg in data:
                products = include_pipe(reg['products']['id'])
                prices = include_pipe(reg['products']['price'])
                recoms = twelve_rec(recommended)
                if(prices != '' and products != ''):
                    writer.writerow([reg['id'], products, prices, recoms])