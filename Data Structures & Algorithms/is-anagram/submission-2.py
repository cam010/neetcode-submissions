class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if set(s) != set(t): return False
        c_1 = {}
        c_2 = {}
        for char in s:
            if c_1.get(char, False):
                c_1[char] += 1
            else:
                c_1[char] = 1
        for char in t:
            if c_2.get(char, False):
                c_2[char] += 1
            else:
                c_2[char] = 1
        print(c_1, c_2)
        for key in list(c_1.keys()):
            if c_2.get(key, False):
                if c_1[key] != c_2[key]:
                    return False
            else:
                return False
        return True
