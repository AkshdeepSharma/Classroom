class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        date = date.split('-')
        year, month, day, leap = int(date[0]), int(date[1]), int(date[2]), False
        months = {
            2: 31,
            3: 59,
            4: 90,
            5: 120,
            6: 151,
            7: 181,
            8: 212,
            9: 243,
            10: 273,
            11: 304,
            12: 334
        }
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: #is leap year
            leap = True
        if month == 1:
            return day
        else:
            if leap and month > 2:
                return months[month] + day + 1
            else:
                return months[month] + day