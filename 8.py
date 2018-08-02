# June 4, 2018

"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be
decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001'
"""

mapping = dict((i + 1, chr(i + 97)) for i in range(26))

def decode(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1 + decode(s[1:])
    return 2 + decode(s[2:])


if __name__ == '__main__':
    codes = [
        '1',
        '111',
        '001',
        '101010',
        '923948701',
        '103741121834710278',
        '273401827340123470124710483710234',
        '70987102837401897412934712934712034712034713',
        '103741121042378107834102348712039417237870987000198237412349173',
    ]
    for code in codes:
        print(mapping)
        for ch in list(code):
            print(ch)
        if any(int(ch) not in mapping for ch in list(code)):
            raise ValueError('Illegal encoded value not in (1...26)')
        print(decode('111'))