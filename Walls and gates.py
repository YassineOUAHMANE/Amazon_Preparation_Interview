from typing import List
from collections import deque
class Solution:        #Implementing a DFS solution O((n*m)^2) time complexity and  space complexity O(m*n)
    def gates_walls_DFS(self,grid:List[List[float]]) -> List[List[float]]:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r:int,c:int,distance:int):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r,c) in visited or grid[r][c] < distance:
                return 
            visited.add((r,c)) 
            grid[r][c] = distance     
            dfs(r+1,c,distance+1)
            dfs(r-1,c,distance+1)
            dfs(r,c+1,distance+1)
            dfs(r,c-1,distance+1)

        for r in range(rows):
            for c in range(cols):
                visited = set()
                if grid[r][c] == 0:
                    dfs(r,c,0)
        return grid                    

#solution = Solution()
#print(solution.gates_walls_DFS([
#  [float('inf'), -1, 0, float('inf')],
#  [float('inf'), float('inf'), float('inf'), -1],
#  [float('inf'), -1, float('inf'), -1],
#  [0, -1, float('inf'), float('inf')]
#]
#))
            
              

          
#class treenode:
#    def __init__(self,val,left=None,right=None):
#        self.val = val
#        self.left = left
#        self.right = right
#
#
#    @staticmethod
#    def BFS(root):
#        if not root:
#            return root
#        result = []    
#        queue = []
#        queue.append(root)
#        while queue:
#            n = len(queue)
#            for _ in range(n):
#                node = queue.pop(0)
#                result.append(node.val)
#                if node.left:
#                  queue.append(node.left)
#                if node.right:
#                  queue.append(node.right)   
#        return result               
#
#root = treenode(1)
#root.right = treenode(2)
#root.left = treenode(3)
#root.left.left = treenode(4)
#root.right.right = treenode(5)
#root.right.right.right = treenode(6)
#
#
#print(*treenode.BFS(root))  # * unpack the elements


       #This solution is O(m*n) time complexity and O(n*m) space complexity      
    def gates_walls_BFS(self,grid:List[List[float]]) -> List[List[float]]:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        #Enqueing all the gates
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c,0)) #Append the position of the gate and the distance
        while queue:
            r,c,dist = queue.popleft()
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]: # All four directions
                nr ,nc = r + dr , c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == float('inf'):
                    grid[nr][nc] = dist + 1 
                    queue.append((nr,nc,dist+1))
        return grid            


                    





    



            
                         


