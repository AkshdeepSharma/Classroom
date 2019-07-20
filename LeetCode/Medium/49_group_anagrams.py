class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            print(key)
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        return [groups[i] for i in groups]