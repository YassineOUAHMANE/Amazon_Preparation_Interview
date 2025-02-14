class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, array) -> ListNode:
    unique_element_array = set(array) # space storage
    dummy = ListNode(0)
    current = dummy 
    dummy.next = head
    while current.next!=None:
        if current.next.val in unique_element_array:
            current.next = current.next.next
        else:
            current = current.next
    return  dummy.next

# let's write another version with prev and current pointers
def removeElements(head: ListNode, array) -> ListNode:
    unique_element_array = set(array)  # space storage
    dummy = ListNode(0)
    dummy.next = head
    current = head
    prev = dummy 
    while current!=None:
        if current.val in unique_element_array:
            prev.next = current.next
            current = current.next
        else:
            prev =current
            current = current.next
    return dummy.next    

def binary_search(array,val):
    left = 0
    right = len(array)-1
    while left<=right:
        mid = (left+right)//2
        if array[mid]==val:
            return True
        elif array[mid]>val:
            right = mid-1
        else:
            left = mid+1
    return False        


# let's write another version with prev and current pointers and binary search
# we can use binary search to find the element in the array
def removeElements(head: ListNode, array) -> ListNode:
    array.sort() # sort the array complexity O(nlogn)
    dummy = ListNode(0)
    dummy.next = head
    current = head
    prev = dummy 
    while current!=None:
        if binary_search(array,current.val):  #log(n)
            prev.next = current.next
            current = current.next
        else:
            prev =current
            current = current.next
    return dummy.next      
    

