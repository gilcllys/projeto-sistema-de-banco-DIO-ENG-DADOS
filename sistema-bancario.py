class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}'

class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Saque de R${valor:.2f} realizado com sucesso!')
            else:
                print('Saldo insuficiente.')
        else:
            print('O valor do saque deve ser positivo.')

    def consultar_saldo(self):
        print(f'Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}')

    def __str__(self):
        return f'Conta: {self.numero_conta}\nTitular: {self.titular.nome}\nSaldo: R${self.saldo:.2f}'

class SistemaBancario:
    def __init__(self):
        self.contas = {}
        self.usuarios = {}

    def criar_usuario(self, nome, cpf):
        if cpf not in self.usuarios:
            self.usuarios[cpf] = Usuario(nome, cpf)
            print(f'Usuário {nome} criado com sucesso!')
        else:
            print('Usuário com este CPF já existe.')

    def listar_usuarios(self):
        if not self.usuarios:
            print('Nenhum usuário cadastrado.')
        else:
            for usuario in self.usuarios.values():
                print(usuario)

    def filtrar_usuarios(self, nome=None, cpf=None):
        encontrados = []
        for usuario in self.usuarios.values():
            if (nome and nome.lower() in usuario.nome.lower()) or (cpf and cpf == usuario.cpf):
                encontrados.append(usuario)
        
        if not encontrados:
            print('Nenhum usuário encontrado.')
        else:
            for usuario in encontrados:
                print(usuario)

    def criar_conta(self, numero_conta, cpf, saldo=0):
        if cpf in self.usuarios:
            if numero_conta not in self.contas:
                self.contas[numero_conta] = ContaBancaria(numero_conta, self.usuarios[cpf], saldo)
                print('Conta criada com sucesso!')
            else:
                print('Número da conta já existe.')
        else:
            print('Usuário não encontrado.')

    def depositar(self, numero_conta, valor):
        if numero_conta in self.contas:
            self.contas[numero_conta].depositar(valor)
        else:
            print('Conta não encontrada.')

    def sacar(self, numero_conta, valor):
        if numero_conta in self.contas:
            self.contas[numero_conta].sacar(valor)
        else:
            print('Conta não encontrada.')

    def consultar_saldo(self, numero_conta):
        if numero_conta in self.contas:
            self.contas[numero_conta].consultar_saldo()
        else:
            print('Conta não encontrada.')

def main():
    sistema = SistemaBancario()
    
    while True:
        print('\nSistema Bancário')
        print('1. Criar Usuário')
        print('2. Listar Usuários')
        print('3. Filtrar Usuários')
        print('4. Criar Conta')
        print('5. Depositar')
        print('6. Sacar')
        print('7. Consultar Saldo')
        print('8. Sair')
        
        escolha = input('Escolha uma opção: ')
        
        if escolha == '1':
            nome = input('Nome do usuário: ')
            cpf = input('CPF do usuário: ')
            sistema.criar_usuario(nome, cpf)
        
        elif escolha == '2':
            sistema.listar_usuarios()
        
        elif escolha == '3':
            nome = input('Nome do usuário (opcional): ')
            cpf = input('CPF do usuário (opcional): ')
            sistema.filtrar_usuarios(nome, cpf)
        
        elif escolha == '4':
            numero_conta = input('Número da conta: ')
            cpf = input('CPF do titular: ')
            saldo = float(input('Saldo inicial (opcional, 0 por padrão): ') or 0)
            sistema.criar_conta(numero_conta, cpf, saldo)
        
        elif escolha == '5':
            numero_conta = input('Número da conta: ')
            valor = float(input('Valor do depósito: '))
            sistema.depositar(numero_conta, valor)
        
        elif escolha == '6':
            numero_conta = input('Número da conta: ')
            valor = float(input('Valor do saque: '))
            sistema.sacar(numero_conta, valor)
        
        elif escolha == '7':
            numero_conta = input('Número da conta: ')
            sistema.consultar_saldo(numero_conta)
        
        elif escolha == '8':
            print('Saindo do sistema.')
            break
        
        else:
            print('Opção inválida.')

if __name__ == "__main__":
    main()
