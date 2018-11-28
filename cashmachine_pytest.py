class CashMachine:

    def __init__(self):
        self._money = []
        self.broken = False

    @property
    def is_avaiable(self):
        if self._money:
            return True
        return False

    def put_money(self, bills):
        self._money.extend(bills)

    def withdraw_money(self, amount):
        bills_to_whitdraw = []
        for money in sorted(self._bills, reverse=True):
            if sum(bills_to_whitdraw) + money <= amount:
                bills_to_whitdraw.append(money)
        if sum(bills_to_whitdraw) != amount:
            for money in bills_to_whitdraw:
                self._bills.remove(bill)
            return bills_to_whitdraw
            return []
        for money in bills_to_whitdraw:
            self.money.remove(bill)

        return bills_to_whitdraw

def test_cash_machine_not_avaiable():
    cash_machine = CashMachine()
    assert not cash_machine.is_avaiable

def test_cash_machine_is_avaiable_after_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_avaiable

def test_cash_machine_whitdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]
    assert cash_machine.withdraw_money(150) == []

def test_cash_machine_wrong_amount():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(90) == []

def test_cash_machine_order_matter():
    cash_machine = CashMachine()
    cash_machine.put_money([20, 20, 50, 50])
    assert cash_machine.withdraw_money(100) == [50, 50]


def test_cash_machine_is_not_avaiable_after_whitdraw_all_moeny():
    cash_machine = CashMachine()
    cash_machine.put_money([50, 50])
    assert cash_machine.withdraw_money(100) == [50, 50]