def iter_BS(arr,ele):

	first = 0
	last  = len(arr) - 1
	found = False

	while not found and first <= last:

		mid = (first + last) // 2

		if arr[mid] == ele:

			found = True

		else:

			if ele > arr[mid]:
				first = mid + 1
			else:
				last = mid - 1
