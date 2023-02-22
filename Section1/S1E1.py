class Mat:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        
    def add(self):
        return self.n1 + self.n2
    
    def sub(self):
        return self.n1 - self.n2

    def div(self):
        return self.n1/self.n2

    def mult(self):
        return self.n1 * self.n2

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
m = Mat(n1, n2)

print(m.add())
print(m.sub())
print(m.div())
print(m.mult())

    