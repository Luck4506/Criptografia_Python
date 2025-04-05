import numpy as np
contituar = 'S'
while contituar == 'S':
    escolha = input('[1 = Criptografar/2 = Descriptografar]: ')
    if escolha == '1':
        frase_cripto = list(input('Digite a frase que você quer criptografar: ').strip().upper().replace(" ", ""))
        if len(frase_cripto) % 2 != 0:
            frase_cripto.append(frase_cripto[-1])
        t_cripto = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        frase_cripto = np.array(frase_cripto).reshape(1, -1)
        m_cripto, n_cripto = frase_cripto.shape
        I_cripto = []
        P_cripto = []
        TC_cripto = []
        cripto_result = []
        for letra in frase_cripto.flatten():  
            posicao_cripto = np.where(t_cripto == letra.upper())[0][0] + 1 
            I_cripto.append(posicao_cripto)
        I_cripto = np.array(I_cripto).reshape(1, -1) 
        for c in range(n_cripto // 2):
            k_cripto = 2 * c
            par_cripto = np.array([[I_cripto[0, k_cripto]], [I_cripto[0, k_cripto + 1]]])
            P_cripto.append(par_cripto)
        P_cripto = np.hstack(P_cripto)
        A_cripto = np.array([[2, 1],
                             [3, 2]])
        C_cripto = A_cripto @ P_cripto
        C_cripto = np.mod(C_cripto, 26)
        r_cripto, s_cripto = C_cripto.shape
        for i in range(r_cripto):
            for j in range(s_cripto):
                if C_cripto[i, j] == 0:
                    C_cripto[i, j] = 26
        C_cripto = C_cripto.T
        TC_cripto = np.zeros((1, n_cripto), dtype=int)

        for c in range(n_cripto // 2):
            k_cripto = 2 * c
            TC_cripto[0, k_cripto] = C_cripto[c, 0]       
            TC_cripto[0, k_cripto + 1] = C_cripto[c, 1]
        cripto_result = [t_cripto[i - 1] for i in TC_cripto.flatten()]
        print(f"Seu código criptografado é: {''.join(cripto_result)}")

    elif escolha == '2':
        frase_descripto = list(input('Digite a frase que você quer descriptografar: ').strip().upper())
        frase_descripto = np.array(frase_descripto).reshape(1, -1)
        t_descripto = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        t_inversos_descripto = np.array([[1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25], [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]])
        index_descripto = []
        I_descripto = []
        P_descripto = []
        C_descripto = []
        A_descripto = np.array([[2, 1], [3, 2]])
        det_descripto = A_descripto[0, 0] * A_descripto[1, 1] - A_descripto[0, 1] * A_descripto[1, 0]
        det_descripto = np.mod(det_descripto, 26)
        ind_descripto = np.where(t_inversos_descripto[0] == det_descripto)[0][0]
        inverso_descripto = t_inversos_descripto[1][ind_descripto]
        AI_descripto = inverso_descripto * np.array([[A_descripto[1, 1], -A_descripto[0, 1]], [-A_descripto[1, 0], A_descripto[0, 0]]])
        AI_descripto = np.mod(AI_descripto, 26)
        AI_descripto[AI_descripto == 0] = 26
        m_descripto, n_descripto = frase_descripto.shape
        for letra in frase_descripto.flatten():  
            posicao_descripto = np.where(t_descripto == letra.upper())[0][0] + 1 
            I_descripto.append(posicao_descripto)
        I_descripto = np.array(I_descripto).reshape(1, -1)
        for c in range(n_descripto // 2):
            k_descripto = 2 * c
            par_descripto = np.array([[I_descripto[0, k_descripto]], [I_descripto[0, k_descripto + 1]]])
            C_descripto.append(par_descripto)
        C_descripto = np.hstack(C_descripto)
        P_descripto = AI_descripto @ C_descripto
        P_descripto = np.mod(P_descripto, 26)
        P_descripto[P_descripto == 0] = 26
        r_descripto, s_descripto = P_descripto.shape
        for i in range(r_descripto):
            for j in range(s_descripto):
                if P_descripto[i, j] == 0:
                    P_descripto[i, j] = 26
        P_descripto = P_descripto.T
        TP_descripto = np.zeros((1, n_descripto), dtype=int)
        for c in range(n_descripto // 2):
            k_descripto = 2 * c
            TP_descripto[0, k_descripto] = P_descripto[c, 0]
            TP_descripto[0, k_descripto + 1] = P_descripto[c, 1]
        descripto_result = [t_descripto[i - 1] for i in TP_descripto.flatten()]
        print(f"Seu código descriptografado é: {''.join(descripto_result)}")
