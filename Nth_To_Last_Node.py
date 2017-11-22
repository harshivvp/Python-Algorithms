from nose.tools import assert_equal

class TestNLast(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def nth_to_last_node(n,head):

        left_pointer = head
        right_pointer = head

        for i in range(n-1):

            if not right_pointer.nextnode:
                raise LookupError("Error: n is larger than the linked list!")

            right_pointer = right_pointer.nextnode

        while right_pointer.nextnode:

            left_pointer = left_pointer.nextnode
            right_pointer = right_pointer.nextnode

        return left_pointer

    def test(self, sol):
        assert_equal(sol(2, a), d)
        print('ALL TEST CASES PASSED')

a = TestNLast(1)
b = TestNLast(2)
c = TestNLast(3)
d = TestNLast(4)
e = TestNLast(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

target_node = TestNLast.nth_to_last_node(2, a)
target_node.value

t = TestNLast(2)
t.test(TestNLast.nth_to_last_node)
