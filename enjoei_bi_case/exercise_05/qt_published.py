#!/usr/bin/env python3
"""qt_published.py: Retorna quantidade de produtos com state =='published'"""

__author__      = "Wellington Chagas"
__copyright__   = "Open-source"

__license__ = "Free"
__version__ = "1.0"
__maintainer__ = "Wellington Chagas"
__email__ = "wlchagas@gmail.com"
__status__ = "Done"

import csv
from datetime import timedelta,datetime

# Definir o nome do .csv gerado com base no momento em que foi executado
csv_output = 'qt_published_'+str(datetime.today())

# Definir o formato da data conforme o banco de dados
datetimeFormat = "%Y-%m-%d %H:%M:%S.%f"

# Definir a data inicial para comparação (utilizando a data informada no texto do exercicio)
initialDate = datetime.strptime("2017-03-22 00:00:00.000000",datetimeFormat) - timedelta(days=90)

info = {'state' : [], 'created_at' : []}

with open("database/products.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        created_at = row.get('created_at')
        try:
            verifyDate = datetime.strptime(created_at,datetimeFormat)
            # Se a data de criação do produto for menos de 90 dias continuar
            if(verifyDate >= initialDate):
                state = row.get('state')
                # Se o estado for 'published' armazenar
                if(state == 'published'):
                    info['state'].append(state)
                    info['created_at'].append(created_at)
        except ValueError:
            pass

# Armazenar registros dos anúncios criados a menos de 90 dias                    
with open('db_review/'+csv_output+'.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter=',')
        writer.writerow(['state','created_at'])
        for i in range(len(info['state'])):
            writer.writerow([info['state'][i],info['created_at'][i]])

print('Quantidade de produtos com estado \'published\' = ',len(info['state']))            