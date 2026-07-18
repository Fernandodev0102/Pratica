# Consultar saldo
# Nova movimentação
# Conferir extrato
# Consciliar saldo com o sistema

Saldo_inicial = float(input("Digite o saldo inicial: \n"))
Movimentacao = 0
Saldo_atual = Saldo_inicial





def Calculo_Saldo(x):
    Movimentacao = float(input("Digite o valor da movimentação: \n"))
    if x == 1:
        Saldo_atual = Saldo_inicial + Movimentacao
        return Saldo_atual
        print(f"Seu saldo atual é:{Saldo_atual}")
    if x ==2:
        Saldo_atual = Saldo_inicial - Movimentacao
        return Saldo_atual
        print(f"Seu saldo atual é:{Saldo_atual}")
        






Menu = 0

while Menu != 5:
    print("Escolha uma opção: \n")
    print("1- Consultar saldo \n2- Registrar movimentação \n3- Conferir extrato \n4- Consciliação de valores \n5- Sair")
    Menu = int(input("Digite sua resposta: \n"))

# ---------------------------------------------------------




    if Menu == 1:
        print(f"Seu saldo atual é:{Saldo_atual} ")
    if Menu == 2:
        Operacao = int(input("Selecione a opção desejada: \n1- Registrar ganho \n2- Registrar gasto \n"))
        Saldo_atual =   Calculo_Saldo(Operacao)




    if Menu == 3:
        print("Extrato")




    if Menu == 4:
        print("Consciliação")

