"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE

from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
   
 # Used chatGpt to help trouble shoot getting the variables in the right format so i could calculate
 # interest earned in line 34
    balance = float(balance)
    interest_rate = float(interest_rate)
    months = int(months)

 # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    
    account = Account(balance, 0)


    # Calculate interest earned
    # ADD YOUR CODE HERE

    interest_earned = balance * interest_rate/100 * months/12 
    # previous line of code on 27 
    # interest_earned = float(balance) * interest_rate/100 * months/12 

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE

    new_cd_balance = interest_earned + balance

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    account.set_balance(new_cd_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return new_cd_balance, interest_earned

    # return  f'Here is your updated account balance: {new_cd_balance: ,.2f} and here is your earned interest: {interest_earned: ,.2f}'
    # I got help from chat GPT on line 44

    