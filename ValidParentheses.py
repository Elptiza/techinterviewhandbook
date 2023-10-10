# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets
# Open brackets must be closed in the correct order
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false

def isValid (s):
    dict_open_scob = ['(','{','[']
    dict_close_scob = [')', '}', ']']
    end_scob = []

    if len(s)%2 != 0 or len(s)==0 or s[0] in dict_close_scob:
        return False

    for i in range(len(s)):

        if s[i] in dict_open_scob:
            end = dict_close_scob[dict_open_scob.index(s[i])]
            end_scob.insert(0,end)
            print (end_scob)
        elif s[i] in dict_close_scob and len(end_scob) != 0:
            if s[i] == end_scob[0]:
                end_scob.pop(0)
            else :
                return print(False)
        else :
            return print(False)
    if len(end_scob) == 0:
        return print(True)
    else :
        return print(False)

# s = "{(})"
# isValid (s)
s ="(){}}{"
isValid(s)

