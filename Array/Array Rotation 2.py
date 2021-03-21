def leftRotate(arr, d, n):
    for i in range(d):
        leftRotateByOne(arr, n)

#Here the elements of the array are moved towards right
# by one position and the initial first element will be stored at the end of the array.
# This process will continue 'd' times
def leftRotateByOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def printArray(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")


arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)