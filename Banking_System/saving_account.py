from user_account import  UserAccount
class SavingAccount(UserAccount):
    def __init__(self,username,password):
        super().__init__(username,password)
    def withdraw(self):
        while True:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Invalid amount!!!")
                    self.get_valid_amount()
                elif self.balance - amount < 100:  # Maintain minimum balance
                    print("Insufficient balance! Minimum balance of 100 must be maintained.")
                    self.get_valid_amount()
                else:
                    self.balance -= amount  # Accessing private variable
                    print("Money withdrawn, Current balance is: ", self.balance)
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                self.get_valid_amount()