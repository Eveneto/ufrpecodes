contador = 0
def f(n):
    global contador
    contador +=1 
    if n == 1:
        return 1
    elif n % 2 == 0:
        return f(n / 2)
    else:
        return f(3 * n + 1)
entrada = int(input())
maiorvalor = 0
for i in range(entrada):
    A, B = [int(x) for x in input().split()]
    for n in range(A, B):
        f(n)
        if contador > maiorvalor:
            maiorvalor = contador
            contador = -1
    print('Caso {}: {}'.format(i+1, maiorvalor))
#código incompleto






        
            


   
    
    





        





