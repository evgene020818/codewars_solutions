'''
Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first.
'''


def high_and_low(numbers):
    nums_arr = numbers.split(' ')
    nums_arr = [int(i) for i in nums_arr]
    return str(max(nums_arr)) + ' ' + str(min(nums_arr))