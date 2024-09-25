import csv
import os

campos = ['nome' , 'preço' , 'código']
file_name = "database.csv"

#Funções que gerenciam e atualizam o csv:

def carregar_produtos():
    if not os.path.exists(file_name):
        criar_csv()
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def salvar_produtos(produtos):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = produtos[0].keys() if produtos else campos
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produtos)

def criar_csv():
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()