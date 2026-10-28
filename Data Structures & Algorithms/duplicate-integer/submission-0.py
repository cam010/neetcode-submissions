class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        u_nums = {}
        for num in nums:
            if u_nums.get(num, False):
                return True
            u_nums[num] = True
        return False