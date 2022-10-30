def pay_vat():
    with open("data/balance.txt", "r") as f:
        current_balance_ = f.read()
        current_balance = int(current_balance_)
        x = {17*current_balance/100}
    print(f"YOU PAID ${x} IN SALES TAX!")
    print(x)

