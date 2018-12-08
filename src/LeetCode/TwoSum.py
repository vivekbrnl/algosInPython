class Solution:
    def twoSum(self, nums, target):
        nums_index = [(v, index) for index, v in enumerate(nums)]
        print(nums_index)
        nums_index.sort()
        print(nums_index)
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1


print(Solution().twoSum([3, 2, 4, 3], 6))
