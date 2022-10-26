def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a = len(s1)
    b = len(s2)
    c = len(s3)
    if a % 2 != 0:
        s1 = s1 + ", "
    else:
        s1 = ""
    if b % 2 != 0:
        s2 = s2 + ', '
    else:
        s2 = ""
    if c % 2 != 0:
        s3 = s3
    else:
        s3 = ''
    ans = '['+s1+s2+s3+']'

    return ans
print(main('11','225','333'))