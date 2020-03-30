##Using the Python Structure with python...
# #!/usr/bin/python3

def main():
    print("Hello World!")

    a = 'AsadAnik'
    typeOf = type(a)
    print(typeOf, a)

    b = 123
    typeOf = type(b)
    print(typeOf, b)

 ##Swapping values
    aa, bb = 0, 1
    aa, bb = bb, aa
    print('After Swapped value of aa, bb = {}, {}'.format(aa, bb))

 ##Tuple values
    tupleValues = (1, 2, 3, 4, 5)
    print(tupleValues)

 ##List values
    listValues = [1, 2, 3, 4, 5, 6, 7]
    print(listValues)

if __name__ == "__main__": main()