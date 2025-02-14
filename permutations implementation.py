#implement permutations as it is implemented in itertools module
def permutations(nums):
    def backtrack(nums, path):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            backtrack(nums[:i]+nums[i+1:], path+[nums[i]])
    res = []
    backtrack(nums, [])
    return res

print(permutations([1,2,3])) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
