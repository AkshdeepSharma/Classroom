class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        jewels = set(J)
        for stone in S:
            if stone in jewels:
                count += 1
        return count

'''Java
class Solution {
    public int numJewelsInStones(String J, String S) {
        int count = 0;
        for (int i = 0; i < S.length(); i++) {
            if (J.contains(Character.toString(S.charAt(i))))
                count += 1;
        }
        return count;
    }
}
'''