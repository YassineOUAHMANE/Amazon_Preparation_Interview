class PriorityQueues:
    def __init__(self):
        self.heap = []
    def left_child(self,i:int) ->  int:
            return 2 * i + 1
    def right_child(self,i:int) -> int:
            return 2 * i + 2
    def parent(self,i:int) -> int:
          return  (i-1)//2
    def swap(self,i:int,j:int):
          if 0 <= i < len(self.heap) and 0 <= j < len(self.heap):
            self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
          else:
               raise IndexError("The indexes that you want to swap not exist in the heap")  
    def heap_up(self,i:int):
          if not self.heap[self.parent(i)] or not self.heap[i]:
                  return 
          while i > 0 and self.heap[self.parent(i)] >  self.heap[i]:
                  self.swap(self.parent(i),i)
                  i = self.heap[self.parent(i)]
    def heap_down(self,i:int):
          smallest = i
          left = self.left_child(i)
          right = self.right_child(i)
          if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                   smallest = left
          if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                   smallest = right
          if smallest!=i:
               self.swap(i,smallest)
               self.heap_down(smallest) 
    def remove_min(self) -> int:
         if not self.heap:
              raise IndexError("Priority Queue is empty")      
         min_element = self.heap[0]
         self.heap[0] = self.heap[-1]
         self.heap.pop()
         if self.heap:
            self.heap_down(0)
         return min_element
    def insert(self, value:int):
         self.heap.append(value)
         self.heap_up(len(self.heap)-1)
         

    


     
    