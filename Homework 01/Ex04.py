# Exercício 4: Escreva um programa que recebe sequencia
# e calcula aquantidade de letras e dígitos.

import os

os.system("cls")

wordSequence = input()

letters = sum(x.isalpha() for x in wordSequence)
numbers = sum(x.isdigit() for x in wordSequence)

# print result
os.system("cls")
print("Letras {}".format(letters))
print("Digitos {}".format(numbers))