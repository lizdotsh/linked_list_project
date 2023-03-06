import time
import random
class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.next = None 
            self.prev = None

            

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__head = None
        self.__tail = None
        self.__size = 0



    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new __tail position. this is the only way to add items at the __tail
        # position. TODO replace pass with your implementation
        new_node = self.__Node(val)
        self.__size += 1
        if self.__size <= 1:
            self.__head = new_node
            self.__tail = new_node
        else: 
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node

    def _get_node_at(self, index):
        if 0 > index >= self.__size:
            raise IndexError
        cur = self.__head
        for idx in range(index):
            cur = cur.next
        return cur
    def insert_element_at(self, val, index):
        # Assuming the __head position (not the __header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the __tail position. TODO
        # replace pass with your implementation
        if (index < 0) or (index >= self.__size - 1):
            raise IndexError
        self.__size += 1
        new_node = self.__Node(val)
        after = self._get_node_at(index)
        if index == 0: 
            self.__head = new_node
        else:
            before = after.prev
            before.next = new_node
            new_node.prev = before
        new_node.next = after
        after.prev = new_node
        



        



    def remove_element_at(self, index):
        # Assuming the __head position (not the __header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if 0 > index > self.__size - 1: 
            raise IndexError
        element = self.get_element_at(index)
        element.prev.next = element.next
        element.next.prev = element.prev
        element = None
        self.__size = self.__size - 1
    def get_element_at(self, index):
        # Assuming the __head position (not the __header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if 0 > index > self.__size - 1:
            raise IndexError
        cur = self.__head
        for elm in range(index):
            cur = cur.next
        return cur.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the __head, which should become the ___tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        self.__head.prev = self.__tail
        self.__tail.next = self.__head
        self.__tail = self.__head
        self.__head = self.__tail.next
        self.__tail.next = None
        self.__head.prev = None

        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations.  replace pass with your implementation
        #return str([elm for elm in self])
        printstr = ""
        for elm in self: 
            printstr += f" {str(elm)},"
        return f"[{printstr[:-1]} ]"

    def __repr__(self):
        """
        Representation of it, is the exact same as __str__ but works when calling in the REPL. 
        Added mostly for debugging purposes 
        """
        return str(self)

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__current = self.__head
        return self


    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__current:
            val = self.__current.val
            self.__current = self.__current.next
            return val
        else:
            raise StopIteration


    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        revself = Linked_List()
        revself.__head = revself.__Node(self.__tail.val)
        revself.__size += 1
        cur = self.__tail
        rev = revself.__head

        for x in range(1, self.__size):
            rev.next = revself.__Node(cur.prev.val)
            rev.next.prev = rev
            rev = rev.next
            cur = cur.prev
            revself.__size += 1
        revself.__tail = rev
        return revself


