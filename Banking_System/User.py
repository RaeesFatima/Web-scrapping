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

    @username.setter
    def username(self,new_username):
        if len(new_username)>=3:
            self.__username=new_username
        else:
            print("Username must be at least 3 characters long.")

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
                    num = int(input("\nPress 1 to re-enter amount or another key to exit! "))
                    if num != 1:
                        print("exited")
                        break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

                num = int(input("\nPress 1 to re-enter amount or another key to exit! "))
                if num != 1:
                    print("exited")
                    break

        # return self.__balance

    def withdraw(self):
        while True:
            try:
                amount=int(input("Enter amount to withdraw: "))
                if amount > self.__balance:
                    print("Insufficient balance")
                    num = int(input("\nPress 1 to re-enter amount or another key to exit! "))
                    if num != 1:
                        print("exited")
                        break
                elif amount<=0:
                    print("Invalid amount!!!")
                    num = int(input("\nPress 1 to re-enter amount or another key to exit! "))
                    if num != 1:
                        print("exited")
                        break
                else:
                    self.__balance = self.__balance - amount
                    print("Money withdraw, Current balance is: ", self.__balance)
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                num = int(input("\nPress 1 to re-enter amount or another key to exit! "))
                if num != 1:
                    print("exited")
                    break
        # return self.__balance

def show_menu(user):
    while True:
        print("1. Show Account details")
        print("2. Show current balance")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Exit")
        num = int(input("choose 1 to 5 what do you want: "))

        if num == 1:
            print("--------------Account Details-------------")
            print(
                f"Username:\t\t{user.username}\nPassword:\t\t{user.password}\nAccount No.:\t{user.account_number}\n")
        elif num == 2:
            print("your current balance is: ", user.balance)
        elif num == 3:
            user.deposit()
        elif num == 4:
            user.withdraw()
        elif num == 5:
            print("\nThank you for using our banking system. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please choose a valid option.")

        again = input("\nPress 0 to show menu again, any other key to exit: ")
        if again != "0":
            print("\nThank you for using our banking system. Goodbye!")
            break  # Exit

# users=[]
print("Hello dear user, Create your account here!")
name=input("Please enter your name : ")
passwrd=input("Please enter your password : ")

# users.append({"name":username,"password":password,"account_number":1})
# print(users)

user1=UserAccount(name,passwrd)
menu = int(input("\nPress 0 to show menu (or any other key to exit): "))
if menu == 0:
    show_menu(user1)
else:
    print("\nThank you for using our banking system. Goodbye!")
