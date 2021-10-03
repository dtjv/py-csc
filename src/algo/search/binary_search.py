def binary_search_iterative(target: int, nums: list[int]) -> int:
    s_idx = 0
    e_idx = len(nums) - 1

    while s_idx <= e_idx:
        mid = (e_idx - s_idx + 1) // 2 + s_idx

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            e_idx = mid - 1
        else:
            s_idx = mid + 1

    return -1


def binary_search_recursive(target: int, nums: list[int]) -> int:
    result = -1

    if len(nums) > 0:
        mid = len(nums) // 2

        if target < nums[mid]:
            result = binary_search_recursive(target, nums[:mid])
        elif target > nums[mid]:
            rc = binary_search_recursive(target, nums[mid + 1:])
            result = -1 if rc == -1 else mid + 1 + rc
        else:
            result = mid

    return result
