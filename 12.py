# June 8, 2018

"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s
and a set of all possible query strings, return all strings in the
set that have s as a prefix.

For example, given the query string 'de' and the set of strings
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data
structure to speed up queries.
"""

def autocomplete(query, strings):
    return [s for s in strings if s.startswith(query)]

if __name__ == '__main__':
    query = 'de'
    strings = ['dog', 'deer', 'deal']
    assert autocomplete(query, strings) == ['deer', 'deal']