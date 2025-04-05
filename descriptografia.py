import numpy as np
frase_cifrada = list(input('Digite a frase que você quer criptografar: ').strip().upper())
frase_cifrada = np.array(frase_cifrada).reshape(1, -1)
t = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
t_inversos = np.array([[1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25], [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]])
index = []
I = []
P = []
C = []
A = np.array([[2, 1], [3, 2]])
det = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
det = np.mod(det, 26)
ind = np.where(t_inversos[0] == det)[0][0]
inverso = t_inversos[1][ind]
AI = inverso * np.array([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]])
AI = np.mod(AI, 26)
AI[AI == 0] = 26
m, n = frase_cifrada.shape
for letra in frase_cifrada.flatten():  
    posicao = np.where(t == letra.upper())[0][0] + 1 
    I.append(posicao)
I = np.array(I).reshape(1, -1)
for c in range(n // 2):
    k = 2 * c
    par = np.array([[I[0, k]], [I[0, k + 1]]])
    C.append(par)
C = np.hstack(C)
P = AI @ C
P = np.mod(P, 26)
P = np.mod(P, 26)
P[P == 0] = 26
r, s = P.shape
for i in range(r):
    for j in range(s):
        if P[i, j] == 0:
            P[i, j] = 26
TP = np.zeros((1, n), dtype=int)
for c in range(n // 2):
    k = 2 * c
    TP[0, k] = P[0, c]
    TP[0, k + 1] = P[1, c]
descripto = [t[i - 1] for i in TP.flatten()]
print(f"Seu código cifrado é: {''.join(descripto)}")