if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from __head to __tail? Does a for loop
    # iterate through your reversed list from __tail to __head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    
    # TEST CODE BELOW
    # NOTE: I would not normally put functions in the if __name__ == '__main__' section. 
    # But i was not sure how the grading system would see that, and you said to put it in here
    # So I will just keep it here even if it looks ugly.

    
    def runtime_ratio(function, n1 = 1000, n2 = 10000, num = 1, *args, **kwargs):
    #  if list != None:
        n1_lst = basic_test_lst(n1)
        
        st = time.process_time()
        for x in range(num):
            function(n1,n1_lst, **kwargs)

        et = time.process_time()
        n1_time = (1000*(et - st))/ num 
        n2_lst = basic_test_lst(n2)
        st = time.process_time()
        for x in range(num):
            function(n2,n2_lst, **kwargs)
        et = time.process_time() 
        n2_time = (1000*(et - st))/ num
        overall_ratio = (n2_time/n2) / (n1_time/n1)
        raw_ratio = (n2_time) / (n1_time)
        return (n1_time, n2_time, n2/n1, raw_ratio, overall_ratio)


    def basic_methods(l1):
        try:
            print('trying basic methods')
            if len(l1) > 0:
                print(f"__head: {l1.__head.val}")
                print(f"__tail: {l1.__tail.val}")
            if len(l1) > 1:
                print(f"__head; next: {l1.__head.next.val}")
            print(f"length: {len(l1)}")
            print(f"string: {str(l1)}")
            print('passed basic methods')
        except: "basic method failure"
        try: 
            l1.insert_element_at
        except: "insert_element_at method failure"
    def append_tests():
        print('starting basic append tests')
        try: 
            testlst = Linked_List()
        except: print('  🔴 Failed Obj. Creation')
        else: print('  ✅ Passed Obj. Created')

        try: 
            testlst.append_element(1)
            assert testlst.__head.val == 1, '__headval'
            assert len(testlst) == 1, 'length'
            assert testlst.__tail.val == 1, '__tailval'
            assert testlst.__head.next is None, '__headnext = none'
        except AssertionError as err: print("  🔴 Failed list size 1 attributes:", err)
        except: print("  🆘 Failed list size 1 UNKNOWN ERROR")
        else: print('  ✅ Passed List size 1')

        try: 
            testlst.append_element(2)
            assert len(testlst) == 2, 'length'
            assert testlst.__head.val == 1, '__headval'
            assert testlst.__tail.val == 2, '__tailval'
            assert testlst.__head.next is testlst.__tail, '__head.next = __tail'
            assert testlst.__tail.prev is testlst.__head, '__tail.prev = __head'
            assert testlst.__tail.next is None, '__tail.next None'
        except AssertionError as err: 
            print("  🔴 Failed list size 2 attributes:", err)
        except: print("  🆘 Failed list size 2 UNKNOWN ERROR")
        else: print('  ✅ Passed List size 2')

        try: 
            testlst.append_element(3)
            testlst.append_element(4)
            assert len(testlst) == 4, 'length'
            assert testlst.__head.val == 1, '__headval'
            assert testlst.__tail.val == 4, '__tailval'
            assert testlst.__head.prev is None, '__head prev'
            assert testlst.__tail.next is None, '__tail next'
            assert testlst.__head.next.val == 2, 'next from __head val'
            assert testlst.__head.next.prev is testlst.__head, 'wrapping back to __head'
            assert [i for i in testlst] == [1,2,3,4], 'to list'
        except AssertionError as err: print("  🔴 Failed list size 4 attributes:", err)
        except: print("  🆘 Failed list size 4 UNKNOWN ERROR")
        else: print('  ✅ Passed List size 4')
        
    def basic_test_lst(length = 25) -> Linked_List:
        lst = Linked_List()
        for x in range(length):
            lst.append_element(x)
        return lst
    def str_test():
        print('starting __str__ tests:')
        try:
            lst = str(basic_test_lst(length = 0))
            assert lst == "[ ]"
        except AssertionError: print("  🔴 Zero String Formatting Error", lst)
        except: print("  🆘 unknown zero length string error")
        else: print("  ✅ Passed Zero Length")

        try: 
            lst = str(basic_test_lst(length = 5))
            assert lst == "[ 0, 1, 2, 3, 4 ]"
        except AssertionError: print("  🔴 multi String Formatting Error", lst)
        except: print("  🆘 unknown multi length string error")
        else: print("  ✅ Passed multi Length")

        try: 
            lst = str(basic_test_lst(length = 1))
            assert(lst) == "[ 0 ]"
        except AssertionError: print("  🔴 Single String Formatting Error", lst)
        except: print("  🆘 unknown Single length string error")
        else: print("  ✅ Passed single Length")
        

    def insert_element_tests(): 
        print('starting insert_element_at tests')
        testlst = basic_test_lst(length = 20)
        unmodified_lst = basic_test_lst(length = 20)
        try: 
            testlst.insert_element_at('lmao', 0)
            assert testlst.__head.val == 'lmao', f"__headval"
            assert testlst.__head.next.val == 0, 'next val is zero'
            assert testlst.get_element_at(0) == 'lmao', 'get_element_at'
            assert len(testlst) == 21, 'length'
            assert testlst.__head.next.val == unmodified_lst.__head.val, f"unmodif {testlst.__head.next.val}; {unmodified_lst.__head.val}"
        except AssertionError as err: print("  🔴 Failed insert at zero: ", err, str(testlst)) 
        except: 
            print("  🆘 unknown insert at zero error")
            raise
        else: print("  ✅ Passed Insert at Zero")

        testlst = basic_test_lst(length = 10)
        try: 
            testlst.insert_element_at('lmao', 3)
            assert testlst.__head.val == 0, f"__headval"
            assert testlst.__head.next.val == 1, 'next val is zero'
            assert testlst.get_element_at(3) == 'lmao', 'get_element_at'
            assert [i for i in testlst] == [0, 1, 2, 'lmao', 3, 4, 5, 6, 7, 8, 9], 'fullequals'
            assert len(testlst) == 11, 'length'
            assert testlst._get_node_at(3).next.val == unmodified_lst._get_node_at(3).val, f"unmodif next {testlst._get_node_at(3).next.val}; {unmodified_lst._get_node_at(3).val}"
            assert testlst._get_node_at(3).prev.val == unmodified_lst._get_node_at(2).val, f"unmodif prev {testlst._get_node_at(3).prev.val}; {unmodified_lst._get_node_at(2).val}"
        except AssertionError as err: print("  🔴 Failed insert at three: ", err, str(testlst)) 
        except: 
            print("  🆘 unknown insert at three error")
            raise
        else: print("  ✅ Passed Insert at three")

        # Indexerrors

        # <0 Indexerror
        testlst = basic_test_lst(length = 10)
        pointers_original = [id(val) for val in testlst]
        try: 
            testlst.insert_element_at('lmao', -1)
            assert [id(val) for val in testlst] == pointers_original, 'changed list'
        except IndexError: print('  ✅ Passed <0 IndexError')
        except AssertionError: print('  🔴 Failed <0 IndexError: changed memory')
        else: print('  🔴 Failed <0 IndexError')

        # >length indexerror
        try: 
            testlst.insert_element_at('lmao', 10)
            assert [id(val) for val in testlst] == pointers_original, 'changed list'
        except IndexError: print('  ✅ Passed >length IndexError')
        except AssertionError: print('  🔴 Failed >length IndexError: changed memory')
        else: print('  🔴 Failed >length IndexError')
        
        # insert __tail 
        try: 
            testlst.insert_element_at('lmao', 9)
            assert [id(val) for val in testlst] == pointers_original, 'changed list'
        except IndexError: print('  ✅ Passed __tail IndexError')
        except AssertionError: print('  🔴 Failed __tail IndexError: changed memory')
        else: print('  🔴 Failed __tail IndexError', str(testlst))
    


    def reverse_tests():
        print('starting reversed tests')
        revlst = basic_test_lst(length = 10)
        revorig = basic_test_lst(length = 10)
        try: rev = reversed(revlst)
        except: print('  🔴 Failed to reverse List')
        else: print('  ✅ Passed reverse() call')

        try: 
            assert [i for i in revlst] == [i for i in revorig], 'mutate original'
        except AssertionError as err: print('  🔴 Mutated Values in original list', err, str(revlst), str(revorig))

        try: 
            assert [i for i in rev] == [9,8,7,6,5,4,3,2,1,0], 'Value Check'
            assert len(rev) == len(revorig), 'length check'
        except AssertionError as err: print('  🔴 Failed Value Check', err, str(rev))
        except: print('  🆘 Unknown value check error')
        else: print('  ✅ Passed value check')

        # pointer check 
        try: 
            #revlst.__head.val = 'lmao'
            #revlst.__head.next.val = 'lmao2'
            cur = revlst.__head
            revcur = rev.__tail
            comparison = []
            boollst = []
            for i in range(len(rev)):
                comparison.append((id(cur.val), id(revcur.val)))
                boollst.append((id(cur.val) == id(revcur.val)))
                cur = cur.next
                revcur = revcur.prev
            assert all(boollst), 'same memory ids'
        except AssertionError as err: print('  🔴 Not pointing to the same data', str(comparison), str(boollst))
        except: print('  🆘 Unknown obj in memory error')
        else: print('  ✅ Passed same obj in memory check')
    def rotate_tests():
        print('starting rotate_left tests')
        testlst = basic_test_lst(length = 6)
        try: 
            testlst.rotate_left()
            assert [i for i in testlst] == [1, 2, 3, 4, 5, 0], 'fulllist'
        except AssertionError as err: print('  🔴 Failed Value Check', err, str(testlst))
        except: 
            print(' 🆘 Failed Value Check, unknown error')
            raise
        else: print('  ✅ Passed Value Check')

        # __tail/__head check
        try: 
            assert testlst.__head.prev is None, '__headprev'
            assert testlst.__head.next.val == 2, '__headnext'
            assert testlst.__tail.next is None, '__tailnext'
            assert testlst.__tail.prev.val == 5, '__tailprev'
        except AssertionError as err: print('  🔴 Failed __tail/__head Check', err, str(testlst))
        except: 
            print(' 🆘 Failed __tail/__head Check, unknown error')
            raise
        else: print('  ✅ Passed __tail/__head Check')

    def iter_test():
        print('starting iteration tests')
        lst = basic_test_lst(100)
        unlinked_lst = [i for i in range(100)]
        try: 
            for a,b in zip(lst, unlinked_lst): 
                if a != b: 
                    raise ValueError
        except ValueError: print(" 🔴 Failed Iteration Test", str(lst), str(unlinked_lst))
        except: 
            print(' 🆘 Failed Iteration test: Unknown error')
            raise
        else: print('  ✅ Passed Iteration Test')

        # Reversed
        try: 
            for a,b in zip(reversed(lst), reversed(unlinked_lst)): 
                if a != b: 
                    raise ValueError
        except ValueError: print(" 🔴 Failed Reverse Iteration Test", str(lst), str(unlinked_lst))
        except: 
            print(' 🆘 Failed Reversed Iteration test: Unknown error')
            raise
        else: print('  ✅ Passed Reversed Iteration Test')

    def runtime_check_helper(name, fn, n_1, n_2, number, method = 'linear', lower = .3, upper = 1.3):
        try: 
            results = runtime_ratio(fn, n1 = n_1, n2 = n_2, num = number)
            assert results[-1] < upper, f"more than {method}"#random number; about linear ish 
            assert results[-1] > lower,  f"less than {method}"#random number; about linear ish 
        except AssertionError: print(f"  🔴 Failed: {name} runtime Not {method}", results)
        else: print(f"  ✅ Passed: {name} runtime ~{method}. ({results[-1]})")
    
                
    def runtime_check():
        print('starting runtime tests')
        def strtest(n,lst):
            return str(lst)
        runtime_check_helper('String', strtest, 10000, 600000, 10)
        # Iterator
        def itertest(n,lst):
            for x in lst:
                x
        runtime_check_helper('iter', itertest,1000,1000000, 1 )

        # get_element_at
        def gettest(n,lst:Linked_List):
            lst.get_element_at(n-1)
        runtime_check_helper('get_element_at', gettest, 2000, 30000, 10)
        def inserttest(n, lst:Linked_List):
            lst.insert_element_at('test',n-2)
        runtime_check_helper('insert_element_at', inserttest, 2000, 30000, 10)
        def rotatetest(n, lst:Linked_List):
            lst.rotate_left()
        runtime_check_helper('rotate_left', rotatetest, 2000, 3000000, 10, method = 'constant', lower = 0, upper = .1)
        def revtest(n, lst:Linked_List):
            reversed(lst)
        runtime_check_helper('reversed', revtest, 200, 10000, 10)
    append_tests()
    str_test()
    insert_element_tests()
    reverse_tests()
    iter_test()
    rotate_tests()
    runtime_check()
    l1 = Linked_List()
    print(str(l1))
    print(f"length: {len(l1)}")
    l1.append_element(5)
    basic_methods(l1)
    l1.append_element(2)
    basic_methods(l1)
    listtest = [i for i in l1]
    print(listtest)
    for x in [random.randint(0, 100000) for i in range(100)]:
        l1.append_element(x)
    basic_methods(l1)
