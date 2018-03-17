# Exercício 1: Escreva um programa que recebe, pelo console, uma sequencia
# de números separados por vírgula e gera uma lista e uma tupla contendo
# todos estes números.

import os

os.system("cls")

numberSeq = input()
numberList = numberSeq.split(",")

#print list
print(numberList)
#print tuple
print(tuple(numberList))