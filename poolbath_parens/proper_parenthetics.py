# -*- coding: utf-8 -*-

def parenthetic_checker(text):
    """
    Return 1 if the string is "open" (there are open parens that are not closed)
    Return 0 if the string is "balanced" (there are an equal number of open and
    closed parentheses in the string)
    Return -1 if the string is "broken" (a closing parens has not been proceeded
    by one that opens)
    """
    # everything begins in a state of balance
    open_p = 0
    for char in text:
        # find an open para, open para count increments
        if char == u'(':
            open_p += 1
        # find closed, decrement open_p unless it is already 0 (means broken)
        elif char == u')':
            if open_p > 0:
                open_p -= 1
            else:
                return -1
    # return 1 (int of true) if open_p hasn't been closed (>0), else return 0
    return int(open_p > 0)
