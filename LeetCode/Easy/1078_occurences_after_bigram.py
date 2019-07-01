class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text_list = list(text.split(" "))
        res = []
        for i in range(1, len(text_list)):
            if i != len(text_list) - 1 and text_list[i] == second and text_list[i - 1] == first:
                res.append(text_list[i + 1])
        return res