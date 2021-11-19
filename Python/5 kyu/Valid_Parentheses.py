'''
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
'''


def valid_parentheses(string):
    opens = 0
    for i in string:
        if opens < 0:
            return False

        if i == '(':
            opens += 1
        elif i == ')':
            opens -= 1

    return opens == 0
