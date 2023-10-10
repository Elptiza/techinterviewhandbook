# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower()
    new_s = []
    for el in s:
        if (el >= 'a' and el <= 'z') or (el >= '0' and el <= '9'):
            new_s.append(el)
    print(new_s)
    for i in range(len(new_s)//2):
        if new_s[i] != new_s[len(new_s) - 1 - i]:
            return print(False)
    return print(True)

# s = "A man, a plan, a canal: Panama"
# isPalindrome(s)
# Output: true

# s = "race a car"
# isPalindrome(s)
# Output: false

s = " "
isPalindrome(s)
# Output: true