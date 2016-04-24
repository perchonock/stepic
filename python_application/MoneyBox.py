class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        if self.capacity >= self.money + v:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v) == True:
            self.money += v

piggy = MoneyBox(5)
print(piggy.capacity)
print(piggy.money)
piggy.add(4)
print(piggy.money)

