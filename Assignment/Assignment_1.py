# Task 1 (50 points)
# Question 1


arr1 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48] # 1
arr2 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48] # 2
arr3 = [15, 13, 16, 12, 17, 11, 18, 10, 19, 9] # 3


# only output the odd values from the above lists (print the output for all lists)
def odd_values(num,arr): # pass the num as list number and arr as list name
    print(f'output for arr {num}: \n')
# your code here
    odd_values = [x for x in arr if x % 2 != 0]
    print(odd_values)
    print('\n End of odd values')

odd_values(1,arr1)
odd_values(2,arr2)
odd_values(3,arr3)



# Question 2
arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] # 1
arr2 = [17, 19, 15, 16, 14, 18, 13, 12, 11, 20] #2
arr3 = [55, 66, 77, 88, 99, 11, 22, 33, 44] #3

# Only output the sum/total of the lists values (print the output for all lists)
def sum_values(num, arr): # pass the num as list number and arr as list name
    print(f'output for arr {num} : \n')
#your code here
    sum = 0
    for i in arr:
        sum = sum + i
    print(sum)    
    print('\n End of sum values')

sum_values(1,arr1)
sum_values(2,arr2)
sum_values(3,arr3)


# Question 3
arr1 = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100] #1
arr2 = [5, -8, 13, -21, 34, -55, 89, -144, 233] #2
arr3 = [-7, 12, -15, 18, -21, 24, -27, 30, -33] #3
arr4 = [11, -22, 33, -44, 55, -66, 77, -88, 99] #4
arr5 = [-3, 6, -9, 12, -15, 18, -21, 24, -27, 30] #5

# Convert the negative values in the following lists to positive and ouput the sum of all values (print the output for all lists).
def converted_sum_values(num, arr): # pass the num as list number and arr as list
 
#your code here
    arr = [-x for x in arr if x < 0]
    sum = 0
    for i in arr:
        sum = sum + i
    print(sum)    
    print(f'output for arr {num} : \n')
    
    print('\n End of converted sum values')

converted_sum_values(1,arr1)
converted_sum_values(2,arr2)
converted_sum_values(3,arr3)
converted_sum_values(4,arr4)
converted_sum_values(5,arr5)

# Question 4
arr1 = ['apple', '', 'banana', '', 'cherry'] #1
arr2 = ['', 'dog', '', 'cat', ''] #2
arr3 = ['hello', '', 'world', '', ''] #3
arr4 = ['', '', '', '', ''] #4
arr5 = ['one', '', 'two', '', 'three'] #5

# Remove empty strings from the above lists and output the lists (print the output for all lists)
def empty_str(num, arr): # pass the num as list number and arr as list name
    print(f'output for arr {num} : \n')
#your code here
    arr = [i for i in arr if i!='']
    print(arr)
    print('\n End of empty str values')

empty_str(1,arr1)
empty_str(2,arr2)
empty_str(3,arr3)
empty_str(4,arr4)
empty_str(5,arr5)

# Question 5
# Write a function that takes in a list and prints the smallest value from that list.

def smallest_num(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    print(smallest)        

smallest_num([5,6,7,3434,656,23,56])



# Task 2 (50 Points)
# This task is divided into sub parts.
# Part 1: Bank Account Class
# 1. Create BankAccount class with following attributes and methods:
# Attributes:
# account_number: An integer.
# balance: A float.
# account_holder: A string.
# Methods:
# deposit(self, amount): Adds the amount to current balance.
# withdraw(self, amount): Subtracts the amount from current balance.

class BankAccount:
    def __init__(self,account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        self.balance = self.balance - amount    

# get_balance(self): Returns the current balance.
    def get_balance(self):
        return self.balance
# call the BankAccount class by creating an instance of it and pass in the values.
# pass the balance as 1000, give a account number and account holder name
bank_account = BankAccount(account_number=7866, balance=1000, account_holder="Prab Yadav")

# call deposit() method, withdraw() method by passing deposit amount as 200,withdraw amount as 700
bank_account.deposit(200)
bank_account.withdraw(700)

# then print the total balance of the account (call the get_balance() method)

print("Bank Account Balance:", bank_account.get_balance())

# Part 2: Checking Account Class
# 1. Create CheckingAccount class that inherits from BankAccount
# 2. Add the following attributes and methods to the CheckingAccount class:
# Attributes:
# transaction_fees: A float, transaction fees charged for each transaction.
# Methods:
# apply_transaction_fees(self): Subtracts the transaction fees from current balance.

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, account_holder, transaction_fees):
        super().__init__(account_number, balance, account_holder)
        self.transaction_fees = transaction_fees

    def apply_transaction_fees(self):
        self.balance -= self.transaction_fees

# call CheckingAccount class by creating an instance of it
# pass the transaction fees as 34.50 and call the apply_transaction_fees() method
# then print the total balance of the account (call the get_balance() method)

checking_account = CheckingAccount(account_number=545341, balance=4432, account_holder="Prabhaa Y", transaction_fees=34.50)
checking_account.apply_transaction_fees()
print("Checking Account Balance:", checking_account.get_balance())


# Part 3: Savings Account Class
# 1. Create SavingsAccount class that inherits from BankAccount.
# 2. Add the following attributes and methods to the SavingsAccount class:
# Attributes:
# interest_rate: A float
# Methods:
# calculate_interest(self): Calculates and adds the interest to the current balance.
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, account_holder, interest_rate):
        super().__init__(account_number, balance, account_holder)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest



# call SavingsAccount class by creating an instance of it
# pass the interest rate as 0.12 and call the calculate_interest() method
# then print the total balance of the account (call the get_balance() method)

savings_account = SavingsAccount(account_number=98765, balance=5000, account_holder="Prabhakar Yadav", interest_rate=0.12)
savings_account.calculate_interest()
print("Savings Account Balance:", savings_account.get_balance())