class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx< tx and sy<ty:
            if tx < ty:
                ty %= tx
            else:
                tx %= ty
        if sx == tx and ty >= sy:
            return (ty - sy) % tx == 0
        elif  sy == ty and tx >= sx:
            return (tx - sx) % ty == 0
        return False


        