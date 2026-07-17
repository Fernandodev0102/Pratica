

Contas_recorrentes = []


usuario = input("Olá, qual seu nome?: \n")
print("Olá,",usuario)
print("Agora vamos definir suas contas recorrentes")

# Menu inicial
while True:
  print("Para sair deste menu basta digitar 0")
  definicao_recorrentes = input("Qual conta você quer definir agora?:\n")

  if definicao_recorrentes == "0":
    break
# Puxa o nome da conta
  Contas_recorrentes.append(definicao_recorrentes)



#  Definição de conta 
  fixa_ou_variavel = input("O valor desta conta é fixo? \n 1 - Sim \n 2 - Não \n")
  Tipo_fixa = "Conta fixa"
  Tipo_variavel = "Conta variável"
#   Puxa o tipo de conta
  if fixa_ou_variavel == "1" and fixa_ou_variavel != "0":
    Contas_recorrentes.append(Tipo_fixa)

  if fixa_ou_variavel == "2" and fixa_ou_variavel != "0":
    Contas_recorrentes.append(Tipo_variavel)




# Definição de valores
# Puxa o valor da conta
  if fixa_ou_variavel == "1" and fixa_ou_variavel != "0":
    valor_fixo = input("Digite o valor desta conta: \n")
    Contas_recorrentes.append(valor_fixo)

  if fixa_ou_variavel == "2" and fixa_ou_variavel != "0":
    valor_variavel = input("Digite o valor máximo que essa conta pode atingir: \n")
    Contas_recorrentes.append(valor_variavel)
    


# Amostragem de dados
print("|-------------------------------------------------|")
print("Resumo das suas contas recorrentes")
# Organização dos dados
for i in range(0,len(Contas_recorrentes),3):
    Nome_conta = Contas_recorrentes[i]
    Tipo_conta = Contas_recorrentes[i+1]
    Valor_conta = Contas_recorrentes[i+2]
    print(f"Conta: \n {Nome_conta} \n Tipo de conta: {Tipo_conta} \n Valor: R${Valor_conta} \n ----------------------------------")


# Somatório das contas
Soma = 0
for j in range(0,len(Contas_recorrentes),3):
    Valores = float(Contas_recorrentes[j+2])
    Soma += Valores
print(f"O valor total das contas é: R${Soma}")
