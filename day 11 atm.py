Account_holder_Name=input("enter your name:")
def credits(bal,amount):
    if amount>0:
        bal += amount
        print(f"your account is credited with {amount} now your total bank balance is :{bal}")
    else:
        print("please enter positive value")
    return bal

def debit(bal,amount):
    if bal>=amount:
        bal-=amount
        print(f"your account is debited for Rs.{amount} and your current balance is Rs.{bal}")
    elif amount>bal:
        print(f"insuffient balance")
    else:
        print("please enter the positive value")
    return bal

def balancecheck(bal):
    # bal global
    print(f"{Account_holder_Name} your current balance is Rs.{bal}")

def wish(end="thank you"):
    return end
print(wish())
bal=0
while True:
    print(f"Atm Machine")
    print("to show Atm Uses select choice 1")
    print("1)credit the amount")
    print("2)debit the amount")
    print("3)for balance enquiery")
    print("4)exit")
    choice=input("enter the choice :")
    if choice=="1":
        amount=float(input("enter the amount"))
        bal=credits(bal,amount)
    elif choice=="2":
        amount=float(input("enter the amount:"))
        bal= debit(bal,amount)
    elif choice=="3":
        balancecheck(Account_holder_Name,bal)
    elif choice=="4":
        print(wish())
    else:
        print("invalid choice")


