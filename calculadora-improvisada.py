def sucessor(A):
    return A + 1

def soma(A, B):
    c = A
    for i in range(B):
        A = sucessor(A)
    return A

def multiplicacao(A, B):
    c = 0
    for i in range(B):
        c = soma(c, A)
    return c

def exponenciacao(A, B):
    c = 1
    for i in range(B):
        c = multiplicacao(c, A)
    return c

while True:
    cmd = input()
    if cmd:
        cmd = cmd.split()
        if cmd[0] == 'Suc':
            print(sucessor(int(cmd[1])))
        elif cmd[0] == 'Soma':
            print(soma(int(cmd[1]), int(cmd[2])))
        elif cmd[0] == 'Mult':
            print(multiplicacao(int(cmd[1]), int(cmd[2])))
        elif cmd[0] == 'Exp':
            print(exponenciacao(int(cmd[1]), int(cmd[2])))
    else:
        break




