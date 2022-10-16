import time
import datetime

def deposit():
    while True:
        _deposit = input("DEPOSIT AMOUNT: $")
        if _deposit.isdigit():
            deposit = int(_deposit)
            if deposit > 0:
                break
            else:
                time.sleep(.5)
                print("Please enter a valid amount.")
        else:
            time.sleep(.5)
            print("Please enter a valid amount.")
    str_deposit = str(deposit)
    with open("data/balance.txt", "r") as f:
        previous_amount = f.read()
        int_previous_amount = int(previous_amount)
    with open("data/balance.txt", "w") as f:
        total_deposit = int_previous_amount + deposit
        str_total_deposit = str(total_deposit)
        f.write(str_total_deposit)
    time.sleep(.5)
    print(f"[+] DEPOSITED ${str_deposit}")
    time.sleep(.5)
    print(f"CURRENT BALANCE: ${str_total_deposit}")
    with open("data\logs.txt", "w") as f:
        current_time = datetime.datetime.now()
        day = current_time.strftime("%d")
        month = current_time.strftime("%m")
        year = current_time.strftime("%Y")
        f.write(f"({day}/{month}/{year}) DEPOSITED CASH ${str_deposit}")

def withdraw():
    while True:
        _withdraw = input("WITHDRAW AMOUNT: $")
        if _withdraw.isdigit():
            withdraw = int(_withdraw)
            with open("data/balance.txt", "r") as f:
                previous_amount = f.read()
                int_previous_amount = int(previous_amount)
            if int_previous_amount > withdraw:
                break
            else:
                time.sleep(.5)
                print("Please enter a valid amount.")
        else:
            time.sleep(.5)
            print("Please enter a valid amount.")
    str_withdraw = str(withdraw)
    with open("data/balance.txt", "r") as f:
        previous_amount = f.read()
        int_previous_amount = int(previous_amount)
    with open("data/balance.txt", "w") as f:
        total_withdraw = int_previous_amount - withdraw
        str_total_withdraw = str(total_withdraw)
        f.write(str_total_withdraw)
    time.sleep(.5)
    print(f"[-] WITHDRAW ${str_withdraw}")
    time.sleep(.5)
    print(f"CURRENT BALANCE: ${str_total_withdraw}")
    with open("data\logs.txt", "w") as f:
        current_time = datetime.datetime.now()
        day = current_time.strftime("%d")
        month = current_time.strftime("%m")
        year = current_time.strftime("%Y")
        f.write(f"({day}/{month}/{year}) WITHDRAWAL CASH ${str_withdraw}")


