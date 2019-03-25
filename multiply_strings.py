class Solution: #368ms
    def multiply(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        z = 0
        C = 0
        while i >= 0:
            j = len(num2) - 1
            c = 0
            tmp_z = 0
            tmp_s = ''
            while j >= 0:
                # print(num2[j], num1[i], c, tmp_z)
                tmpi_z = int(num2[j])*int(num1[i]) + c
                c = tmpi_z // 10
                tmp_z += (tmpi_z % 10) * 10**(len(num2)-1-j)
                tmp_s = str(tmpi_z % 10) + tmp_s
                j -= 1
                # print(num2[j], num1[i], c, tmp_z)
                # print("\n")
            # print("\n\n")
            if c != 0:
                tmp_z += c * 10**(len(str(tmp_z)))
                tmp_s = str(c) + tmp_s
            z += int(tmp_s) * 10**(len(num1)-1-i)
            i -= 1
        return str(z)