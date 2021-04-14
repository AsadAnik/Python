## Linear Searching Algorithm In Python..
# Array Is -> [10, 14, 19, 26, 31, 33, 35, 42, 44];

## Algorithm..
# Start from the leftmost element of given arr[] and one by one compare element x with each element of arr[]
# If x matches with any of the element, return the index value.
# If x doesn’t match with any of elements in arr[] , return -1 or element not found.

## Program..
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10, 14, 19, 26, 31, 33, 35, 42, 44]
x = 19
# search = str(linear_search(arr, x))
print("Element found at index "+str(linear_search(arr, x)))