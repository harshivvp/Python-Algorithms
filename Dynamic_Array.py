import ctypes

class DynamicArray():

    def __init__(self):

        self.n = 0
        self.capacity = 1
        self.A = self.make_Array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):

        if not 0 <= k < self.n:
            return IndexError

        return self.A[k]

    def append(self,element):

        if self.n == self.capacity:
            self._resize(self.capacity * 2) #2x capacity if not enough

        self.A[self.n] = element
        self.n += 1

    def _resize(self,new_cap):

        B = self.make_Array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_Array(self,new_cap):

        return(new_cap * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
print('Length of array is : ', len(arr))
print('Array element appended : ' , arr[0])
