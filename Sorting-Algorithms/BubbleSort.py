def Bubble_Sort(arr):	

	for n in range(len(arr)-1,0,-1):

			for k in range(n):

				if arr[k] > arr[k+1]:

					temp = arr[k]
					arr[k] = arr[k+1]
					arr[k+1] = temp

	print(arr)

Bubble_Sort([3,4,1,5])


arr = [3,2,1,5]
for n in range(len(arr)-1,0,-1):


def SelectionSort(arr):

	for fillslot in range(len(arr)-1,0,-1):

		positionOfMax = 0

		for location in range(1,fillslot+1):

			if arr[location] > arr[positionOfMax]:
				positionOfMax = location

		temp = arr[fillslot]
		arr[fillslot] = arr[positionOfMax]
		arr[positionOfMax] = temp 