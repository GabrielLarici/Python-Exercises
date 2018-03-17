# Exercício 7: Escreva um programa Python para
# manipulação de datas e apresente na tela:
# 	– Data atual
# 	– Ano atual
# 	– Mês atual
# 	– Dia atual
# 	– Data atual formatada dia/mês/ano
# 	– Data atual no formato:
# 		dia de mês_por_extenso de ano

import os
import datetime

os.system("cls")

now = datetime.datetime.now()

print("Data atual: {}".format(now))
print("Ano atual: {}".format(now.year))
print("Mês atual: {}".format(now.month))
print("Dia atual: {}".format(now.day))
print("Data atual formatada: {}".format(now.strftime("%d/%m/%Y")))
print(now.strftime("%d de %B de %Y"))