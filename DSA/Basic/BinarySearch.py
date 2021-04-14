## Python Program for Binary Search (Recursive and Iterative)..
# In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison.

### Easy Algorithm...
# defining an Array and take a number to make search with it.
# loop trow the array and check found is default false.
    # when array length is done then return from loop.
    # and when found is true then also return from loop.
# in loop let's make mid and find it (find the middle node of array) (mid = (first + last) / 2).
# if middle is search item which you want then, make found true.
    # after find the mid which is search item then return from all and result is this.
# if search item is less then mid item of array so make sure last one make (last = mid - 1).
# if search item is greater then mid item of array so make sure first one make (first = mid + 1).
# after all make return of found , and which would find your search item there.


### Algorithm...
# Define Array [1, 2, 3, 5, 8];
# set:= first = 0, last is length of arr[] - 1, found = false;
# while loop throw -->> first <= last and not found:
    # set:= mid = (first + last) / 2;
    # condition if arr[mid] == searchFor:
        # set:= found is True;
    # Otherwise,
        # condition if searchFor < arr[mid]:
            # set:= last = mid - 1;
        # Or, Otherwise,
            # set:= first = mid + 1;
# return the found;
# end of program.


### Program...
def binary_search(arr, searchFor):
    first = 0
    last = len(arr) - 1
    found = False

    while(first <= last and not found):
        mid = (first + last) // 2
        if arr[mid] == searchFor:
            found = True
        else:
            if searchFor < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

print(binary_search([1, 2, 3, 5, 8], 6))
print(binary_search([1, 2, 3, 5, 8], 5))


#### Check the (Binary Search Methods) folder to understand by diagrams..