
# ATM Simulator

password = "vishnu123"
balance = 10000000000000000

# Login attempt
for i in range(3):
    user_input = input("Enter ATM password: ")
    if user_input == password:
        print("Access Granted \n")
        break
    else:
        print("Wrong password ")
else:
    print("Too many wrong attempts. Card blocked.")
    exit()

# ATM Menu
while True:
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(" Your current balance is:", balance)

    elif choice == "2":
        deposit = float(input("Enter amount to deposit: ₹"))
        if deposit > 0:
            balance += deposit
            print("DONE ₹", deposit, "deposited successfully.")
        else:
            print(" Invalid amount.")

    elif choice == "3":
        withdraw = float(input("Enter amount to withdraw: ₹"))
        if 0 < withdraw <= balance:
            balance -= withdraw
            print("DONE ₹", withdraw, "withdrawn successfully.")
        else:
            print(" Insufficient balance or invalid amount.")

    elif choice == "4":
        print("Thank you for using Vishnu Bank ATM!")
        break

    else:
        print(" Invalid choice. Please select between 1-4.")
