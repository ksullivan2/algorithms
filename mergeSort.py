myArray = [1, 5, 3, 7, 4, 2, 3, 6, 8, 9]
from math import ceil

def mergeSort(array):

	aux = []
	for value in array:
		aux.append(value)
	

	splitMerge(array, aux, 0, len(array))
	return array
	


def splitMerge(array, aux, low, high):
	mid = int((high+low) / 2)
	
	if len(array[low:high]) > 1:
		splitMerge(array, aux, low, mid)
		splitMerge(array, aux, mid, high)
		merge(array, aux, low, mid, high)
		copyArray(array, aux, low, high)
	else:
		return

def merge(array, aux, low, mid, high):
	leftHalfIndex = low
	rightHalfIndex = mid

	for index in range(low,high):
		#if there are still left values remaining AND
		#either ran out of right half values OR left value is less than right value
		if leftHalfIndex < mid and (rightHalfIndex >= high or array[leftHalfIndex] <= array[rightHalfIndex]):
			#store the value of the leftHalfIndex into the aux array at the correct place
			aux[index] = array[leftHalfIndex]
			#move the left pointer up one
			leftHalfIndex += 1
		else:
			#store the value of the rightHalfIndex into the aux array at the correct place
			aux[index] = array[rightHalfIndex]
			#move the right point up one
			rightHalfIndex += 1
	
def copyArray(array, aux, low, high):
	for index, value in enumerate(aux):
		array[index] = value


print(mergeSort(myArray))