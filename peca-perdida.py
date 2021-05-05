N = int(input('Digite o numero de peças: '))
pecas = {int(pecas) for pecas in input().split()}
pecas_totais = set(range(1, N+1))
peca_perdida = pecas_totais ^ pecas
print(peca_perdida)



   
    
    





        





