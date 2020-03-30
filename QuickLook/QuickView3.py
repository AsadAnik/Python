###Class/Object with Fibonacci work...
class Fibo():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

#making object instence for this class..
f = Fibo(0, 1)
for r in f.series():
    if r > 100: break
    print(r, end='')