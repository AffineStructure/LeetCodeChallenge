class Solution:
    def isHappy(self, n: int) -> bool:
        truthSet = set()
        val = n
        while val not in truthSet and val != 1:
            truthSet.add(val)
            val = sum(int(i)**2 for i in list(str(val)))
        return True if val == 1 else False