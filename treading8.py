import threading

account_balance = 1000

def withdraw_money(amount):
    global account_balance
    if account_balance >= amount:
        account_balance -= amount
        print("Remaining balance:", account_balance)
    else:
        print("Insufficient balance")

# Correct way to create threads
thred1 = threading.Thread(target=withdraw_money, args=(500,))
thred2 = threading.Thread(target=withdraw_money, args=(800,))

thred1.start()
thred2.start()

thred1.join()
thred2.join()

print("Final account balance:", account_balance)
