# -*- coding: utf-8 -*-
"""Tests for proper_parenthetics.py"""
from proper_parenthetics import parenthetic_checker


def test_balanced_returns_zero():
    result = parenthetic_checker(u'((()))')
    assert result == 0


def test_unbalanced_returns_neg_1():
    result = parenthetic_checker(u'((())))')
    assert result == -1


def test_open_returns_one():
    result = parenthetic_checker(u'(((()))')
    assert result == 1


def test_extra_chars_do_not_matter_balanced():
    result = parenthetic_checker(u'(dsfdf)()()((23f3423r32))')
    assert result == 0


def test_extra_chars_do_not_matter_broken():
    result = parenthetic_checker(u'(dsfdf))()()((23f3423r32))')
                                        # ^
    assert result == -1


def test_extra_chars_do_not_matter_open():
    result = parenthetic_checker(u'(dsfdf)(()()((23f3423r32))')
                                        # ^
    assert result == 1


def test_assignment_example():
    result = parenthetic_checker(u')))(((')
    assert result == -1
