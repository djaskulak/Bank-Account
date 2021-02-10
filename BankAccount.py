""" CS 1.1 Bank Account """
""" by Danika Jaskulak-Gonzalez """

# define bank account class
""" methods needed: 
    * deposit(balance and amount)
    * withdraw(balance and amount)
    * get_balance(print and return)
    * add_interest(interest = balance *  0.00083)
    * print_receipt(name, account number, routing number, balance)
"""

# Import random to make random account numbers
from random import randint

####### Make Random Account Numbers #######
def AccountNum():
        account_num = ""
        for i in range(8):
            account_num +=str(randint(0,9))
        return int(account_num)

####### Make Random Routing Number #######
def RoutNum():
        routing_num = ""
        for i in range(8):
            routing_num +=str(randint(0,9))
        return int(routing_num)

####### Bank Account class #######
class BankAccount:

  # initializing details of account
  def __init__(self, name, account_num, routing_num, balance):
    self.name = name;

    self.account_num = account_num;
    self.routing_num = routing_num;

    self.balance = 0.0;

  # method for depositing money into the account
  def deposit(self, amount):
    # adding amount to the balance
    self.balance = self.balance + amount;
    # print statement updating the balance
    print(f"The amount of ${amount} was deposited into your account. Your new balance is ${self.balance}.");

  # method for withdrawing money from the account
  def withdraw(self, amount):

    # make sure amount is less than the balance
    if self.balance < amount:
      print(f"Unable to complete request due to insufficient funds. Account balance: ${self.balance}");
    else:
      self.balance = self.balance - amount;
      print(f"The amount ${amount} was withdrawn from your account. Your new balance is ${self.balance}");

  # method for getting the balance of the account, must return current balance
  def get_balance(self, balance):
    # storing the balance into a variable that will be returned
    balance = self.balance;
    print(f"Your account has a current balance of ${balance}");
    return balance;

  # method for adding monthly interest to the account
  def add_interest(self, balance):
    #rounding the balance after interest
    self.balance = round(self.balance * 1.00083, 2)
    print(f"After interest, your balance is {self.balance}.")

  # method for printing a receipt with everything
  def print_receipt(self):
    name = self.name
    balance = self.balance
    account_number = self.account_number

    # we need the account number to be a list 
    account_number = [int(x) for x in str(self.account_number)] 

    # making the account number only show up as the last 4 digits
    for i in range(4):
        account_number[i] ="*"

    # combining what's left of the account number with the stars
    account_number = ''.join([str(elem) for elem in account_number])

    print(f"Your Receipt: {name}")
    print(f"Account Number: {account_number}, {balance}")
    print(f"Balance: {balance}")
####### End of Bank Account class ####### 

####### Start of 3 Accounts #######

# Dua Lipa
Dua_Lipa = BankAccount("Dua Lipa", AccountNum(), RoutNum(), 5000000) 
Dua_Lipa.withdraw(500)
Dua_Lipa.deposit(250)
Dua_Lipa.get_balance(1)
Dua_Lipa.add_interest(1)
Dua_Lipa.print_receipt()

# Emma Watson
Emma_Watson = BankAccount("Emma Watson", AccountNum(), RoutNum(), 5000000) 
Emma_Watson.withdraw(500)
Emma_Watson.deposit(250)
Emma_Watson.get_balance(1)
Emma_Watson.add_interest(1)
Emma_Watson.print_receipt()

# Ariana Grande
Ariana_Grande = BankAccount("Ariana Grande", AccountNum(), RoutNum(), 5000000) 
Ariana_Grande.withdraw(500)
Ariana_Grande.deposit(250)
Ariana_Grande.get_balance(1)
Ariana_Grande.add_interest(1)
Ariana_Grande.print_receipt()

""" STRETCH CHALLENGE: make terminal ATM, with charge for use """