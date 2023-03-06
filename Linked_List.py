import time
import random
class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class.  replace pass with your implementation
            # NOTE: Performance is O(1), there is no way to call this function twice by itself as it is tied to the node
            # NOTE: If you were to create a bunch of nodes that would be different, but this is a method of one individual node so O(1)
            self.val = val
            self.next = None 
            self.prev = None

            

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        # NOTE: Performance is O(1). Tied to the setup of one specific Linked_List Object, and runs at the creation 
        # NOTE: So, should not be above O(1). 
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0



    def __len__(self):
        # Return the number of value-containing nodes in this list. 
        # NOTE: O(1), as __size is an attribute of the Linked_list class that is stored
        # NOTE: So, it does not have to loop over anything to get it.
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new __tail position. this is the only way to add items at the __tail
        # position.
        # NOTE: Performance of O(1). As we know the tail position and it always adds an element to the tail position, 
        # it does not have to walk the whole linked list to get it, and can always just start from right before it has to insert. 
        # I also ran a runtime test to be sure, and it is definitely constant.  
        new_node = self.__Node(val)
        self.__size += 1
        if self.__size <= 1:
            self.__header.next = new_node
            self.__trailer.prev = new_node
            new_node.prev = self.__header
            new_node.next = self.__trailer
        else: 
            new_node.prev = self.__trailer.prev
            new_node.prev.next = new_node
            new_node.next = self.__trailer
            self.__trailer.prev = new_node

    def __get_node_at(self, index):
        """
        Custom method I made, used in other public methods. I wanted something the same as self.get_element_at, but that returned the node at that index instead. 
        I needed this as many other methods seem to use this and I didn't want to duplicate code. 
        The performance of this should be O(n), as it has to walk the whole list exactly once.         
        """
        if (index < 0) or (index > self.__size-1):
            raise IndexError
        cur = self.__header.next
        for idx in range(index):
            cur = cur.next
        return cur
    def insert_element_at(self, val, index):
        # Assuming the head position (not the __header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. 
        # NOTE: Performance should be O(n). It has to walk the entire distance of the list a single time to find 
        # NOTE: the place it must insert itself at. After that has been found, it only has constant time operations. as the limit
        # NOTE: as n -> inf makes constant time irrelevant, it is only O(n). Also it uses the __get_node_at private method to do this actual looping, so should be the same. 
        # NOTE: I also measured the performance in the runtime tests and it matches up at being approximately linear in practice. 
        if (index < 0) or (index >= self.__size):
            raise IndexError
        self.__size += 1
        new_node = self.__Node(val)
        after = self.__get_node_at(index)
        if index == 0: 
            self.__header.next = new_node
        before = after.prev
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node

    def remove_element_at(self, index):
        # Assuming the head position (not the __header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. 
        # NOTE: Remove element at will be O(n) time complexity consistently. 
        # Whatever the index number, it must loop that many times to find the element. 
        # It uses __get_note_at private method, so that is where the looping comes from 
        # Tested with runtime tests and it is linear time in practice
        if (index < 0) or (index >= self.__size):
            raise IndexError
        element = self.__get_node_at(index)
        element.prev.next = element.next
        element.next.prev = element.prev
        return_value = element.val
        element = None
        self.__size -= 1
        return return_value
        
    def get_element_at(self, index):
        # Assuming the __head position (not the __header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. 
        # NOTE: This function is O(n). It has to travel to the point in the list element by element to find it
        # NOTE: Tested with runtime tests and it is indeed linear time. 
        if (index < 0) or (index >= self.__size):
            raise IndexError
        cur = self.__header.next
        for elm in range(index):
            cur = cur.next
        return cur.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. 
        # NOTE: This method is O(1). It only has to mess with elements near the header and trailer nodes
        # NOTE: and swap some values around. This distance is always the same relative to these nodes, and 
        # NOTE: thus is constant time. 
        if self.__size == 0:
            return  
        self.__header.next.prev = self.__trailer.prev
        self.__trailer.prev.next = self.__header.next
        self.__trailer.prev = self.__header.next
        self.__header.next = self.__header.next.next
        self.__header.next.prev = self.__header
        self.__trailer.prev.next = self.__trailer

        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations.  
        # NOTE: This method is O(n). It has to traverse the entire list element by element and print it out
        # NOTE: It only has to do it once as it walks the list, however, to it will stay linear time
        # NOTE: Tested with runtime test, it is linear. 
        printstr = ""
        for elm in self: 
            printstr += f" {str(elm)},"
        return f"[{printstr[:-1]} ]"

    def __repr__(self):
        """
        Representation of it, is the exact same as __str__ but works when calling in the REPL. 
        Added mostly for debugging purposes. Same O(n) as __str__ 
        """
        return str(self)

    def __iter__(self):
        # Initialize a new attribute for walking through your list 
        # NOTE: This function itself is O(1), but it is typically called with __next__ by the system which goes across 
        # NOTE: an element each time __next__ is called.
        self.__current = self.__header.next
        return self


    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. 
        # NOTE: This method is O(1) by itself, as it only checks a single value and decides if it needs to be returned. 
        # NOTE: but this is missing the fact that the system calls it until the StopIteration Exception. 
        # NOTE: If we count the whole process, including that, it is O(n), as it has to travel the list. 
        # NOTE: Runtime tests of the full iteration process show O(n)
        if self.__current is not self.__trailer:
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
        # NOTE: This method is O(n). Each time it is called, it creates a new list, and then walks across the new and old at the same time
        # NOTE: it walks across the old list backwards, however, using .prev instead of .next. But this is one loop, and becaues it walks it at the same
        # NOTE: time, it doesn't have to have any sort of nested loop, and is therefore O(n). 
        # NOTE: Runtime tests also show it is O(n)
        revself = Linked_List()
        cur = self.__trailer
        rev = revself.__header
        for x in range(self.__size):
            rev.next = revself.__Node(cur.prev.val)
            rev.next.prev = rev
            rev = rev.next
            cur = cur.prev
            revself.__size += 1
        revself.__trailer.prev = rev
        rev.next = revself.__trailer
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
    # NOTE: TEST CODE BELOW
    # NOTE: I would not normally put functions in the if __name__ == '__main__' section. 
    # But i was not sure how the grading system would see that, and you said to put it in here
    # So I will just keep it here even if it looks ugly.
    # Explanations of test cases in the docstrings for the various functions 
    # ALSO NOTE: the runtime tests can be a little finnickey, if they dont work just run them again and it should work. 

    
   

    def append_tests():
        """
        This tests 4 situations 
        1. Basic generating the object of class Linked_List. just figured I should have this in here somewhere
        2. appending to create a list of size 1 (ie empty list and adding another one)
        3. list of size 2 (I can more completely test with this one vs a longer one)
        4. list of size 4 (just to make sure it works on larger size lists)

        A bunch of the test cases here are quite complicated and some of the messages are a bit confusing but it does test everything.
        """
        print('starting basic append tests')
        try: 
            testlst = Linked_List()
        except: print('  🔴 Failed Obj. Creation')
        else: print('  ✅ Passed Obj. Created')

        try: 
            testlst.append_element(1)
            assert testlst._Linked_List__header.next.val == 1, 'headval'
            assert len(testlst) == 1, 'length'
            assert testlst._Linked_List__trailer.prev.val == 1, 'tailval'
            assert testlst._Linked_List__header.next.next is testlst._Linked_List__trailer, 'headnext = none'
        except AssertionError as err: print("  🔴 Failed list size 1 attributes:", err)
        except: print("  🆘 Failed list size 1 UNKNOWN ERROR")
        else: print('  ✅ Passed List size 1')

        try: 
            testlst.append_element(2)
            assert len(testlst) == 2, 'length'
            assert testlst._Linked_List__header.next.val == 1, 'headval'
            assert testlst._Linked_List__trailer.prev.val == 2, 'tailval'
            assert testlst._Linked_List__header.next.next is testlst._Linked_List__trailer.prev, 'head.next =tail'
            assert testlst._Linked_List__trailer.prev.prev is testlst._Linked_List__header.next, 'tail.prev =head'
            assert testlst._Linked_List__trailer.prev.next is testlst._Linked_List__trailer, 'tail.next None'
        except AssertionError as err: 
            print("  🔴 Failed list size 2 attributes:", err)
        except: print("  🆘 Failed list size 2 UNKNOWN ERROR")
        else: print('  ✅ Passed List size 2')

        try: 
            testlst.append_element(3)
            testlst.append_element(4)
            assert len(testlst) == 4, 'length'
            assert testlst._Linked_List__header.next.val == 1, 'headval'
            assert testlst._Linked_List__trailer.prev.val == 4, 'tailval'
            assert testlst._Linked_List__header.prev is None, 'head prev'
            assert testlst._Linked_List__trailer.prev.next is testlst._Linked_List__trailer, 'tail next'
            assert testlst._Linked_List__header.next.next.val == 2, 'next from head val'
            assert testlst._Linked_List__header.next.next.prev is testlst._Linked_List__header.next, 'wrapping back to head'
            assert testlst._Linked_List__header.next.prev is testlst._Linked_List__header, 'wrapping back to head'
            assert [i for i in testlst] == [1,2,3,4], 'to list'
        except AssertionError as err: print("  🔴 Failed list size 4 attributes:", err)
        except: print("  🆘 Failed list size 4 UNKNOWN ERROR")
        else: print('  ✅ Passed List size 4')
        
    def basic_test_lst(length = 25) -> Linked_List:
        """
        Simple helper function used to generate test lists that just are a range of integers
        """
        lst = Linked_List()
        for x in range(length):
            lst.append_element(x)
        return lst
    def str_test():
        """
        tests string generation. Starts with 0 and makes sure it is [ ], as described

        then goes to test a longer list of size n > 1 with the correct one space to the left and right, and no trailing comma

        then goes to test a single digit, to make sure it still works and puts the [ elm ] spacing around the single element, and no comma in any 
        """
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
        
    def remove_tests():
        """
        simple test of removing elements from lists. uses a test case of [0,1,2,3,4]
        1. tests removing first digit
        2. tests removing third digit (index = 2)
        3. tests removing final digit (index = 4)

        also tests for length.
        """
        print('starting remove_element_at tests')
        testlst = basic_test_lst(length = 5)
        unmodified_lst = basic_test_lst(length = 5)
        try: 
            testlst.remove_element_at(0)
            assert [i for i in testlst] == [1,2,3,4]
            assert len(testlst) == 4, 'length error'
            [i for i in reversed(testlst)]
        except AssertionError as err: print(' 🔴 Failed to remove element at zero:', err, str(testlst))
        except: 
            print("  🆘 unknown removal at zero error")
            raise
        else: print("  ✅ Passed removal at Zero")
        testlst = basic_test_lst(length = 5)
        try: 
            testlst.remove_element_at(2)
            assert len(testlst) == 4, 'length error'
            assert [i for i in testlst] == [0,1,3,4]
            [i for i in reversed(testlst)]
        except AssertionError as err: print(' 🔴 Failed to remove element at 2:', err, str(testlst))
        except: 
            print("  🆘 unknown removal at 2 error")
            raise
        else: print("  ✅ Passed removal at 2")
        testlst = basic_test_lst(length = 5)
        try: 
            testlst.remove_element_at(4)
            assert len(testlst) == 4, 'length error'
            assert [i for i in testlst] == [0,1,2,3]
            [i for i in reversed(testlst)]
        except AssertionError as err: print(' 🔴 Failed to remove element at end:', err, str(testlst))
        except: 
            print("  🆘 unknown removal at end error")
            raise
        else: print("  ✅ Passed removal at end")

    def insert_element_tests(): 
        """
        Tests insertign elements at: 
        1. index = 0 (head)
        2. index = 3 (example of normal insert)

        and the following were set to intentionally fail to make sure it gives the correct index error: 
        1. index < 0
        2. index > length
        3. inserting at tail (not allowed)
        """
        print('starting insert_element_at tests')
        testlst = basic_test_lst(length = 20)
        unmodified_lst = basic_test_lst(length = 20)
        try: 
            testlst.insert_element_at('lmao', 0)
            assert testlst._Linked_List__header.next.val == 'lmao', f"headval"
            assert testlst._Linked_List__header.next.next.val == 0, 'next val is zero'
            assert testlst.get_element_at(0) == 'lmao', 'get_element_at'
            assert len(testlst) == 21, 'length'
        except AssertionError as err: print("  🔴 Failed insert at zero: ", err, str(testlst)) 
        except: 
            print("  🆘 unknown insert at zero error")
            raise
        else: print("  ✅ Passed Insert at Zero")

        testlst = basic_test_lst(length = 10)
        try: 
            testlst.insert_element_at('lmao', 3)
            assert testlst._Linked_List__header.next.val == 0, f"headval"
            assert testlst._Linked_List__header.next.next.val == 1, 'next val is zero'
            assert testlst.get_element_at(3) == 'lmao', 'get_element_at'
            assert [i for i in testlst] == [0, 1, 2, 'lmao', 3, 4, 5, 6, 7, 8, 9], 'fullequals'
            assert len(testlst) == 11, 'length'
            [i for i in reversed(testlst)]
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
            testlst.insert_element_at('lmao', 11)
            assert [id(val) for val in testlst] == pointers_original, 'changed list'
        except IndexError: print('  ✅ Passed >length IndexError')
        except AssertionError: print('  🔴 Failed >length IndexError: changed memory')
        else: print('  🔴 Failed >length IndexError')
        
        testlst = basic_test_lst(length = 10)
        # inserttail 
        try: 
            testlst.insert_element_at('lmao', 10)
            assert [id(val) for val in testlst] == pointers_original, 'changed list'
        except IndexError: print('  ✅ Passed tail IndexError')
        except AssertionError: print('  🔴 Failed tail IndexError: changed memory')
        else: print('  🔴 Failed tail IndexError', str(testlst))
    


    def reverse_tests():
        """
        Simple test case of reversing the list. 
        it 
        1. tests to make sure the values didn't mutate the order of the original list
        2. test to make sure it reversed the test case correctly (value wise)
        3. a run through of all the pointer IDs from opposite directions, makes sure they still point to the same values even if the list itself is different. 
        """
        print('starting reversed tests')
        revlst = basic_test_lst(length = 10)
        revorig = basic_test_lst(length = 10)
        try: rev = reversed(revlst)
        except: print('  🔴 Failed to reverse List')
        else: print('  ✅ Passed reverse() call')

        try: 
            assert [i for i in revlst] == [i for i in revorig], 'mutate original'
        except AssertionError as err: print('  🔴 Mutated Values in original list', err, str(revlst), str(revorig))
        except: 
            raise
        else: print('  ✅ Passed mutate check')

        try: 
            assert [i for i in rev] == [9,8,7,6,5,4,3,2,1,0], 'Value Check'
            assert len(rev) == len(revorig), 'length check'
        except AssertionError as err: print('  🔴 Failed Value Check', err, str(rev))
        except: print('  🆘 Unknown value check error')
        else: print('  ✅ Passed value check')

        # pointer check 
        try: 
            cur = revlst._Linked_List__header.next
            revcur = rev._Linked_List__trailer.prev
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
        """
        simple test cases to make sure rotate works correctly. 
        starts with simple value check to make sure it is like it supposed to be
        ends with bit trying to make sure the connections all work correctly

        """
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

        #tail/_Linked_List__head check
        try: 
            assert testlst._Linked_List__header.next.prev is testlst._Linked_List__header, 'headprev'
            assert testlst._Linked_List__header.next.next.val == 2, 'headnext'
            assert testlst._Linked_List__trailer.prev.next is testlst._Linked_List__trailer, 'tailnext'
            assert testlst._Linked_List__trailer.prev.prev.val == 5, 'tailprev'
            [i for i in reversed(testlst)]
        except AssertionError as err: print('  🔴 Failed tail/head Check', err, str(testlst))
        except: 
            print('  🆘 Failed tail/head Check, unknown error')
            raise
        else: print('  ✅ Passed tail/head Check')

    def iter_test():
        """
        simple test case of iterating to make sure it works fine. 
        1. creates two lists, one linked list and one python list. runs through them and makes sure it is iterating correctly
        2. same thing, but reversed in direction 
        """
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
    def runtime_ratio(function, n1 = 1000, n2 = 10000, num = 1, *args, **kwargs):
        """
        very messy function, just used to time a bunch of custom functions later to try and compute it at two different n values
        if it is not the correct time complexity, it would blow up or be way smaller than it if n1 and n2 are sufficiently different
        """
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

    def runtime_check_helper(name, fn, n_1, n_2, number, method = 'linear', lower = .3, upper = 1.3):
        """
        small helper function to make it easier to write lots of runtime tests
        """
        try: 
            results = runtime_ratio(fn, n1 = n_1, n2 = n_2, num = number)
            assert results[-1] < upper, f"more than {method}"#random number; about linear ish 
            assert results[-1] > lower,  f"less than {method}"#random number; about linear ish 
        except AssertionError: print(f"  🔴 Failed: {name} runtime Not {method}", results)
        else: print(f"  ✅ Passed: {name} runtime ~{method}. ({results[-1]})")
    
                
    def runtime_check():
        """
        just creating little functions and passing them to two previous functions to print and output the runtime results 
        """
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
        def removetest(n, lst:Linked_List):
            lst.remove_element_at(n-3)
        runtime_check_helper('remove_element_at', removetest, 2000, 30000, 1)
        def appendtest(n, lst:Linked_List):
            lst.append_element('test')
        runtime_check_helper('append_element', appendtest, 2000, 3000000, 10, method = 'constant', lower = 0, upper = .1)
        def rotatetest(n, lst:Linked_List):
            lst.rotate_left()
        runtime_check_helper('rotate_left', rotatetest, 2000, 3000000, 10, method = 'constant', lower = 0, upper = .1)
        
        def revtest(n, lst:Linked_List):
            reversed(lst)
        runtime_check_helper('reversed', revtest, 2000, 10000, 10)
    append_tests()
    rotate_tests()
    str_test()
    remove_tests()
    insert_element_tests()
    reverse_tests()
    iter_test()
    runtime_check()
    