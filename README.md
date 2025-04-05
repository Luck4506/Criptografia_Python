
##  Português
Este programa em Python implementa um sistema de criptografia e descriptografia usando a Cifra de Hill 2x2, uma técnica de codificação baseada em álgebra linear e operações com matrizes. O usuário pode escolher entre criptografar ou descriptografar uma mensagem, de forma simples, diretamente pelo terminal.

Ao escolher a opção desejada, o sistema:
	•	Converte as letras em números (A = 1, …, Z = 26)
	•	Agrupa os valores em pares
	•	Aplica uma multiplicação por uma matriz chave 2x2
	•	Utiliza a operação módulo 26 para manter os resultados no intervalo do alfabeto
	•	E por fim, converte os números novamente em letras para formar a mensagem final

O programa trata automaticamente frases com número ímpar de letras (duplicando a última letra) para garantir que todos os pares sejam completos.

A matriz chave utilizada na criptografia é:

A = [[2, 1],
     [3, 2]]

Na descriptografia, é usada a inversa modular dessa matriz, calculada com base em uma tabela de inversos mod 26.

Funcionalidades
	•	Criptografar frases utilizando álgebra linear
	•	Descriptografar mensagens codificadas com a mesma lógica
	•	Aceita frases com letras maiúsculas e ignora espaços
	•	Conversão letra ↔ número e número ↔ letra com base no alfabeto
	•	Compatível com operações matriciais via biblioteca NumPy


Exemplo:

Criptografar:

Digite a frase que você quer criptografar: Python

Saída:

Seu código criptografado é: ETVXRU


Descriptografar

Digite a frase que você quer descriptografar: ETVXRU

Saída:
Seu código descriptografado é: PYTHON


Tecnologias usadas:
	•	Python 3
	•	NumPy (para manipulação de matrizes)
	•	Álgebra Linear básica
	•	Cifra de Hill 2x2
	•	Módulo 26
	•	Tabela de inversos modulares
	•	Estruturas condicionais, laços e vetores

 ## English 


Hill Cipher 2x2 - Encryption and Decryption in Python

This Python program implements an encryption and decryption system using the Hill Cipher 2x2, a classical encoding technique based on linear algebra and matrix operations. The user can choose to encrypt or decrypt a message, simply through the terminal.

Upon selecting the desired option, the system:
	•	Converts letters into numbers (A = 1, …, Z = 26)
	•	Groups the values into pairs
	•	Applies a multiplication by a 2x2 key matrix
	•	Uses the modulo 26 operation to keep results within the alphabet range
	•	Finally, converts the numbers back into letters to generate the final message

If the input message has an odd number of letters, the last character is automatically duplicated to ensure all letter pairs are complete.

⸻

Key Matrix

The key matrix used for encryption is:

A = [[2, 1],
     [3, 2]]

For decryption, the modular inverse of this matrix is used, based on a mod 26 inverse lookup table.



Features
	•	Encrypt phrases using linear algebra
	•	Decrypt messages encoded with the same logic
	•	Accepts uppercase phrases and ignores spaces
	•	Converts letters ↔ numbers and vice versa, based on the alphabet
	•	Fully compatible with matrix operations using NumPy

Example

Encryption:

Enter the phrase you want to encrypt: Python

Output:

Your encrypted code is: ETVXRU


Decryption:

Enter the phrase you want to decrypt: ETVXRU

Output:

Your decrypted code is: PYTHON

Technologies Used
	•	Python 3
	•	NumPy (for matrix manipulation)
	•	Basic Linear Algebra
	•	Hill Cipher 2x2
	•	Modulo 26 arithmetic
	•	Modular inverse table
	•	Conditionals, loops, and array handling
