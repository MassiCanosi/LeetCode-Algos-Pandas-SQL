class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        node = 0
        next_node = 0
        _len = len(nums)

        while next_node < _len:
            while next_node < _len and nums[node] == nums[next_node]:
                next_node += 1
            if next_node >= _len:
                break
            
            node += 1
            nums[node] = nums[next_node]

        k = len(set(nums))

        return k