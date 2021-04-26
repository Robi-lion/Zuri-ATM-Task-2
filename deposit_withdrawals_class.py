class Transactions:
  def __init__(self, amount, name):
    self.name = name
    self.amount = 0
  
  def check_funds(self):
    total = 0
    total += self.amount
    return total

  def isSufficient(self, amount):
    if amount <= self.check_funds():
        return True
    else:
        return False

  def withdraw(self, amount, description = ""):
    if self.isSufficient(amount):
        self.amount -= amount
        new_istr = f"you have withdrawn {amount} from your account , your balance is {self.amount}"
        return new_istr
    else:
        return False

  def deposit(self, amount, description = ""):
    self.amount +=  amount
    new_istr2 = f"you have deposited {amount} in your account, your balance is {self.amount}"
    return new_istr2