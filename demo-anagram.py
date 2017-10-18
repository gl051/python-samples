#!/usr/bin/env python

"""
    Problem: Given two strings s and t, write a function to determine if t is
    an anagram of s.

    For example,
    s = "anagram", t = "nagaram", return true.
    s = "rat", t = "car", return false.
"""


def is_anagram(s, t):
    """
        Using an hash table, no sorting necessary. We iterate on the the two
        strings only, the time complexity is 2N -> N, but you need memory for
        the hash table.

        Returns true or false
    """
    ht = {}
    if (s is None) or (t is None) or (len(s) != len(t)):
        return False
    for c in s:
        times = ht.setdefault(c, 0)
        ht[c] = times + 1
    for c in t:
        if not ht.has_key(c):
            return False
        else:
            if ht[c] > 1:
                ht[c] = ht[c] - 1
            else:
                ht.pop(c)
    return ht.keys() == []
