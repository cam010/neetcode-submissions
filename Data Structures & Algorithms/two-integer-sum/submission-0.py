class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            target_j = target - nums[i]
            print(hashmap, target_j)
            if hashmap.get(target_j, None) != None :
                j = hashmap[target_j]
                # i always > j
                return [j, i]
            else:
                hashmap[nums[i]] = i