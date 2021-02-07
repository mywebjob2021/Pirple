#import library numpy classic call
#import numpy

#import library numpy as np
import numpy as np

#call variable arr and give to her array value
arr = np.array([1, 2, 3, 4, 5])

#print variable arr
print(arr)

#print number of installing version 
print(np.__version__)

#print type of variable arr
print(type(arr))

#use dtype checking the data type of an array
print(arr.dtype)
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
"""i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )"""

#examples of Dimensions in Arrays 
# 0-D Arrays
arr = np.array(88)
print(arr)

# 1-D Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print('Last element from 2nd dim: ', arr[0, -1])

# 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
#check how many dimensions the array have
print ("dimantion of arry is: ", arr.ndim)

#access the second element of the zero array of the zero array
print(arr[0, 0, 1])

#slice elements from index 2 to index 4 from the following array
arr = np.array([1, 2, 3, 4, 5])
print(arr[2:4])

#slice elements from index 1 to the end of the array 
print(arr[1:])

#negative slicing
print(arr[-3:-1])

#use step 2 to return every other element from index 1 to index 4
print(arr[1:4:2])

#use step 2 to return every other element from the entire array
print(arr[::2])


#use astype converting data type on existing arrays
#convert to integer
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

#convert to string
newarr = arr.astype('S')
print(newarr)
print(newarr.dtype)





