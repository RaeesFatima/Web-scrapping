# Online Banking System (CLI-based)

## Project Overview
This is a simple CLI-based Online Banking System built using Python and Object-Oriented Programming (OOP) principles. The system allows users to create and manage their bank accounts, including depositing and withdrawing money while ensuring basic validation checks.

## Features
- **User Authentication**: Users can create accounts with a username and password.
- **Account Types**:
  - **Saving Account**: Requires a minimum balance of 100.
  - **Current Account**: Allows overdrafts.
- **Banking Operations**:
  - Show account details
  - Check balance
  - Deposit money
  - Withdraw money (with specific rules based on account type)
- **Data Encapsulation**: Private attributes for security.

## Installation and Setup
### Prerequisites
Ensure you have Python installed on your system (Python 3.x recommended).

### Steps to Run
1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the `main.py` file:
   ```sh
   python main.py
   ```
5. Follow the on-screen instructions to create an account and perform banking operations.

## File Structure
```
├── main.py               # Entry point of the application
├── user_account.py       # Base UserAccount class
├── saving_account.py     # SavingAccount subclass with withdrawal restrictions
├── current_account.py    # CurrentAccount subclass allowing overdrafts
├── README.md             # Project documentation
```

## Usage
1. Run `main.py` and create an account by entering your username and password.
2. Choose between a **Saving Account** or **Current Account**.
3. Use the menu options to:
   - View account details
   - Check balance
   - Deposit money
   - Withdraw money (with respective rules)
4. Exit the program when done.

## Future Improvements
- Implement user authentication with a database.
- Add transaction history.
- Improve UI using a graphical interface.

## Conclusion
This project provides a foundational banking system with basic account management features using Python and OOP concepts. While currently a CLI-based system, it can be expanded with more functionalities, database integration, and a graphical interface for a better user experience. It serves as a great learning experience for understanding banking operations and object-oriented design principles.

## License
This project is open-source and free to use.

## Author
Developed by Raees Fatima

