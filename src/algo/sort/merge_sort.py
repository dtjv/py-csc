def merge_sort(nums: list[int]) -> list[int]:
    def merge(a: list[int], b: list[int]) -> list[int]:
        result: list[int] = []

        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        if i < len(a):
            result += a[i:]

        if j < len(b):
            result += b[j:]

        return result

    """
    Returns a new list of 'nums' sorted in acending order.
    """
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))
