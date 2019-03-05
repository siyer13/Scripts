class Calculator:

    def add(self, a, b):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise TypeError('Parameters must be integers')
        return a + b

    def mul(self, d, e):
        return d * e

    def complicated_calculation(self, a, b):
        c = self.add(a, b) + self.mul(a, b)
        return c



cal = Calculator()
val = cal.complicated_calculation(10,10)
print(val)
