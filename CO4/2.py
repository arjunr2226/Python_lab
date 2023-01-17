class Bank:
  acc_count = 0
  def __init__(self, acc_no, name, acc_type, bal):
    self.acc_no = acc_no
    self.name = name
    self.acc_type = acc_type
    self.bal = bal
    Bank.acc_count += 1
  def deposit(self, amnt):
    self.bal += amnt
    return self.bal
  def withdraw(self, amnt):
    self.bal -= amnt
    return self.bal
  def bals(self):
    return self.bal
  def display(self):
    print("\n\n")
    print(self.acc_no, self.name, self.acc_type, self.bal)
    print("\n\n")

i=1
while i != 0:
  ch = int(input("1.CREATE\n2.DISPLAY\n3.DEPOSIT\n4.WITHDRAW\n0.EXIT"))
  if ch == 1:
    b1 = Bank(1, input("ENTER NAME: "), input("ENTER ACCOUNT TYPE:"), int(input("ENTER BALANCE: ")))
  elif ch == 2:
    b1.display()
  elif ch == 3:
    amnt = int(input("ENTER AMOUNT TO DEPOSIT: "))
    if amnt < 0:
      print("ENTER VALID AMOUNT")
    else:  
      b1.deposit(amnt)
  elif ch == 4:
    amnt = int(input("ENTER AMOUNT TO WITHDRAW: "))
    if amnt < 0:
      print("ENTER VALID AMOUNT")
    elif b1.bals() < amnt:
      print("INSUFICIENT BALANCE")
    else:
      b1.withdraw(amnt)
  elif ch == 0:
    break
  else:
    print("WRONG OPTION!")