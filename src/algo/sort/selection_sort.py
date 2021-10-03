def selection_sort(nums: list[int] = []) -> list[int]:
    if len(nums) > 1:
        for i in range(len(nums)):
            j = i + 1
            mv_idx = i

            while j < len(nums):
                if nums[j] < nums[mv_idx]:
                    mv_idx = j
                j += 1

            nums[i], nums[mv_idx] = nums[mv_idx], nums[i]

    return nums
