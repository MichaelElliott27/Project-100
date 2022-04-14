class BankAtm(object):


  def __init__(self, CashWithdrawl, BalanceEnquiry, RemainingMoney, MoneyAllowedToTakeOutAtOnce):
    self.BalanceEnquiry = BalanceEnquiry
    self.RemainingMoney = RemainingMoney
    self.MoneyAllowedToTakeOutAtOnce = MoneyAllowedToTakeOutAtOnce
    self.CashWithdrawl, = CashWithdrawl,

  def atmPinNumber(self):
    print("0371")

  def atmCardNumber(self):
    print("172936212")

  def atmLocator(self):
    print("2 Atm's found nearby")
    "atmLocator functionality here"



money = BankAtm("$20", "$100", "$384", "$50")

print(money.BalanceEnquiry)
