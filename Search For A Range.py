class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        
        while low <=high:
            mid = (low + high) // 2
            if nums[mid] == target:
                if mid == low:
                    return mid
                if nums[mid-1] != target:
                    return mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    def find_last_position(nums, target):
        low, high = 0, len(nums)-1
        
        while low <=high:
            mid = (low + high) // 2
            if nums[mid] == target:
                if mid == high:
                    return mid
                if nums[mid+1] != target:
                    return mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    i = find_first_position(nums, target)
    if i == -1:
    return [-1, -1]
    j = find_last_position(nums, target)
    
return [i, j]