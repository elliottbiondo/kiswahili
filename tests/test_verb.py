from nose.tools import assert_equal, with_setup, assert_raises

from kiswahili.parser import KisVerb, VerbComponents


def test_verb_components():

    vc = VerbComponents(0, 1, 0, "present")

    assert_equal("affirmative", vc.polarity)
    assert_equal("second", vc.person)
    assert_equal("singular", vc.plurality)
    assert_equal("present", vc.tense)

    assert_equal(0, vc.polarity_idx)
    assert_equal(1, vc.person_idx)
    assert_equal(0, vc.plurality_idx)
    assert_equal(2, vc.tense_idx)

    assert_equal("affirmative, second person, singular, present tense", str(vc))


def test_regular():

    verb = KisVerb("ruka", "jump")

    vc = VerbComponents(0, 0, 0, "present")
    assert_equal("ninaruka", verb.conjugate(vc))

    vc = VerbComponents(0, 0, 1, "past")
    assert_equal("tuliruka", verb.conjugate(vc))

    vc = VerbComponents(0, 1, 0, "future")
    assert_equal("utaruka", verb.conjugate(vc))

    vc = VerbComponents(0, 2, 1, "past-perfect")
    assert_equal("wameruka", verb.conjugate(vc))


def test_regular_negation():

    verb = KisVerb("ruka", "jump")

    vc = VerbComponents(1, 0, 0, "present")
    assert_equal("siruki", verb.conjugate(vc))

    vc = VerbComponents(1, 0, 1, "past")
    assert_equal("hatukuruka", verb.conjugate(vc))

    vc = VerbComponents(1, 1, 0, "future")
    assert_equal("hutaruka", verb.conjugate(vc))

    vc = VerbComponents(1, 2, 1, "past-perfect")
    assert_equal("hawajaruka", verb.conjugate(vc))

def test_regular_negation_arabic():

    verb = KisVerb("fikiri", "think")

    vc = VerbComponents(1, 0, 0, "present")
    assert_equal("sifikiri", verb.conjugate(vc))


