def XOR_AND(R0,Ki,L0):
    x = 0
    
    while x < 2 :
        #AND de R0 com Ki retornando o valor para F
        F = ""
        for i in range(len(R0)):
            F  += str(int(R0[i]) & int(Ki[i]))
        
        #XOR de L0 com F retornando o valor para R0 para a segunda rodada
        R0 = ""
        for i in range(len(L0)):
            R0 += str(int(L0[i]) ^ int(F[i]))
        
        x = x+1
    return R0

R0 = "1100"
Ki = "1001"
L0 = "0110"
resultado_XOR_AND = XOR_AND(R0,Ki,L0)  
print(resultado_XOR_AND)
