# Python program for reversal algorithm of array rotation


# Algorithm:
#
# rotate(arr[], d, n)
# reverse(arr[], 1, d);
# reverse(arr[], d + 1, n);
# reverse(arr[], 1, n);

# arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2 and n = 7
# A = [1, 2] and B = [3, 4, 5, 6, 7]
#
# Reverse A, we get
# ArB = [2, 1, 3, 4, 5, 6, 7]
# Reverse B, we get
# ArBr = [2, 1, 7, 6, 5, 4, 3]
# Reverse all, weget(ArBr)
# r = [3, 4, 5, 6, 7, 1, 2]


# Function to reverse arr[] from index start to end


def reverseArray(arr, start, end):
	while (start < end):
		temp = arr[start]
		arr[start] = arr[end]
		arr[end] = temp
		start += 1
		end = end-1

# Function to left rotate arr[] of size n by d


def leftRotate(arr, d):

	if d == 0:
		return
	n = len(arr)
	# in case the rotating factor is
	# greater than array length
	d = d % n
	reverseArray(arr, 0, d-1)
	reverseArray(arr, d, n-1)
	reverseArray(arr, 0, n-1)

# Function to print an array


def printArray(arr):
	for i in range(0, len(arr)):
		print arr[i],


# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2

leftRotate(arr, d) # Rotate array by 2
printArray(arr)
