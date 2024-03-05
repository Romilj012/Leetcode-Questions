class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtracking(current, position, target):
            if target == 0:
                result.append(current.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(position, len(candidates)):
                if candidates[i] == prev:
                    continue
                current.append(candidates[i])
                backtracking(current, i+1, target - candidates[i])
                current.pop()
                prev = candidates[i]
        backtracking([], 0, target)
        return result