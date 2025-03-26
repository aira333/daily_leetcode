# Merge K sorted lists

'''
at first glance, i thought oh just merging and sorting but sorting would
take O(nlogn) time. But we can do better than that. We can use a min heap

1. Create a min heap and insert the first element of all the k lists
2. Pop the top element of the heap and add it to the result list
3. Insert the next element of the list from which the element was popped
4. Repeat steps 2 and 3 until the heap is empty
5. Return the result list
'''
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2
        
        return dummy.next
