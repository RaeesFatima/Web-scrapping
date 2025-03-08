from user_account import  UserAccount
class CurrentAccount(UserAccount):
    def __init__(self,username,password):
        super().__init__(username,password)

    def withdraw(self):
        while True:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Invalid amount!!!")
                    self.get_valid_amount()
                else:
                    self.balance -= amount  # Allow overdraft
                    print("Money withdrawn, Current balance is: ", self.balance)
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                self.get_valid_amount()