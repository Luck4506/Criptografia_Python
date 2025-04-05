import numpy as np
frase = list(input('Digite a frase que você quer criptografar: ').strip().upper().replace(" ", ""))
if len(frase) % 2 != 0:
    frase.append(frase[-1])
t = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
frase = np.array(frase).reshape(1, -1)
m, n = frase.shape
I = []
P = []
TC = []
cripto = []
for letra in frase.flatten():  
    posicao = np.where(t == letra.upper())[0][0] + 1 
    I.append(posicao)
I = np.array(I).reshape(1, -1) 
for c in range (n//2):
    k=2*c
    par = np.array([[I[0, k]], [I[0, k + 1]]])
    P.append(par)
P = np.hstack(P)
A = np.array([[2, 1],
              [3, 2]])
C=A@P
C=np.mod(C, 26)
r, s = C.shape
for i in range(r):
    for j in range(s):
        if [C[i,j]]==0:
            [C[i,j]]=26
# Transpor a matriz cifrada
C = C.T
TC = np.zeros((1, n), dtype=int)

for c in range(n // 2):
    k = 2 * c
    TC[0, k] = C[c, 0]       
    TC[0, k + 1] = C[c, 1]
cripto = [t[i - 1] for i in TC.flatten()]
print(f"Seu código cifrado é: {''.join(cripto)}")