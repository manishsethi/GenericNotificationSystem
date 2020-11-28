# -*- coding: utf-8 -*-

import pytest
from notification_system.skeleton import fib

__author__ = "Manish Sethi"
__copyright__ = "Manish Sethi"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
