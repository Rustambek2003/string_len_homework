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
    s=[]
    a = len(s1)
    b = len(s2)
    c = len(s3)
    if a % 2 != 0:
        s += s1
    if b % 2 != 0:
        s += s2
    if c % 2 != 0:
        s += s3

    return s