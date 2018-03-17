# Exercício 5: Escreva um programa que recebe sequencia
# e calcula a quantidade de letras maiúsculas e minúsculas

import os

os.system("cls")

wordSequence = input()

upper = sum(x.isupper() for x in wordSequence)
lower = sum(x.islower() for x in wordSequence)

# print result
os.system("cls")
print("Maiúsculas {}".format(upper))
print("Minúsculas {}".format(lower))