def seq_search(arr,ele):

	found = False
	pos = 0

	while pos < len(arr) and not found:

		if arr[pos] == ele:

			found = True

		else:

			pos += 1

	return found

print(seq_search([1,2,3,4,5],2))