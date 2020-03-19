"""
-------------------------------------------------------
Various Data Structure Utilities
-------------------------------------------------------
Author:  Laksitha Dissanayake
ID:      170870810
Email:   diss0810@mylaurier.ca
__updated__ = "2020-03-19"
-------------------------------------------------------
"""

# Imports
from Deque_array import Deque
from List_array import List
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue
from Stack_array import Stack

# from Stack_linked import Stack
# from queue_linked import Queue
# from Priority_Queue_linked import Priority_Queue
# from List_linked import List
# from Deque_linked import Deque
# Constants
SEP = "-" * 60


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack, 
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        stack.push(source.pop())
    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())
    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue, 
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        queue.insert(source.pop(0))
    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())
    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq, 
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        pq.insert(source.pop(0))
    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist, 
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        llist.append(source.pop(0))
    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
        target.append(llist.pop(0))
    return


def array_to_deque(deque, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last element in source is at bottom of stack, 
    first element in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        deque - source PriorityQueue object (PriorityQueue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        deque.insert_front(source.pop(0))
    return


def deque_to_array(deque, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top element of stack is at end of target,
    bottom element of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        deque - target PriorityQueue object (PriorityQueue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not deque.is_empty():
        target.append(deque.remove_front())
    return

# Test Functions


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and 
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()

    print("Stack Initialised")
    print()
    print(SEP)
    print("Stack is_empty (expect True): {}".format(s.is_empty()))
    print(SEP)
    print("Add one item to Stack:")
    s.push(source[0])
    print("Top of Stack (peek):")
    print(s.peek())
    print(SEP)
    print("Stack is_empty (expect False): {}".format(s.is_empty()))
    print(SEP)
    print("Stack pop:")
    v = s.pop()
    print(v)
    print(SEP)
    print("Stack is_empty (expect True): {}".format(s.is_empty()))
    print(SEP)
    print("Copy all data to Stack")
    array_to_stack(s, source)
    print(SEP)
    print("Stack is_empty (expect False): {}".format(s.is_empty()))
    print(SEP)
    print("Top of Stack (peek):")
    print(s.peek())
    print(SEP)
    print("Remove all elements from Stack")

    while not s.is_empty():
        v = s.pop()
        print(v)
        print()

    print(SEP)
    print("Stack is_empty (expect True): {}".format(s.is_empty()))
    print()
    return


def queue_test(source):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: test_Queue_array(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        the methods of CircularQueue are tested for both is_empty and 
        non-is_empty queues using the data in source:
        is_empty, push, pop, peek
    -------------------------------------------------------
    """
    q = Queue()

    print("Queue Initialised")
    print()
    print(SEP)
    print("Queue is_empty (expect True): {}".format(q.is_empty()))
    print("Queue size (expect 0): {}".format(len(q)))
    print(SEP)
    print("Add one item to Queue")
    q.insert(source[0])
    print("Front of Queue (peek):")
    print(q.peek())
    print(SEP)
    print("Queue is_empty (expect False): {}".format(q.is_empty()))
    print("Queue size (expect 1): {}".format(len(q)))
    print(SEP)
    print("Queue remove")
    v = q.remove()
    print(v)
    print(SEP)
    print("Queue is_empty (expect True): {}".format(q.is_empty()))
    print("Queue size (expect 0): {}".format(len(q)))
    print(SEP)
    print("Copy all data to Queue")
    array_to_queue(q, source)
    print("Queue is_empty (expect False): {}".format(q.is_empty()))
    print("Queue size (expect > 0): {}".format(len(q)))
    print(SEP)
    print("Front of Queue (peek):")
    print(q.peek())
    print(SEP)
    print("Remove all elements from Queue")

    while not q.is_empty():
        v = q.remove()
        print(v)
        print()

    print(SEP)
    print("Queue is_empty (expect True): {}".format(q.is_empty()))
    print("Queue size (expect 0): {}".format(len(q)))
    print()
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: Priority_Queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Priority_Queue are tested for both is_empty and 
        non-is_empty priority queues using the data in a:
        is_empty, push, pop, peek
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print("Priority Queue Initialised")
    print()
    print(SEP)
    print("Priority Queue is_empty (expect True): {}".format(pq.is_empty()))
    print("Priority Queue size (expect 0): {}".format(len(pq)))
    print(SEP)
    print("Add one item to Priority Queue")
    pq.insert(a[0])
    print("Front of Priority Queue (peek):")
    print(pq.peek())
    print(SEP)
    print("Priority Queue is_empty (expect False): {}".format(pq.is_empty()))
    print("Priority Queue size (expect 1): {}".format(len(pq)))
    print(SEP)
    print("Priority Queue remove")
    v = pq.remove()
    print(v)
    print(SEP)
    print("Priority Queue is_empty (expect True): {}".format(pq.is_empty()))
    print("Priority Queue size (expect 0): {}".format(len(pq)))
    print(SEP)
    print("Copy all data to Priority Queue")
    array_to_pq(pq, a)
    print("Priority Queue is_empty (expect False): {}".format(pq.is_empty()))
    print("Priority Queue size (expect > 0): {}".format(len(pq)))
    print(SEP)
    print("Front of Priority Queue (peek):")
    print(pq.peek())
    print(SEP)
    print("Remove all elements from Priority Queue")

    while not pq.is_empty():
        v = pq.remove()
        print(v)
        print()

    print(SEP)
    print("Priority Queue is_empty (expect True): {}".format(pq.is_empty()))
    print("Priority Queue size (expect 0): {}".format(len(pq)))
    print()
    return


def list_test(a):
    l1 = List()
    # Grab an arbitrary value as a key value
    key = a[0]

    print("Empty list: ")
    print("  Size: {}".format(len(l1)))
    print("  Empty: {}".format(l1.is_empty()))
    print("  Key: {}".format(key))
    print("  Key in list: {}".format(key in l1))

    print(SEP)
    print('Fill the list.')

    array_to_list(l1, a)

    print(SEP)

    for v in l1:
        print(v)
    print()

    print("  Max: {}".format(l1.max()))
    print()
    print("  Min: {}".format(l1.min()))
    print()
    print('Using Key Value')
    print("  Key: {}".format(key))
    print()
    print("  Key in list: {}".format(key in l1))
    print()
    print("  Key count {} times".format(l1.count(key)))
    print()
    print("  Find value: {}".format(l1.find(key)))
    print()
    print("Removing a value:")
    print(l1.remove(key))
    print("Appending a value")
    l1.append(key)
    print("Inserting a value at 0")
    l1.insert(0, key)
    print("Counting a value:")
    n = l1.count(key)
    print("Count: {}".format(n))
    i = l1.index(key)
    print("Index of {}: {}".format(key, i))
    return


def deque_test(source):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: deque_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        the methods of PriorityQueue are tested for both is_empty and 
        non-is_empty priority queues using the data in source:
        is_empty, push, pop, peek
    -------------------------------------------------------
    """
    deque = Deque()

    print("Deque Initialised")
    print()
    print(SEP)
    print("Deque is_empty (expect True): {}".format(deque.is_empty()))
    print("Deque size (expect 0): {}".format(len(deque)))
    print(SEP)
    print("Add one item to Deque")
    deque.insert_front(source[0])
    print("Front of Deque (peek):")
    print(deque.peek_front())
    print(SEP)
    print("Deque is_empty (expect False): {}".format(deque.is_empty()))
    print("Deque size (expect 1): {}".format(len(deque)))
    print(SEP)
    print("Deque remove")
    v = deque.remove_front()
    print(v)
    print(SEP)
    print("Deque is_empty (expect True): {}".format(deque.is_empty()))
    print("Deque size (expect 0): {}".format(len(deque)))
    print(SEP)
    print("Copy all data to Deque")
    array_to_deque(deque, source)
    print("Deque is_empty (expect False): {}".format(deque.is_empty()))
    print("Deque size (expect > 0): {}".format(len(deque)))
    print(SEP)
    print("Front of Deque (peek):")
    print(deque.peek_front())
    print(SEP)
    print("Rear of Deque (peek):")
    print(deque.peek_rear())
    print(SEP)
    print("Remove all elements from Deque")

    while not deque.is_empty():
        v = deque.remove_front()
        print(v)
        print()

    print(SEP)
    print("Deque is_empty (expect True): {}".format(deque.is_empty()))
    print("Deque size (expect 0): {}".format(len(deque)))
    print()
    return

# x = list(range(5))
# y = Stack()
# print(x)
# array_to_stack(y, x)
# stack_to_array(y, x)
# print(x)
# print(SEP)
# y = Queue()
# print(x)
# array_to_queue(y, x)
# queue_to_array(y, x)
# print(x)
# y = Priority_Queue()
# print(x)
# array_to_pq(y, x)
# pq_to_array(y, x)
# print(x)
