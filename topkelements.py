from collections import Counter
import heapq
def topKFrequent(self, nums, k): #O(nlog(n))
        res= []
        Hashmap = {}
        for el in nums:
            Hashmap[el] = Hashmap.get(el,0)+1
        sorted_elements = sorted(Hashmap.items(),key=lambda x:x[1],reverse=True)
        return [key for key,_ in sorted_elements[:k]]
 

def topKFrequent(self, nums, k): #O(nlog(k))
        freq_count = Counter(nums)  # Count occurrences
        return [key for key, _ in heapq.nlargest(k, freq_count.items(), key=lambda x: x[1])]

def topKFrequent(self,nums,k):
        freq_count = Counter(nums)
        min_heap = []
        for key,freq in freq_count:
              heapq.heappush(min_heap,(freq,key))
              if len(min_heap)>k:
                     heapq.heappop(min_heap)
        return [key for _,key in min_heap] 

