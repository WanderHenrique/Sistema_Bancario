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


def create_user(name, cpf, email, phone_number):
    users.append({
        "name": name,
        "cpf": cpf,
        "email": email,
        "phone_number": phone_number,
    })


def create_account(user_id, name, number, balance):
    accounts.append({
        "user_id": user_id,
        "name": name,
        "number": number,
        "balance": balance,
    })


accounts = []
users = []


while True:
    print("Bem-vindo ao seu sistema bancário!")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Visualizar extrato")
    print("4. Criar usuário")
    print("5. Criar conta corrente")
    print("6. Sair")

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
        name = input("Digite o nome do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        email = input("Digite o e-mail do usuário: ")
        phone_number = input("Digite o número de telefone do usuário: ")
        create_user(name, cpf, email, phone_number)
        print("Usuário criado com sucesso.")

    elif choice == "5":
        user_id = input("Digite o ID do usuário: ")
        name = input("Digite o nome da conta: ")
        number = input("Digite o número da conta: ")
        balance = float(input("Digite o saldo inicial: "))
        create_account(user_id, name, number, balance)
        print("Conta criada com sucesso.")

    elif choice == "6":
        print("Obrigado por usar nosso sistema bancário!")
        sys.exit(0)
