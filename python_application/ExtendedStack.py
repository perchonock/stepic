class ExtendedStack(list):
    def sum(self):
        a = self.pop()
        b = self.pop()
        self.append(a+b)

    def sub(self):
        a = self.pop()
        b = self.pop()
        self.append(a-b)

    def mul(self):
        a = self.pop()
        b = self.pop()
        self.append(a*b)

    def div(self):
        a = self.pop()
        b = self.pop()
        self.append(a//b)