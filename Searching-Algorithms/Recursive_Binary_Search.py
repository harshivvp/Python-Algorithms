def recursive_BS(arr,ele):

	if len(arr) == 0:
		return False
	else:
		mid = len(arr)//2

		if arr[mid] == ele:
			return True
		else:
			if ele < arr[mid]:
				return recursive_BS(arr[:mid],ele)
			else:
				return recursive_BS(arr[mid+1:],ele)

print(recursive_BS([1,3,5,6,8,10],2))
print(recursive_BS([1,3,5,6,8,10],3))