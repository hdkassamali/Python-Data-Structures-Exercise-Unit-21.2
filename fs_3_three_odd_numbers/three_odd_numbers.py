def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    sum_of_nums = 0

    for idx in range(0, len(nums) - 2):
        sum_of_nums = (nums[idx] + nums[idx + 1] + nums[idx + 2])
        if sum_of_nums % 2 == 1:
            return True
        else:
            sum_of_nums = 0
    return False
