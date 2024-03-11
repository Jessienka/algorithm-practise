# Edge check1: same length but different appearing times of each char
# Edge check2: different length but same char


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)