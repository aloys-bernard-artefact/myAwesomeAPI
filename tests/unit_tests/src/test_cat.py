# testing the class Cat methods

import pytest


def test_speak(cat):
    assert cat.speak() == "Meow"


def test_aging(cat):
    cat.aging()
    cat.aging()
    assert cat.age == 2


def test_sleep(cat):
    cat.sleep()
    assert cat.asleep == True
