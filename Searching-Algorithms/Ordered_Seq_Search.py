def ordered_seq_search(arr,ele):

	found = False
	pos = 0 
	stopped = False

	while pos < len(arr) and not found and not stopped:

		if arr[pos] == ele:

			found = True

		else:

			if arr[pos] > ele:

				stopped = True

			else:

				pos += 1

	return found

print(ordered_seq_search([1,2,3,4,5],5))