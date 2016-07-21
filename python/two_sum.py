
# Implement a TwoSum interface that has 2 methods: Store and Test.
# Store adds an integer to an internal data store and
# Test checks if an integer passed to Test is the sum of any two integers
# in the internal data store.
# Once you provide an answer interviewer will ask the O complexity of the solution and ask you to optimize it.

# Questions : Are duplicate integers allowed in the data store



#oset = set([105,99,4,6,9,1, 4, 23, 2,3])

#print(oset)

#print(sorted(oset))

class Two_Sum:

    #sorted_data_store = None

    def __init__(self):
        self.data_store = set()
        self.sorted_data_store = set()

    def store(self,number):
        self.data_store.add(number)
        self.sorted_data_store = sorted(self.data_store)

    def test(self):
        print(self.sorted_data_store)




ts = Two_Sum()

ts.store(3)
ts.store(5)
ts.store(105)
ts.store(3)
ts.store(99)
ts.store(4)
ts.test()
