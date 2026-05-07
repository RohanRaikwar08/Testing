class Account:

    def __init__(self):
        self.__number = None
        self.__account_type = None
        self.__balance = 0.0


    def get_number(self):
        return self.__number

    def set_number(self,number):
        self.__number = number

    def get_account_type(self):
        return self.__account_type

    def set_account_type(self,account_type):
        self.__account_type = account_type

    def get_balance(self):
        return self.__balance

    def set_balance(self,balance):
        self.__balance = balance


acc = Account()
acc.set_number("12345")
acc.set_account_type("saving")
acc.set_balance(1000)
print("Account Number:",acc.get_number())
print("Account Type:",acc.get_account_type())
print("Balance:",acc.get_balance())


