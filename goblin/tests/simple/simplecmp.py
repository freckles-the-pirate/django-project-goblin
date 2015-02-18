#!/usr/bin/env python

def _cmp_length(l1, l2):
    if (len(l1) == 0):
        l1 = [0]
    if (len(l2) == 0):
        l2 = [0]
    return (l1, l2)

def _pad(l1, l2):
    if (len(l1) > len(l2)):
        l2.extend([0]*(len(l1) - len(l2)))
    elif (len(l2) > len(l1)):
        l1.extend([0]*(len(l2) - len(l1)))
    return (l1, l2)

def eq(l1, l2):
    (l1, l2) = _pad(l1, l2)
    return l1 == l2

def lt(l1, l2):
    (l1, l2) = _pad(l1, l2)
    return l1 < l2

def gt(l1, l2):
    (l1, l2) = _pad(l1, l2)
    return l1 > l2

print eq([1, 2], [1, 2, 0])
print lt([1, 2], [1, 2, 3])
