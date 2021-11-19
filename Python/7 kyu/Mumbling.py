'''
Examples:
    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''


def accum(s):
    result = []
    for i in range(len(s)):
        result.append((s[i] * (i + 1)).capitalize())
    return '-'.join(result)