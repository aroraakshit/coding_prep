class Solution: # 36ms
    def validIPAddress(self, IP: str) -> str:
        if len(IP.split('.')) == 4 :
            lst = IP.split('.')
            vocab = '1234567890'
            for i in lst:
                for j in i:
                    if j not in vocab:
                        return "Neither"
                if i=="" or (len(i) > 1 and i[0] == '0') or eval(i) < 0 or eval(i) > 255: # leading zero
                    return "Neither"
            return "IPv4"
        elif len(IP.split(':')) == 8:
            lst = IP.split(':')
            vocab = 'abcdef1234567890'
            lst = [i.lower() for i in lst]
            for i in lst:
                if i == '' or len(i)>4:
                    return "Neither"
                for j in i:
                    if j not in vocab:
                        return "Neither"
            return "IPv6"
        return "Neither"