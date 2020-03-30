###the conditional expression with python...
# !/usr/bin/python3

def main():
    a, b = 12, 10
##Genaral Expression...
    if a < b :
        print('a is less then b')

    else:
        print('b is less then a')
##Another Expression for Condition checking...
    check = "a is less" if a < b else "b is less"
    print(check)

if __name__ == "__main__": main()