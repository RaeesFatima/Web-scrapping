class UserAccount:
    account_number=0
    def __init__(self,username,password):
        self.__username=username
        self.__password=password
        UserAccount.account_number+=1
        self.__balance=130

    @property
    def username(self):
        return  self.__username

    @property
    def password(self):
        return self.__password

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    @username.setter
    def username(self,new_username):
        if len(new_username)>=3:
            self.__username=new_username
        else:
            print("Username must be at least 3 characters long.")

    @staticmethod
    def get_valid_amount():
        num = int(input("\nPress 1 to re-enter amount or another key to exit! "))
        if num != 1:
            print("exited")

    def deposit(self):
        while True:
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount>0:
                    self.__balance=self.__balance+amount
                    print("Money deposited, Current balance is: ",self.__balance)
                    break
                else:
                    print("Invalid amount!!!!")
                    self.get_valid_amount()
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                self.get_valid_amount()

        # return self.__balance

    def withdraw(self):
        while True:
            try:
                amount=int(input("Enter amount to withdraw: "))
                if amount > self.__balance:
                    print("Insufficient balance")
                    self.get_valid_amount()
                elif amount<=0:
                    print("Invalid amount!!!")
                    self.get_valid_amount()
                else:
                    self.__balance = self.__balance - amount
                    print("Money withdraw, Current balance is: ", self.__balance)
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                self.get_valid_amount()
        # return self.__balance
