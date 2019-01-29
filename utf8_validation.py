class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        encoding = [str('{0:8b}'.format(i)) for i in data]
        encoding = [i.replace(' ','0') for i in encoding]
        i = 0
        print(encoding)
        while(True):
            if i >= len(encoding):
                break
            elif encoding[i][0] == '0':
                i += 1
            elif encoding[i][0:2] == '10':
                return False
            else:
                j=0
                while j < 8 and encoding[i][j] == '1':
                    j += 1
                if j > 4:
                    return False
                # j is number of bytes
                j -= 1
                i += 1
                while j != 0 and i < len(encoding):
                    if encoding[i][0:2] != '10':
                        return False
                    j -= 1
                    i += 1
                if j > 0:
                    return False
        return True