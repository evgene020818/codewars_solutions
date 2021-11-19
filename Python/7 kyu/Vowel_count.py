'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    for i in list(vowels):
        string_ = string_.replace(i, '')
    return string_