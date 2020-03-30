###The Quick Review of Python's latest version here...
##Updated in Expression in Python3..
a, b = 0, 1
print("a is less then b" if a<b else "a is greater then b")

###There is another updates wih value assignments..
##Used with the format function inner of print function..
print('a ({}) is less then b ({})'.format(a, b))

###With the for loops examples...
fh = open('lines.txt')
for line in fh.readlines():
    print(line, end='')