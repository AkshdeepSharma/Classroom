class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """

        def find_median(count):
            total_sum = sum(count)
            num = []
            if total_sum % 2 == 0:
                half_sum = total_sum // 2
            else:
                half_sum = total_sum / 2
            for i in range(len(count)):
                total_sum -= count[i]
                if total_sum == half_sum:
                    num.append(i)
                elif total_sum < half_sum:
                    num.append(i)
                    break
            return float(sum(num)) / len(num)

        def find_mode(count):
            return count.index(max(count))

        def find_mean(count):
            mean, total_nums = 0, 0
            for i, val in enumerate(count):
                mean += i * val
                if val != 0:
                    total_nums += val
            return float(mean) / total_nums

        def find_min(count):
            for i in range(len(count)):
                if count[i] != 0:
                    return i

        def find_max(count):
            for i in reversed(range(len(count))):
                if count[i] != 0:
                    return i

        return [find_min(count), find_max(count), find_mean(count), find_median(count), find_mode(count)]