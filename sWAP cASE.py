You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2


def swap_case(s):
    a = list(s)
    for i in range(len(s)):
        if a[i].isupper():
            a[i] = s[i].lower()
        else:
            a[i] = s[i].upper()
    return ''.join(a)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
