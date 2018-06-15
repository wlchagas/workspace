#!/usr/bin/env python3
"""top_5.py: Top 5 categorias, subcategorias e departamentos mais vendidos Rio de Janeiro"""

__author__      = "Wellington Chagas"
__copyright__   = "Open-source"

__license__ = "Free"
__version__ = "1.0"
__maintainer__ = "Wellington Chagas"
__email__ = "wlchagas@gmail.com"
__status__ = "Done"

import csv
from collections import defaultdict

def top5(list, top=5):
    # Encontra os top 5 de ocorrências dentro de uma lista
    counts = defaultdict(int)
    for x in list:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup:tup[1])[:top]

users_id = []
info = {'category' : [], 'subcategory' : [], 'department' : []}

with open("database/users.csv",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Caso seja do Rio de Janeiro, armazena o id do usuário
        if(row.get('city') == 'Rio de Janeiro'):
            users_id.append(row.get('id'))

with open("database/products.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Se o usuário que criou o anúncio, for do Rio de Janeiro, guardar as informações
        # de categoria, subcategoria e departamento
        if(row.get('user_id') in users_id):
            if(row.get('product_subcategory') != ''):
                info['category'].append(row.get('product_category'))
                info['subcategory'].append(row.get('product_subcategory'))
                info['department'].append(row.get('product_department'))

# Mostrar no terminal o top 5 de vendas em categorias, subcategorias e departamentos no Rio de Janeiro
print('== Top 5 de produtos vendidos ==')
print('Categorias : ',top5(info['category']))
print('Subcategorias : ',top5(info['subcategory']))
print('Departamentos : ',top5(info['department']))
