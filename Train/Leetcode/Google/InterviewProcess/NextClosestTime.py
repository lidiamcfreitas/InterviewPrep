# Author: Lidia Freitas
# Start date: 14:28 8-4-2018
# Finish date: idea 14:34 ; implementation 14:52

import math


class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hours, minutes = time.split(':')
        if len(hours) > 1:
            hours = [int(_) for _ in hours]
        else:
            hours = [0, int(hours)]

        if len(minutes) > 1:
            minutes = [int(_) for _ in minutes]
        else:
            minutes = [0, int(minutes)]

        digits_original = [int(_) for _ in time.replace(':', '')]

        minimum = min(digits_original)

        # minutes
        x = math.inf
        for digit in digits_original:
            if minutes[1] < digit < x:
                x = digit

        if x != math.inf:
            return "{}{}:{}{}".format(hours[0], hours[1], minutes[0], x)

        x = 6
        for digit in digits_original:
            if minutes[0] < digit < x:
                x = digit

        if x != 6:
            return "{}{}:{}{}".format(hours[0], hours[1], x, minimum)

        # hours
        for i in range(hours[0]*10 + hours[1] + 1, 24):
            dec = i // 10
            unit = i % 10
            if dec in digits_original and unit in digits_original:
                return "{}{}:{}{}".format(dec, unit, minimum, minimum)

        # next day
        return "{}{}:{}{}".format(minimum, minimum, minimum, minimum)


# test
a = Solution()
print(a.nextClosestTime(time="19:34"))  # 19:39
print(a.nextClosestTime(time="15:39"))  # 15:51
print(a.nextClosestTime(time="23:59"))  # 02:02
print(a.nextClosestTime(time="12:09"))  # 12:10
print(a.nextClosestTime(time="01:34"))  # 01:40

'''
19:39
15:51
23:62
12:10
01:40
'''
