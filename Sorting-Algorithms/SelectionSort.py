def SelectionSort(arr):

	for fillslot in range(len(arr)-1,0,-1):

		positionOfMax = 0

		for location in range(1,fillslot+1):

			if arr[location] > arr[positionOfMax]

				positionOfMax = location
					