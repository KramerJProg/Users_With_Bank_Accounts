# class represents a Bank Account that yields 2 separate accounts.
class BankAccount:
    # dunder init takes two params, int_rate = interest rate, 
    # balance = starting balance of funds in an account.
    def __init__(self, int_rate = .1, balance = 30):
        # attributes
        self.int_rate = int_rate
        self.balance = balance

    # deposits the amount of funds into the balance of an account 
    # passed from an instance, through the parameter amount
    def deposit(self, amount):
        self.balance += amount
        return self
    
    # withdraws the amount of funds from the balance of an account 
    # passed from an instance, through the parameter amount as long
    # as the balance is greater than the withdrawl amount. If the
    # balance is less than the desired amount to be taken out, the
    # balance is charged a $5 fee along with a print message.
    def withdraw(self, amount):
        penalty = 5
        if self.balance > amount:
            self.balance -= amount
        else:
            self.balance -= penalty
            print("Insufficient funds: Charging a $5 fee.")
        return self

    # displays the balance of the instance account.
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    # if the balance is positive, the amount of the balance will accumulate
    # the amount of funds in the the user's balance multiplied by the 
    # interest rate. 
    def yield_interest(self):
        if self.balance > 0:
            addedInt = self.balance * self.int_rate
            self.balance += addedInt
        return self

# Instances
account1 = BankAccount()
account2 = BankAccount()

account1.deposit(0).deposit(0).deposit(0).withdraw(50).yield_interest().display_account_info()

account2.deposit(20).deposit(40).withdraw(5).withdraw(7).withdraw(3).withdraw(13).yield_interest().display_account_info()


class User:
    # Passing in 1 params : name 
    def __init__(self, name):
        # 2 attributes that provide a name and Bank Account class.
        self.name = name
        self.account = BankAccount(int_rate = .2, balance = 0)

    # function that passes in 1 argument from the instance that adds funds to the bank account.
    def make_deposit(self):
        self.account.deposit(1000) 
        return self

    # function that passes in 1 argument from the instance that subtracts funds to the bank account.
    def make_withdrawl(self):
        self.account.withdraw(50)
        return self

    # function displays user's current account balance.
    def display_user_balance(self):
        print(f"User: {self.name} , Balance: {self.account.display_account_info()}")

    # function that transfers funds from one user's account to another user's account.
    def transfer_money(self, user):
        self.account.withdraw(10)
        user.account.deposit(15)
        self.account.display_account_info()
        user.account.display_account_info()

# Instances with values passed in. Total of 3.
kramer = User("Kramer")
jessie = User("Jessie")
jason = User("Jason")

kramer.make_deposit().make_deposit().make_deposit().make_withdrawl().transfer_money(jason)

jessie.make_deposit().make_deposit().make_withdrawl().make_withdrawl()

jason.make_deposit().make_withdrawl().make_withdrawl().make_withdrawl()

jessie.display_user_balance()
jason.display_user_balance()