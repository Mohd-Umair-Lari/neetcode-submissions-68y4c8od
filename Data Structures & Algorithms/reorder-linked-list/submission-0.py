# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if(head == None): return
#finding middle and end of LL with fast n slow ptrs.
        s = head
        f = head
        while(f != None and f.next != None):
            s = s.next
            f = f.next.next

#split list and keep mid next
        second = s.next
        s.next = None

#Reversing second half of LL
        curr = second
        prev = None
        while(curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
#inplace ordering
        first, second = head, prev
        while(second):
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
            