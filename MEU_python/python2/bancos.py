from contas import Conta, ContaPoupanca, ContaFuncionario


class Banco():
    """
    Classe Banco
    """

    def __init__(self):
        """
        Construtor da classe Banco
        :param contas: lista de contas cadastradas no sistema
        ja são criadas 4 contas padrão para fazer algumas operações
        """
        c1 = Conta(numero=1, senha=123, titular="João", saldoi=500)
        c2 = Conta(numero=2, senha=456, titular="Maria", saldoi=250)
        c3 = Conta(numero=3, senha=789, titular="José", saldoi=10000)
        c4 = Conta(numero=4, senha=000, titular="Pedro", saldoi=0)
        self._contas = [c1, c2, c3, c4]
        
        c5 = ContaFuncionario(numero=1, senha=123, titular="Ademiro", funcao="Gerente")
        c6 = ContaFuncionario(numero=2, senha=456, titular="Mano TI", funcao="Tecnico de Rede")
        self._contasFuncionarios = [c5, c6]
        
        c7 = ContaPoupanca(numero=1, senha=789, titular="Jeremias", saldoi=10000, taxa=0.005)
        c8 = ContaPoupanca(numero=2, senha=000, titular="Paulo II", saldoi=605, taxa=0.002)
        self._contasPoupanca = [c7, c8]
        

    def atendimento_blank(self):
        """
        Atendimento feito ao iniciar o sistema
        Será escolhido pelo usuário o tipo de conta a ser utilizada
        """
        print("Bem vindo ao sistema de atendimento do banco")
        mod = int(input(
            "Qual o modelo da sua conta? (1 - Conta Corrente, 2 - Conta Poupança, 3 - Funcionário): "))
        if mod == 1:
            self.atendimento_cc()

        elif mod == 2:
            self.atendimento_po()

        elif mod == 3:
            self.atendimento_fu()

        else:
            print("Modelo de conta não encontrado.")
            print("Finalizando operação...")

    def atendimento_cc(self):
        """
        Atendimento para usuários de Conta Corrente
        """
        tipo = "cc"
        num = int(input("Digite o numero da sua conta: "))
        if self.confere_num_conta(num, tipo) is not False:
            index = self.confere_num_conta(num, tipo)
            # É o indice da conta na lista de contas cadastradas no sistema do banco
            sen = int(input("Digite a senha da sua conta: "))
            if self._contas[index].valida_senha_conta(sen):
                # É executado um método dentro da classe Conta
                while (True):
                    op = int(input(
                        "Qual operacao deseja realizar? (1 - Saque, 2 - Deposito, 3 - Ver Saldo, 4 - Transferencia, 5 - Sair): "))
                    if op == 1:
                        valor = float(input("Digite o valor do saque: R$"))
                        self._contas[index].saque(sen, valor, op)

                    elif op == 2:
                        valor = float(input("Digite o valor do deposito: R$"))
                        self._contas[index].deposito(valor)

                    elif op == 3:
                        print(
                            f"O seu saldo é de R${self._contas[index].getSaldo(sen)}")

                    elif op == 4:
                        num1 = int(
                            input("Digite o numero da conta do beneficiario: "))
                        if self.confere_num_conta(num1, tipo) is not False:
                            index1 = self.confere_num_conta(num1, tipo)
                            # É conferido se existe uma conta com o numero do beneficiario
                            # Em seguida ja é atribuído o indice da conta dele na lista de contas do banco a uma variavel
                            self._contas[index1].exibeDadosBeneficiarioTransferencia()
                            op1 = int(input("É esse o beneficiario da transferencia? (1 - Sim, 2 - Não): "))
                            if op1 == 1:
                                valor = float(
                                    input("Digite o valor da transferencia: R$"))
                                self._contas[index].saque(sen, valor, op)
                                self._contas[index1].deposito(valor)
                            else:
                                print("Operação encerrada")
                        else:
                            print("Conta não encontrada")

                    elif op == 5:
                        break
            else:
                print("Senha inválida")
        else:
            print("Conta não encontrada")

    def atendimento_po(self):
        """
        Atendimento para usuários de Conta Poupança
        """
        tipo = "po"
        num = int(input("Digite o numero da sua conta: "))
        if self.confere_num_conta(num, tipo) is not False:
            index = self.confere_num_conta(num, tipo)
            # É o indice da conta na lista de contas cadastradas no sistema do banco
            sen = int(input("Digite a senha da sua conta: "))
            if self._contas[index].valida_senha_conta(sen):
                # É executado um método dentro da classe Conta
                while (True):
                    op = int(input(
                        "Qual operacao deseja realizar? (1 - Saque, 2 - Deposito, 3 - Ver Saldo, 4 - Transferencia, 5 - Sair): "))
                    if op == 1:
                        # haha
                        a = 3

                    elif op == 2:
                        # haha
                        a = 4

                    elif op == 3:
                        # haha
                        a = 4

                    elif op == 4:
                        # haha
                        a = 4

                    elif op == 5:
                        break
            else:
                print("Senha inválida")
        else:
            print("Conta não encontrada")

    def atendimento_fu(self):
        """
        Atendimento para usuários de Conta Funcionário do Banco
        """
        tipo = "fu"
        num = int(input("Digite o numero da sua conta: "))
        if self.confere_num_conta(num, tipo) is not False:
            index = self.confere_num_conta(num, tipo)
            # É o indice da conta na lista de contas cadastradas no sistema do banco
            sen = int(input("Digite a senha da sua conta: "))
            if self._contasFuncionarios[index].valida_senha_conta(sen):
                # É executado um método dentro da classe Conta
                while (True):
                    op = int(input(
                        "Qual operacao deseja realizar? (1 - Mudar senha de um cliente, 2 - Cadastrar uma nova conta, 3 - Ver Info. de um cliente, 4 - Sair): "))
                    if op == 1:
                        if self._contasFuncionarios[index].funcao is not "Gerente":
                            print("Sua conta nao tem permissao de realizar esta operacao...")
                        else:
                            tipo1 = int(input("Qual tipo de conta tera sua senha alterada? (1 - Conta Corrente, 2 - Conta Poupanca, 3 - Conta de funcionario): "))
                            if tipo1 == 1 or tipo1 == 2 or tipo1 == 3:
                                if tipo1 == 1:
                                    tipo1 = "cc"
                                elif tipo1 == 2:
                                    tipo1 = "po"
                                elif tipo1 == 3:
                                    tipo1 = "fu"
                                num1 = int(
                                input("Digite o numero da conta que tera a senha alterada: "))
                                if self.confere_num_conta(num1, tipo1) is not False:
                                    index1 = self.confere_num_conta(num1, tipo1)
                                    # É conferido se existe uma conta com o numero do beneficiario
                                    # Em seguida ja é atribuído o indice da conta dele na lista de contas do banco a uma variavel
                                    sen1 = int(
                                        input("Digite a nova senha do usuario: "))
                                    if tipo1 == "cc":
                                        self._contas[index1].setSenha(sen1)
                                        print()
                                    elif tipo1 == "po":
                                        self._contasPoupanca[index1].setSenha(sen1)
                                    elif tipo1 == "fu":
                                        self._contasFuncionarios[index1].setSenha(sen1)
                                else:
                                    print("Conta não encontrada")
                            else:
                                print("Tipo de conta invalido...")
                            
                    elif op == 2:
                        tipo1 = int(input("Qual tipo de conta sera criada? (1 - Conta Corrente, 2 - Conta Poupanca, 3 - Conta de funcionario): "))
                        if tipo1 == 1 or tipo1 == 2:
                            if tipo1 == 1:
                                tipo1 = "cc"
                            elif tipo1 == 2:
                                tipo1 = "po"
                            num1 = int(
                                input("Digite o numero da nova conta: "))
                            while(True):
                                if self.confere_num_conta(num1, tipo1) is not False:
                                    # Se ja existe uma conta com esse numero:
                                    print("Esse numero de conta ja esta em uso...")
                                    num1 = int(input("Tente novamente:"))
                                else:
                                    break
                            sen1 = int(input("Digite a senha da nova conta, use apenas numeros: "))
                            titu1 = input("Digite o nome do titular: ")
                            sald1 = float(input("Digite o saldo da nova conta: R$"))
                            tax1 = 0.0
                            func1 = "0"
                            if tipo1 == "po":
                                tax1 = float(input("Digite a taxa de rendimento da nova conta: "))
                            self.cria_nova_conta(num=num1, tit=titu1, sen=sen1, tax=tax1, sald=sald1, tipo=tipo1, func=func1)
                        elif tipo1 == 3:
                            if self._contasFuncionarios[index].funcao is not "Gerente":
                                print("Sua conta nao tem permissao de realizar esta operacao...")
                            else:
                                tipo1 = "fu"
                                num1 = int(
                                input("Digite o numero da nova conta: "))
                                while(True):
                                    if self.confere_num_conta(num1, tipo1) is not False:
                                        # Se ja existe uma conta com esse numero:
                                        print("Esse numero de conta ja esta em uso...")
                                        num1 = int(input("Tente novamente:"))
                                    else:
                                        break
                                sen1 = int(input("Digite a senha da nova conta, use apenas numeros: "))
                                titu1 = input("Digite o nome do funcionario: ")
                                func1 = input("Digite a funcao do novo funcionario: ")
                                tax1=0
                                sald1=0
                                self.cria_nova_conta(num=num1, tit=titu1, sen=sen1, tax=tax1, sald=sald1, tipo=tipo1, func=func1)
                        else:
                            print("Tipo de conta invalido...")

                    elif op == 3:
                        # haha
                        a = 4

                    elif op == 4:
                        break
            else:
                print("Senha inválida")
        else:
            print("Conta não encontrada")

    def confere_num_conta(self, numero, tipo):
        """
        Confere se existe alguma conta no sistema com este número
        mas antes confere o tipo de conta para ver as listas
        """
        if tipo == "cc":
            #Confere o tipo de conta sendo buscado, vendo qual lista de contas será consultada
            for i in range(0, len(self._contas)):
                if self._contas[i].numero == numero:
                    return i
                    # É retornado o ídice da conta dentro da lista de contas do sistema
                    # Isso facilita o futuro manuseio da conta pelo sistema
        elif tipo == "po":
            for i in range(0, len(self._contasPoupanca)):
                if self._contasPoupanca[i].numero == numero:
                    return i
                    # É retornado o ídice da conta dentro da lista de contas do sistema
                    # Isso facilita o futuro manuseio da conta pelo sistema
        elif tipo == "fu":
            for i in range(0, len(self._contasFuncionarios)):
                if self._contasFuncionarios[i].numero == numero:
                    return i
                    # É retornado o ídice da conta dentro da lista de contas do sistema
                    # Isso facilita o futuro manuseio da conta pelo sistema
        return False
    
    def cria_nova_conta(self, num, tit, sen, tax, sald, func, tipo):
        if tipo == "cc":
            c9 = Conta(numero=num, senha=sen, titular=tit, saldoi=sald)
            self._contas.append(c9)
        elif tipo == "po":
            c9 = ContaPoupanca(numero=num, senha=sen, titular=tit, saldoi=sald, taxa=tax)
            self._contasPoupanca.append(c9)
        elif tipo == "fu":
            c9 = ContaFuncionario(numero=num, senha=sen, titular=tit, funcao=func)
            self._contasFuncionarios.append(c9)
        print("Nova conta cadastrada com sucesso!")
