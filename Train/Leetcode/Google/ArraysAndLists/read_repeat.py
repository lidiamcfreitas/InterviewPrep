# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        res_list = []

        read4_out = read4(buf)
        to_read = n

        while read4_out > 0 and to_read > 0:

            for i in range(min(read4_out, to_read)):
                res_list.append(buf[i])

            to_read -= read4_out
            read4_out = read4(buf)

        del buf[:]

        for c in res_list:
            buf.append(c)

        return len(buf)