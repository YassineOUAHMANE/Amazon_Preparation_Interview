class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def addtwonumbers(l1,l2):
    dummy = ListNode(0)
    node = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum = val1 + val2 + carry 
        carry = sum // 10
        node.next = ListNode(sum % 10)
        node = node.next 
        if l1:
            l1 = l1.next
        if l2 :
            l2 = l2.next 
        
    return dummy.next

   
    
        

