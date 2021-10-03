def quick_sort(nums: list[int] = []) -> list[int]:
    def qs(s_idx: int, e_idx: int, nums: list[int] = []) -> list[int]:
        if s_idx < e_idx:
            p_idx = partition(s_idx, e_idx, nums)

            qs(s_idx, p_idx - 1, nums)
            qs(p_idx + 1, e_idx, nums)

        return nums

    def partition(s_idx: int, e_idx: int, nums: list[int] = []) -> int:
        pivot = nums[e_idx]
        p_idx = s_idx

        for i in range(s_idx, e_idx):
            if (nums[i] <= pivot):
                nums[p_idx], nums[i] = nums[i], nums[p_idx]
                p_idx += 1

        nums[p_idx], nums[e_idx] = nums[e_idx], nums[p_idx]

        return p_idx

    return qs(0, len(nums) - 1, nums)
