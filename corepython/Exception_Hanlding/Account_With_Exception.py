


class InsufficientFundException(Exception):
    def __inti__(self,msg):
        super().__init__(msg)


class Account:
    def __int__(self):
        self.balance = 0
        self.count = 0

    def get_balance(self):
        return self.balance

    def set_balance(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"deposited: {amount},current balance:{self.balance}")

    def withdrawal(self,amount):
        if amount < 2000:
            raise InsufficientFundException("you cannot Withdraw more than ₹2000 in a single transaction.")

        if self.count >= 2:
            raise InsufficientFundException("Withdrawal limit exceeded. Maximum 3 withdrawals allowed.")

        if self.balance - amount >= 2000:
            self.balance -= amount
            self.count += 1
            print(f"withdraw: {amount},Remaining balance: {self.balance}")

        else:
            raise InsufficientFundException("Insufficient Balance,minimum ₹2000 must remain in the account.")


acc = Account()
acc.set_balance(50000)
print(acc.get_balance())



try:
    acc.deposit(1000)
    acc.withdrawal(500)
    acc.withdrawal(2000)
    acc.withdrawal(20000)


except InsufficientFundException as e:
    print("exception", e)








