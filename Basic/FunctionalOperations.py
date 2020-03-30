###The Functional Operations with Python...
# !/usr/bin/python3

def main():
    showLength(9)
    showLength(7)
    showLength(5)
    showLength(4)
    showLength(2)
    showLength(1)

##Funtion...
def showLength(num):
    for i in range(num ,10):
        print(i, end=' ')
    print()#newLine..

if __name__ == "__main__" : main()