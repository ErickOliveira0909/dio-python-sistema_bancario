import textwrap

def menu():
    menu = """\n
    ==================== MENU ====================
    [ d ]\tDepositar
    [ s ]\tSacar
    [ e ]\tExtrato
    [ nc ]\tNova conta
    [ lc ]\tListar contas
    [ nu ]\tNovo Usuário
    [ q ]\tSair
    => """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R${valor: .2f}\n"
    else:
        print("\n@@@ Erro ao efetuar a operação! O valor informado é inválido. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques == limite_saques:
        print("\n@@@ Operação falhou! O limite de saques foi alcançado 3/3")
    elif saldo == 0:
        print("\n@@@ Operação falhou! Saldo insuficiente")
    
    elif valor <= saldo:
        if valor <= 500:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor: .2f}\n"
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido")
    return saldo, extrato
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuarios for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usúario coom esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (lograduoro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco":endereco})
    print("======== Usúario criado com sucesso! ========")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usúario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n======== Conta criada com sucesso! ========")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    print("\n@@@ Usúario não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
        Agência: {conta["agencia"]}
        C/C:     {conta["numero_conta"]}
        Titular: {conta["usuario"]["nome"]}
        '''
        print("="*100)
        print(textwrap.dedent(linha))
def exibir_extrato(saldo, /, *, extrato):
    print("\n==================== EXTRATO ====================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    
    else:
        print(extrato)
        print(f"\nSaldo: {saldo: .2f}")
        print("================================================")



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"


    saldo = 0
    extrato = ""
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
            print(saldo,extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                valor=valor,
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
                numero_saques=numero_saques
            )

        elif opcao == "e":
           exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Opção inválida! Tente novamente.")


main()