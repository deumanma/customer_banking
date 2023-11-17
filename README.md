# customer_banking

## Module 3 Challenge

This code is for a customer banking system that will calculate and track interest earned on savings and CD accounts. It includes four starter code files: account.py, savings_account_py, cd_account.py, and customer_banking.py. All of the starter code files have been updated based on the instructions in the homework. Three of the files: account.py, savings_account_py, and cd_account.py are used as imports into customer_banking. The end user is only interacting with the inputs from the customer_banking.py file where it asks for savings and cd account balances, the interest rate percentage for each of the accounts and the total months that the user has had the account open for. Then it will return the updated balance based on interest earned. 

Account.py - creates the account class with the set balance and set interest methods that are called in cd_account, savings_account, and customer_banking. 

cd_account.py - imports the data from account and defined the create cd account function which includes the balance, interest rate and month, and calculates the interest based on those inputs. 

savings_account.py - imports account from account and defines the function for creating the savings acount. and calculates the interest based on balance, interest rates, and months in the account. 

customer banking imports from savings_count and cd_account for their respective creation functions. Then it ass the user to input the following for their savings acount: balance, interest, and maturity of account. Then will print out their new balance accounting for interest earned. Then it asks for the same inputs below but for their CD account information and prints the updated balance for the cd account factoring in interest earned.  

This assignment I did a much better job of writing more useful comments for myself to come back to and documenting where I received help for troubleshooting my code. I did use the class banking solutions file as a reference point when I was getting started and indicated on the file and line if I used outside troubleshooting tools like ChatGPT. I also left some of my old code to see how it evolved over time if I was struggling over a certain part. 

**Note**
The instructions said to add the menu.py file into our repository and initially I did, but it was not referenced anywhere so I removed. 
