class BankAccount:
    def __init__(self, account_holder,balance):
        self.account_holder = account_holder
        self.balance= balance
        self.is_active=True
    def deposit(self, amount):
        if self.is_active:
            self.balance+=amount
            print(f"se ha depositado {amount}. saldo actual: {self.balance}")
        else: 
            print("no se puede dpositar, cuenta inactiva")
    def withdraw(self,amount):
        if self.is_active:
            if amount<= self.balance:
                self.balance -=amount
                print(f"se ha retirado {amount}. saldo actual: {self.balance}")
            else:
                print("fondos insuficiente")
        else:
            print("no se puede retirar, cuenta inactiva")
    def deactive(self):
        self.is_active= False
        print("la cuenta ha sido desactivada")
    def active (self):
        self.is_active=True
        print("la cuenta ha sido activada")
    #crear objetos de la clase BankAccount
cuenta1=BankAccount("jose",500)
cuenta2=BankAccount("maria",1000)
cuenta1.deposit(500)
cuenta2.withdraw(100)
cuenta1.deactive()
cuenta1.deposit(200)
cuenta1.active()
cuenta1.deposit(200)
