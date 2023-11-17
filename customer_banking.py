# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE

from savings_account import create_savings_account

from cd_account import create_cd_account

# Define the main function
def main(create_savings_account, create_cd_account):

    # old code below: 
    # def main(create_savings_account, create_cd_account):
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    
    savings_balance = float(input("Please enter your savings account balance: "))
    savings_interest = float(input("What is the interest rate for this account: "))
    savings_maturity = float(input("How many months have you had this account? "))

    # Call the create_savings_account function and pass the variables from the user. This is starting code
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your updated balance is {updated_savings_balance: ,.2f} and your interest earned is: {interest_earned: ,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    cd_balance = float(input(("What is your CD Balance? ")))
# example to come back to 
# cd_balance = input(float("What is your CD Balance? "))

    cd_interest = float(input(("What is your interest rate? ")))
    cd_maturity = float(input(("How many months have you had this CD? ")))

    # Call the create_cd_account function and pass the variables from the user. this was starting code
# old code 
# updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    updated_cd_balance, interest_earned_cd = create_cd_account(cd_balance, cd_interest, cd_interest)


    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    # used formatting from class assignment to update the : .2f
    print(f"Your updated CD balance is: {updated_cd_balance: ,.2f} and your earned interest is: {interest_earned_cd: ,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main(create_savings_account, create_cd_account)