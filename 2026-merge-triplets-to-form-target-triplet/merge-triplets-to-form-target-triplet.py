class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_a, max_b, max_c = 0, 0, 0
        target_a, target_b, target_c = target

        for triplet in triplets:
            a, b, c = triplet
            if a <= target_a and b <= target_b and c <= target_c:
                max_a = max(max_a, a)
                max_b = max(max_b, b)
                max_c = max(max_c, c)
        return [max_a, max_b, max_c] == [target_a, target_b, target_c]
            
        