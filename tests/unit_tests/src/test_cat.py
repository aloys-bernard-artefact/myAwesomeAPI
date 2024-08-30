# testing the class Cat methods

import pytest


def test_speak(_cat):
    assert _cat.speak() == "Meow"


def test_aging(_cat):
    _cat.aging()
    _cat.aging()
    assert _cat.age == 2


def test_sleep(_cat):
    _cat.sleep()
    assert _cat.asleep == True
