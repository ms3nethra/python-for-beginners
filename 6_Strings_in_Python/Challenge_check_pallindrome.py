"""challenge : find if string is pallindrome
* A string is said to be pallindrome if the reverse of the string is the same as string.
* for example, "radar" is a palindrome, but "radix" is not a palindrome
"""

s = "rahul"

#rev is: s[::-1], using string slicing

if s == s[::-1]:
    print("yes")
else:
    print("No")