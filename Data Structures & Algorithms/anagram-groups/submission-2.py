class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        while len(strs) > 1:
            first_str = strs[0]
            counter_first_string = self.create_counter(first_str) 
            anagram_group = [first_str]
            new_strs = []
            for string in strs[1:]:
                # Make this quicker by not having to make a
                # counter for first_str to check anagram each time.
                if self.check_anagram(string, counter_first_string):
                    anagram_group.append(string)
                else:
                    new_strs.append(string)
            ret.append(anagram_group)
            strs = new_strs
        if len(strs) == 1:
            ret.append(strs)
        return ret

    def create_counter(self, string):
        counter = {}
        for i in range(len(string)):
            counter[string[i]] = counter.get(string[i], 0) + 1
        return counter
    
    def check_anagram(self, a, counter_b):
        counter_a = self.create_counter(a)
        return counter_a == counter_b