class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p1 = 0
        out = []
        nums = sorted(nums)

        while p1 < len(nums) - 2:
            p2 = p1 + 1
            p3 = len(nums) - 1
            if p1 > 0 and nums[p1] == nums[p1-1]:
                p1 += 1
                continue

            while p2 < p3:
                if nums[p1] + nums[p2] + nums[p3] == 0:
                    out.append([nums[p1], nums[p2], nums[p3]])
                    p2 += 1 

                    while p2 < p3 and nums[p2] == nums[p2 - 1]:
                        p2 += 1

                elif nums[p1] + nums[p2] + nums[p3] < 0:
                    p2 += 1
                elif nums[p1] + nums[p2] + nums[p3] > 0:
                    p3 -= 1

            p1 += 1
        
        return out