def iterative_BS(arr,ele):

	first = 0
	last = len(arr) - 1
	found = False

	while first <= last and not found:
		
		mid = (first + last)//2

		if arr[mid] == ele:
			found = True
		else:
			if ele < arr[mid]:
				last = mid - 1
			else:
				first = mid + 1

	return found

print(iterative_BS([1,2,3,4,5,6,7,8],9))
print(iterative_BS([1,2,3,4,5,6,7,8],3))


def BubbleSort(arr):

	for n in range(len(arr) - 1, 0,-1) #here, for array = [1,2,3,4], output will be [3,2,1]. not taking the last element cuz len(arr)-1.
	