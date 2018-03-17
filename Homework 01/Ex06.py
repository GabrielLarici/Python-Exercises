# Exercício 6: Um website necessita registrar usuários e suas
# respectivas senhas. Escreva um programa que verifique a
# validade das senhas a partir dos seguintes critérios:
# 	- Pelo menos uma letra minúscula [a-z]
# 	- Pelo menos uma letra dígito [0-9]
# 	- Pelo menos uma letra maiúscula [A-Z]
# 	- Pelo menos um símbolo [$#@]
# 	- Tamanho mínimo da senha: 6
# 	- Tamanho máximo da senha: 12

import os

os.system("cls")

password = input()

specialChars = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ '''

if(any(str.isdigit(c) for c in password)      and
   any(str.islower(c) for c in password)      and
   any(str.isupper(c) for c in password)      and
   [c for c in password if c in specialChars] and
   len(password) in range (6, 13)):
	print("Senha válida")
else:
	print("Senha inválida")