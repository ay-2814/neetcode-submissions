class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # print(f"input: {numbers}")

        has_seen = set()
        result = []

        for i, num in enumerate(numbers):
            if (target-num) in has_seen:
                result.append(numbers.index(target-num)+1)
                result.append(numbers.index(num)+1)
            else:
                has_seen.add(num)
        
        return result

