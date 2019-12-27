class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        begin, end = min(start, destination), max(start, destination)
        return min(sum(distance[begin:end]), sum(distance) - sum(distance[begin:end]))