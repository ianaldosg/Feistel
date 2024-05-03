def XOR_AND(L0,Ki,R0):

    #AND de R0 com Ki retornando o valor para F
    F = ""
    for i in range(len(R0)):
        F  += str(int(R0[i]) & int(Ki[i]))
        
    #XOR de L0 com F retornando o valor para R0 para a segunda rodada
    R1 = ""
    for i in range(len(L0)):
        R1 += str(int(L0[i]) ^ int(F[i]))
        
    return R1

def gerador_de_subchave(R):
    Ki = R[1:] + R[0]
    return Ki

#Primeira vez

R0 = "1100"
L0 = "0110"
Ki = gerador_de_subchave(R0)


L2 = XOR_AND(L0,Ki,R0)
Ki1 = gerador_de_subchave(L2)
R2 = XOR_AND(R0,Ki1,L2)
print(L2 + R2)