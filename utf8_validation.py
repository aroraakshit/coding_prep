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

# can also be achieved by bit manipulation! 44ms:

# class Solution:
#     def validUtf8(self, data):
#         """
#         :type data: List[int]
#         :rtype: bool
#         """

#         # Number of bytes in the current UTF-8 character
#         n_bytes = 0

#         # Mask to check if the most significant bit (8th bit from the left) is set or not
#         mask1 = 1 << 7

#         # Mask to check if the second most significant bit is set or not
#         mask2 = 1 << 6
#         for num in data:

#             # Get the number of set most significant bits in the byte if
#             # this is the starting byte of an UTF-8 character.
#             mask = 1 << 7
#             if n_bytes == 0:
#                 while mask & num:
#                     n_bytes += 1
#                     mask = mask >> 1

#                 # 1 byte characters
#                 if n_bytes == 0:
#                     continue

#                 # Invalid scenarios according to the rules of the problem.
#                 if n_bytes == 1 or n_bytes > 4:
#                     return False
#             else:

#                 # If this byte is a part of an existing UTF-8 character, then we
#                 # simply have to look at the two most significant bits and we make
#                 # use of the masks we defined before.
#                 if not (num & mask1 and not (num & mask2)):
#                     return False
#             n_bytes -= 1
#         return n_bytes == 0     
