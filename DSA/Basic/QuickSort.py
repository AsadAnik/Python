## Quick Sorting Algorithm and Program in Python..

## Algorithm...
# First Define the Pivot number from Array.
# Compare Pivot to next number and make replace from node.
# loop while done false ? ->,
    # Condition Pivot >= next number replace first of Pivot.
    # and, left number <= last number then make replace.
    # Set:= leftMark = leftMark + 1;
# Otherwise, next number >= Pivot and last number >= first number,
    # Set:= rightMark = rightMark - 1;

# Condition if last number < first number,
    # Set:= done = True;
# Otherwise,
    # Swap values,
        # Set:= temp = array first item;
        # Set:= array first item = array last item;
        # Set:= array last item = temp;
# returning from partition();



## Program....
def quickSort(data_list):
    quickSortHlp(data_list, 0, len(data_list) - 1)

def quickSortHlp(data_list, first, last):
    if first < last:
        splitPoint = partition(data_list, first, last)
        quickSortHlp(data_list, first, splitPoint - 1)
        quickSortHlp(data_list, splitPoint + 1, last)


def partition(data_list, first, last):
    pivotValue = data_list[first]
    leftMark = first + 1
    rightMark = last
    done = False

    while not done:
        while leftMark <= rightMark and data_list[leftMark] <= pivotValue:
            leftMark = leftMark + 1

        while data_list[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark = rightMark - 1

        if rightMark < leftMark:
            done = True
        else:
            temp = data_list[leftMark]
            data_list[leftMark] = data_list[rightMark]
            data_list[rightMark] = temp

    temp = data_list[first]
    data_list[first] = data_list[rightMark]
    data_list[rightMark] = temp

    return rightMark



data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(data_list)
print(data_list)
