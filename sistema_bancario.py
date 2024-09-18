#atribuição variável menu
def menu(): 
    menu = """
Escolha umas das opções do menu a seguir: 

========= Menu =========

[0] Depositar
[1] Sacar
[2] Extrato
[3] Cadastrar Novo Usuário
[4] Criar Conta Corrente 
[5] Sair 

=========================

=> """
    return input(menu)


#função para plural da palavra real
def gramatica_real(valor):

    if valor == 1:
        return (" real.")
    else:
        return(" reais.")


#função depositar, position only
def depositar(saldo, valor, extrato,/):
    
    #valida valor de deposito  
    if valor >0:      
        saldo += valor #incrementa saldo
        extrato += f"\nDepósito: R${valor: .2f} {gramatica_real(valor)}" #incrementa extrato
        print("Operação concluída com sucesso!")
            
    #barra depositos de valores menores que zero
    else:
        print("Valor inválido. Operação não concluída")

    return saldo, extrato

#função sacar keyword only
def sacar(*,saldo, valor, extrato, limite_por_saque, numero_de_saques, limite_saques_diario):
    
    excedeu_saldo = valor > saldo #atribui regra de validação para a variável excedeu_saldo
    excedeu_limite = valor > limite_por_saque  #atribui regra de validação para a variável excedeu_limite
    excedeu_limite_saques = numero_de_saques >= limite_saques_diario #atribui regra de validação para a variável excedeu_limite_saques

    if excedeu_saldo: #condicional para a condição excedeu saldo verdadeira  
        print("\nOperação falhou. Você não tem saldo suficiente.")
            
    elif excedeu_limite:  #condicional para a condição excedeu limite verdadeira
        print("\nOperação falhou. Valor solicitado é superior ao valor máximo de saque permitido para sua conta.")

    #condicional para a condição excedeu limite saques
    elif excedeu_limite_saques:
        print("\nOperação não concluída. Você excedeu o limite de saques diários.")
    
    elif valor>0:  #validar valor do saque
                
        saldo -= valor #atualiza valor do saldo (debitando)
        extrato += f"\nSaque: R${valor:.2f} {gramatica_real(valor)}" #atualiza extrato, saque com 02 cadas decimais e chama função para a palavra real
        numero_de_saques +=1 #contabiliza número de saques
        print("Operação concluída com sucesso. Retire o dinheiro na boca do caixa eletrônico.")     
        
    #retorno para o não atendimento de nenhuma das condições acima
    else:
        print("Operação falhou. Valor solicitado inválido.")
    
    return saldo, extrato


#função visualizar extrato com argumentos positional only e keyword only
def exibir_extrato(saldo,/,*,extrato):
     
    print(" \n============ EXTRATO ============ ")
    print("Não foram realizadas movimentações." if not extrato else extrato) 
    print(f"\nSaldo: R${saldo:.2f}{gramatica_real(valor=saldo)}")
    print("=================================")


#função cadastrar novo usuário
def cadastar_novo_usuario(usuarios):
    
    #atribui a variavel cpf o valor inserido por usuário
    cpf = input("Digite o cpf (apenas número): ")
    
    #atribuição da variável com o retorno de função
    usuario_verificado = verificar_existencia_usuario(cpf, usuarios)
    
    #verifica se a variável tem valor atribuído, imprime valor e volta ao fluxo da função main 
    if usuario_verificado:
        print("Usuário já cadastrado!")
        
        return
    
    #solicita dados do usuário ainda não cadastrado
    data_nascimento = input("Informe data de nascimento(dd/mm/aaaa): ")
    nome = input("Informe nome completo: ")
    endereco = input("Informe endereço ('logradouro, n. - bairro - cidade/sigla estado'): ")
    
    #adiciona a lista de usuários valor/chave (dicionário) respectivo ao usuário
    usuarios.append({"cpf": cpf,"data_nascimento":data_nascimento, "nome":nome,"endereco":endereco})
    
    print("\nCadastro realizado com sucesso!")

#função para verificar se o cpf já está cadastrado
def verificar_existencia_usuario( cpf, usuarios):
    
    #
    verificar_existencia_usuario = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    
    #retorna o primeiro cpf (e o único) caso a lista tenham conteúdo, e retorna none se a lista estiver vazia
    return verificar_existencia_usuario[0] if verificar_existencia_usuario else None

#função criar conta corrente e vincula a usuário
def criar_conta_corrente(AGENCIA, usuarios, numero_conta):

    #atribui input à variável cpf
    cpf = input("Digite o cpf (apenas número): ")
    
    #verifica se o cpf está na lista de usuários existentes e retorna o cpf
    usuario_verificado = verificar_existencia_usuario(cpf, usuarios)

    #condicional para a criação de cc para usuário já com cadastro
    if usuario_verificado: 
        print(f"""Conta corrente criada com sucesso!
        \n
    === Dados da conta ===
        ID Usuário: {cpf}  
        Agência: {AGENCIA}
        cc: {numero_conta}
                    """)
        return {"gencia":AGENCIA, "numero_conta":numero_conta, "usuario":cpf}

    #imprimi aviso 
    print("Usuário não encontrado, não foi possível concluir abertura de conta")
    return

def main():

#atribuição de variáveis e constante
    saldo = 0
    limite_por_saque = 500
    extrato = " "
    numero_de_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES_DIARIO = 3
    AGENCIA = "0001"

#inicia loop 
    while True:
        #atribui à variável opção o valor inputado em menu
        opcao = int(menu())
        
        #define condicional para depósito e chama função
        if opcao == 0: 
            #converte 'valor' para float 
            valor = float(input("Digite o valor que deseja depositar. Operação permitida apenas com cédula.\n=> "))

            saldo, extrato = depositar(saldo, valor, extrato)      

        elif opcao == 1:  #define condicional para saque
            
            #converte 'valor' para float 
            valor = float(input("Informe o valor do saque: "))        
           
           #funçao sacar recebe argumento keyword retornando saldo e extrato 
            saldo, extrato = sacar (
                 saldo= saldo,
                 valor = valor,
                 extrato = extrato,
                 limite_por_saque = limite_por_saque,
                 numero_de_saques = numero_de_saques,
                 limite_saques_diario = LIMITE_SAQUES_DIARIO,
        
            )


        #condicional para extrato e chama função 
        elif opcao == 2:
             exibir_extrato(saldo, extrato=extrato)

        #condicional para cadastrar novo usuário e chama função 
        elif opcao == 3:
             cadastar_novo_usuario(usuarios)
        
        #condicional para criar conta corrente e chama função    
        elif opcao == 4:
            
            #itera o número da conta 
            numero_conta= len(contas)+1
           
            #atribui a variável o retorno da função 
            novo_cadastro_cc =[criar_conta_corrente(AGENCIA, usuarios, numero_conta)]

            #condicional para a variável 
            if novo_cadastro_cc:
                #Adição dos dados do usuário(cpf) à lista de conta corrente
                contas.append(novo_cadastro_cc)            
 

        #condicional para sair da aplicação
        elif opcao == 5 :
            break

        #condição para o não atendimento a todas as condicionais anteriores
        else:
            print("\nOperação inválida, por favor selecionar novamente a operação desejada.\n=> ")




main()

