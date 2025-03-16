from saving_account import SavingAccount
from current_account import CurrentAccount

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
                f"Username:\t\t{user.username}\nAccount No.:\t{user.account_number}\n")
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

acc_type = input("\nEnter account type (Saving/Current): ").strip().lower()
if acc_type == "saving":
    user1 = SavingAccount(name, passwrd)
    # print("you have chosen saving")
elif acc_type == "current":
    user1 = CurrentAccount(name, passwrd)
else:
    print("Invalid account type! Defaulting to Saving Account.")
    user1 = SavingAccount(name, passwrd)

menu = int(input("\nPress 0 to show the menu (or any other key to exit): "))
if menu == 0:
    show_menu(user1)
else:
    print("\nThank you for using our banking system. Goodbye!")


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="home",
  database="mydatabase"
)

mycursor = mydb.cursor()

# Insert a new user (Ensure this is done first)
sql = "INSERT INTO users (name, password) VALUES (%s, %s)"
val = ("raees", "home")
mycursor.execute(sql, val)
mydb.commit()


user_id = mycursor.lastrowid


sql = "INSERT INTO transactions (transaction_made, balance, userid) VALUES (%s, %s, %s)"
val = ("deposit", 3000, user_id)
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted in transactions.")
