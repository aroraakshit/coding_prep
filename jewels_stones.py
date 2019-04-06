class Solution: #40ms
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = {i:S.count(i) for i in S}
        S_ = set(S)
        J_ = set(J)
        S_J = S_ & J_
        return sum([c[i] for i in list(S_J)])