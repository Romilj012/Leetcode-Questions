class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashtable = dict()
        # for i, num in enumerate(numbers):
        #     if target - num in hashtable:
        #         return [hashtable[target - num]+1, i+1]
        #     hashtable[numbers[i]] = i
        # return []
        l, r = 0, len(numbers)-1
        res = []
        for n in numbers:
            if numbers[l]+ numbers[r] < target:
                l = l+1
            if numbers[l] + numbers[r] > target:
                r = r-1
            if numbers[l]+ numbers[r] == target:
                res.extend([l+1, r+1])
                break
        return res

