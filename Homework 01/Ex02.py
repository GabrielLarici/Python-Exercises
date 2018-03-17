# Exercício 2: Escreva um programa que recebe dois números inteiros (i,j)
# e gera um array 2D. O valor de i é referente as linhas e j as colunas

import os

os.system("cls")

i = input("Informe i: ")
j = input("Informe j: ")
matrix = "\n".join([[0 for y in range(int(j))] for x in range(int(i))])

print(matrix)

