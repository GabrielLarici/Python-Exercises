# Exercício 3: Escreva um programa que recebe sequencia de palavras
# separados por vírgula e apresenta na tela as palavras ordenadas.

import os

os.system("cls")

wordList = input()
orderedList = wordList.split(",")
orderedList.sort()
print(orderedList)