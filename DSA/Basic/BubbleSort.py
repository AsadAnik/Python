## Bubble Sorting Algorithm implementing in Python...
# range functions definition..
# range(stop)...
# range(start, stop)..
# range(start, stop, step).

## Algorithm..
# loop throw for list and another loop one for iteration inner..
# then compare 2nd element with 1st element then swap..
    # swap if 2nd > 1st then, swap.
    # Otherwise, nothing..


## Program..
def bubbdleSort(nList):
    for passnum in range(len(nList) - 1, 0, -1):
        for i in range(passnum):
            if nList[i] > nList[i + 1]:
                temp = nList[i]
                nList[i] = nList[i + 1]
                nList[i + 1] = temp


randomNums = [5, 3, 8, 6, 7, 2]
bubbdleSort(randomNums)
print(randomNums)



# Resource link in bubble sorting...
# (https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php)