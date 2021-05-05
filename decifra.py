letras = list(str(input()))
frase = list(str(input()))
frase_decifrada = []
letra_da_vez = ''
indice = 0
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(frase)):
    letra_da_vez = frase[i]
    indice = alfabeto.index(letra_da_vez)
    frase_decifrada.append(letras[indice])
print("".join(frase_decifrada))










        
            


   
    
    





        





