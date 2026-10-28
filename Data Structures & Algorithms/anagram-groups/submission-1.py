class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        while len(strs) > 1:
            first_str = strs[0]
            anagram_group = [first_str]
            new_strs = []
            for string in strs[1:]:
                if self.check_anagram(first_str, string):
                    anagram_group.append(string)
                else:
                    new_strs.append(string)
            ret.append(anagram_group)
            strs = new_strs
        if len(strs) == 1:
            ret.append(strs)
        return ret
    
    def check_anagram(self, a, b):
        if len(a) != len(b): return False

        counter_a = {}
        counter_b = {}
        for i in range(len(a)):
            counter_a[a[i]] = counter_a.get(a[i], 0) + 1
            counter_b[b[i]] = counter_b.get(b[i], 0) + 1
        return counter_a == counter_b