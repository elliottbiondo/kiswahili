from nose.tools import assert_equal, with_setup, assert_raises

from parser import Verb, Verb_Components


def test_regular():

    verb = Verb("ruka", "jump")

    vc = Verb_Components(0, 0, 0, "present")
    assert_equal("ninaruka", verb.conjugate(vc))

    vc = Verb_Components(0, 0, 1, "past")
    assert_equal("tuliruka", verb.conjugate(vc))

    vc = Verb_Components(0, 1, 0, "future")
    assert_equal("utaruka", verb.conjugate(vc))

    vc = Verb_Components(0, 2, 1, "past-perfect")
    assert_equal("wameruka", verb.conjugate(vc))


def test_regular_negation():

    verb = Verb("ruka", "jump")

    vc = Verb_Components(1, 0, 0, "present")
    assert_equal("siruki", verb.conjugate(vc))

    vc = Verb_Components(1, 0, 1, "past")
    assert_equal("hatukuruka", verb.conjugate(vc))

    vc = Verb_Components(1, 1, 0, "future")
    assert_equal("hutaruka", verb.conjugate(vc))

    vc = Verb_Components(1, 2, 1, "past-perfect")
    assert_equal("hawajaruka", verb.conjugate(vc))

def test_regular_negation_arabic():

    verb = Verb("fikiri", "think")

    vc = Verb_Components(1, 0, 0, "present")
    assert_equal("sifikiri", verb.conjugate(vc))


