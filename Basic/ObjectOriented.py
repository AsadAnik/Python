###The Object Oriented Python...
# !/usr/bin/python3

###Class of Object..
class Egg:
    def __init__(self, nameOfOwner = 'Dohn Doe'):
        self.name = nameOfOwner

    def getOwner(self):
        return self.name

def main():
 ##creating object..
    firstObject = Egg()
    print(firstObject.getOwner())

    firstObject.name = 'AA'
    print(firstObject.getOwner())

if __name__ == "__main__": main()