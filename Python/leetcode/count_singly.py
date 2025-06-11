'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

def count_occurrences(head, K):
    current = head
    count = 0
    while current is not None:
        if current.data == K:
            count+=1
        current = current.next
    return count
