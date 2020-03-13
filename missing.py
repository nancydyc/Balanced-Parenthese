"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """

    # Sort the list
    # Start from the middle digit to check if it matches the index

    # If the digit is the same as the index, 
    # check the number after it until not match;
    # then the number unmatch minus 1 is the missing num.

    # If the digit is greater than it's index, a number is missing before it;
    # check the number before it until the number matches the index;
    # then the number plus 1 is the missing num

    nums.sort()

    check_digit = nums[len(nums)//2]

    order = (len(nums)-1)//2 + 1

    if max(nums) != max_num:
        print(max_num)

    elif check_digit == order:    
        for num in nums[order:]:
            if num != nums.index(num) + 1:
                print(num - 1)
                break

    else: 
        for num in nums[order-1::-1]:
            if num == nums.index(num) +1:
                print(num + 1)
                break

    # This solution assumes 1 is never missing  
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
