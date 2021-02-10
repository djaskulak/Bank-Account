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

####### End of Bank Account class ####### 

# make 3 different bank accounts

""" STRETCH CHALLENGE: make terminal ATM, with charge for use """