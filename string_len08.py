def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    ans = ''
    n = len(s)
    if n%2 != 0:
        ans += s[s//2]
    else:
        ans += s[(s//2)-1:s//2+1]

    return ans
