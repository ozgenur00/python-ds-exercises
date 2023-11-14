def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    if not nums:
        return None
    
    freq_dict = {}

    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
        
        max_count = max(freq_dict.values())
        for num in nums:
            if freq_dict[num] == max_count:
                return num
    