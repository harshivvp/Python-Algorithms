import collections
def finder(arr1,arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

def finderXOR(arr1,arr2):

    result = 0

    for num in arr1+arr2:
        result ^= num
        print(result)
    return result

arr1 = [ 2, 3, 4, 5, 6, 7]
arr2 = [2,3, 4, 6,7]
print(finder(arr1,arr2))
print("Smart way of using XOR / ^ ")
print(finderXOR(arr1,arr2))

