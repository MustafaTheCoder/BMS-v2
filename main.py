from functions import deposit, pay_vat, withdraw
import time

def main():
    print(f"""\n
    WELCOME TO BMSV2.0
    """)
    while True:
        print("""\n
        [1] VIEW BALANCE
        [2] DEPOSIT BALANCE 
        [3] WITHDRAW BALANCE
        [4] VIEW TRANSACTIONS
        [5] PAY VAT
        [6] EXIT
        """)
        while True:
            time.sleep(.5)
            options = input("[+] OPTION: ")
            print("\n")
            if options.isdigit:
                option_chosen = int(options)
                if option_chosen > 0:
                    break
                else:
                    time.sleep(.5)
                    print("Please enter a valid option.")
            else:
                time.sleep(.5)
                print("Please enter a valid option.")


        if option_chosen == 1:
            with open("data/balance.txt", "r") as f:
                current_bal = f.read()
                int_current_bal = int(current_bal)
            print(f"CURRENT BALANCE: ${int_current_bal}")
        elif option_chosen == 2:
            deposit()
        elif option_chosen == 3:
            withdraw()
        elif option_chosen == 4:
            with open("data\logs.txt", "r") as f:
                data = f.read()
                print(data)
        elif option_chosen == 5:
            pay_vat()
        elif option_chosen == 6:
            print("SHUTTING DOWN... 3")
            time.sleep(.5)
            print("SHUTTING DOWN... 2")
            time.sleep(.5)
            print("SHUTTING DOWN... 1")
            time.sleep(.5)
            exit()

main()
            