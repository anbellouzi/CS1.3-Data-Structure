#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    text = remove_special_char(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def remove_special_char(text):
    return ''.join(e for e in text if e.isalnum())


def is_palindrome_iterative(text):
    l = 0               # left side of text
    r = len(text)-1     # right side of text
    while r > l:        
        if (text[r].capitalize() != text[l].capitalize()): # check if left and right are not equal
            print("not palindrome") 
            return False
        r -= 1      # moving left
        l += 1      # moving right
    return True     # reached end this is polindrome


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if left == None: left = 0               # check if left is not set yet
    if right == None: right = len(text)-1   # check if right is not set yet

    if left > right:
        return True

    if text[left].capitalize() != text[right].capitalize():           # check if left and right are not squal
        return False
    
    left += 1
    right -= 1
    
    return is_palindrome_recursive(text, left, right)

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()