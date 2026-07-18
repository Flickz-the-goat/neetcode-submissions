class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = -1
        l, r = 0, len(nums) - 1
        print("Target", target)
        while l < r:
            if nums[l] == target:
                i = l
                break
            elif nums[r] == target:
                i = r
                break

            m = (l + r) // 2
            print(l, m, r)
            print(nums[l], nums[m], nums[r])
            if nums[m] == target:
                i = m
                break
            if nums[m] > target:
                l = m + 1
            else:
                r = m - 1
            

        return i
