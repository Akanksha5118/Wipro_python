class Calc:
    def add(self, *params):
        total = 0
        for x in params:
            total += x
        return total


c = Calc()
print(c.add(20, 30))
print(c.add(20, 30, 40))
print(c.add(10, 20, 30, 40, 50))
