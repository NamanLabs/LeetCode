class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        # Nodes to be swapped
        first = head
        second = head.next
        
        # Swapping
        first.next = self.swapPairs(second.next)
        second.next = first
        
        # What was head.next is now the head of the swapped pair
        return second
