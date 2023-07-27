
import sys
import time


class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Saldo insuficiente.")
            sys.exit(1)
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_statement(self):
        statement = []
        statement.append("Nome: {} Número: {}".format(self.name, self.number))
        statement.append("Saldo: {}".format(self.balance))
        return statement

# Criar uma lista de contas bancárias
accounts = [
    Account("João da Silva", 123456789, 1000),
    Account("Maria da Silva", 987654321, 2000),
]

# Criar um menu para o usuário
while True:
    print("Bem-vindo ao seu sistema bancário!")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Visualizar extrato")
    print("4. Sair")

    choice = input("Qual é a sua escolha? ")

    if choice == "1":
        account_number = input("Digite o número da conta: ")
        amount = float(input("Digite o valor a ser sacado: "))
        accounts[account_number - 1].withdraw(amount)
        print("Saque realizado com sucesso.")

    elif choice == "2":
        account_number = input("Digite o número da conta: ")
        amount = float(input("Digite o valor a ser depositado: "))
        accounts[account_number - 1].deposit(amount)
        print("Depósito realizado com sucesso.")

    elif choice == "3":
        account_number = input("Digite o número da conta: ")
        for statement in accounts[account_number - 1].get_statement():
            print(statement)

    elif choice == "4":
        print("Obrigado por usar nosso sistema bancário!")
        sys.exit(0)
