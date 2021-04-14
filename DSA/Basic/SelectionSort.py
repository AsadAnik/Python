### Selection sort in python..
# The selection sort algorithm sorts an array by repeatedly finding the minimum element(considering ascending order) from unsorted part and putting it at the beginning.
# The algorithm maintains two subarrays in a given array.

# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.

# In every iteration of selection sort,
# the minimum element(considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.


## Program...
def selectionSort(nList):
    for fillSlot in range(len(nList) - 1, 0, -1):
        maxPos = 0
        for location in range(1, fillSlot+1):
            if nList[location] > nList[maxPos]:
                maxPos = location

            temp = nList[fillSlot]
            nList[fillSlot] = nList[maxPos]
            nList[maxPos] = temp

            print('Sorting -->> ', nList)


unsortedList = [5, 3, 8, 6, 7, 2]
selectionSort(unsortedList)
print('Sorted == ', unsortedList)