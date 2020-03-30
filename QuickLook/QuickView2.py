###Specified the Numbers with Python...
def numberSpecifier(n):
    if n == 1:
        print('1 is special')
        return False

    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n//x))
            return False
        else:
            print('{} this is prime number!'.format(n))
            return True

for n in range(1, 20):
    numberSpecifier(n)