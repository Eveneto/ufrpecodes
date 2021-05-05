numPessoas = int(input())
tempo1 = 0
tempo2 = 0
diff = 0
tempoLigado = 0

for i in range(numPessoas):
    tempoPassagem = int(input())
    if numPessoas == 1:
        print(10)
    else:
        if i == 0 or i % 2 == 0:
            tempo1 = tempoPassagem
        else:
            tempo2 = tempoPassagem
        if tempo2 != 0:
            if(tempo1 > tempo2):
                diff = tempo1 - tempo2
            else:
                diff = tempo2 - tempo1
            if diff >= 10:
                tempoLigado += 10
            else: 
                tempoLigado += diff
print(tempoLigado + 10)


        





