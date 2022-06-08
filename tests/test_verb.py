from nose.tools import assert_equal, with_setup, assert_raises

from kiswahili.verb import VerbComponents, KisVerb, EngVerb

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


def test_kis_regular():

    verb = KisVerb("ruka", "jump")

    vc = VerbComponents(0, 0, 0, "present")
    assert_equal("ninaruka", verb.conjugate(vc))

    vc = VerbComponents(0, 0, 1, "past")
    assert_equal("tuliruka", verb.conjugate(vc))

    vc = VerbComponents(0, 1, 0, "future")
    assert_equal("utaruka", verb.conjugate(vc))

    vc = VerbComponents(0, 2, 1, "present-perfect")
    assert_equal("wameruka", verb.conjugate(vc))


def test_kis_regular_negation():

    verb = KisVerb("ruka", "jump")

    vc = VerbComponents(1, 0, 0, "present")
    assert_equal("siruki", verb.conjugate(vc))

    vc = VerbComponents(1, 0, 1, "past")
    assert_equal("hatukuruka", verb.conjugate(vc))

    vc = VerbComponents(1, 1, 0, "future")
    assert_equal("hutaruka", verb.conjugate(vc))

    vc = VerbComponents(1, 2, 1, "present-perfect")
    assert_equal("hawajaruka", verb.conjugate(vc))

def test_kis_regular_negation_arabic():

    verb = KisVerb("fikiri", "think")

    vc = VerbComponents(1, 0, 0, "present")
    assert_equal("sifikiri", verb.conjugate(vc))

def test_eng():

    n = EngVerb("break")

    # present continuous
    assert_equal("I am breaking", n.conjugate(VerbComponents(0, 0, 0, "present")))
    assert_equal("I am not breaking", n.conjugate(VerbComponents(1, 0, 0, "present")))
    assert_equal("You are breaking", n.conjugate(VerbComponents(0, 1, 0, "present")))
    assert_equal("You are not breaking", n.conjugate(VerbComponents(1, 1, 0, "present")))
    assert_equal("S/he is breaking", n.conjugate(VerbComponents(0, 2, 0, "present")))
    assert_equal("S/he is not breaking", n.conjugate(VerbComponents(1, 2, 0, "present")))
    assert_equal("We are breaking", n.conjugate(VerbComponents(0, 0, 1, "present")))
    assert_equal("We are not breaking", n.conjugate(VerbComponents(1, 0, 1, "present")))
    assert_equal("You all are breaking", n.conjugate(VerbComponents(0, 1, 1, "present")))
    assert_equal("You all are not breaking", n.conjugate(VerbComponents(1, 1, 1, "present")))
    assert_equal("They are breaking", n.conjugate(VerbComponents(0, 2, 1, "present")))
    assert_equal("They are not breaking", n.conjugate(VerbComponents(1, 2, 1, "present")))

    # simple past
    assert_equal("I broke", n.conjugate(VerbComponents(0, 0, 0, "past")))
    assert_equal("I did not break", n.conjugate(VerbComponents(1, 0, 0, "past")))
    assert_equal("You broke", n.conjugate(VerbComponents(0, 1, 0, "past")))
    assert_equal("You did not break", n.conjugate(VerbComponents(1, 1, 0, "past")))
    assert_equal("S/he broke", n.conjugate(VerbComponents(0, 2, 0, "past")))
    assert_equal("S/he did not break", n.conjugate(VerbComponents(1, 2, 0, "past")))
    assert_equal("We broke", n.conjugate(VerbComponents(0, 0, 1, "past")))
    assert_equal("We did not break", n.conjugate(VerbComponents(1, 0, 1, "past")))
    assert_equal("You all broke", n.conjugate(VerbComponents(0, 1, 1, "past")))
    assert_equal("You all did not break", n.conjugate(VerbComponents(1, 1, 1, "past")))
    assert_equal("They broke", n.conjugate(VerbComponents(0, 2, 1, "past")))
    assert_equal("They did not break", n.conjugate(VerbComponents(1, 2, 1, "past")))

    # simple future
    assert_equal("I will break", n.conjugate(VerbComponents(0, 0, 0, "future")))
    assert_equal("I will not break", n.conjugate(VerbComponents(1, 0, 0, "future")))
    assert_equal("You will break", n.conjugate(VerbComponents(0, 1, 0, "future")))
    assert_equal("You will not break", n.conjugate(VerbComponents(1, 1, 0, "future")))
    assert_equal("S/he will break", n.conjugate(VerbComponents(0, 2, 0, "future")))
    assert_equal("S/he will not break", n.conjugate(VerbComponents(1, 2, 0, "future")))
    assert_equal("We will break", n.conjugate(VerbComponents(0, 0, 1, "future")))
    assert_equal("We will not break", n.conjugate(VerbComponents(1, 0, 1, "future")))
    assert_equal("You all will break", n.conjugate(VerbComponents(0, 1, 1, "future")))
    assert_equal("You all will not break", n.conjugate(VerbComponents(1, 1, 1, "future")))
    assert_equal("They will break", n.conjugate(VerbComponents(0, 2, 1, "future")))
    assert_equal("They will not break", n.conjugate(VerbComponents(1, 2, 1, "future")))

    # present-perfect
    assert_equal("I have broken", n.conjugate(VerbComponents(0, 0, 0, "present-perfect")))
    assert_equal("I have not broken", n.conjugate(VerbComponents(1, 0, 0, "present-perfect")))
    assert_equal("You have broken", n.conjugate(VerbComponents(0, 1, 0, "present-perfect")))
    assert_equal("You have not broken", n.conjugate(VerbComponents(1, 1, 0, "present-perfect")))
    assert_equal("S/he has broken", n.conjugate(VerbComponents(0, 2, 0, "present-perfect")))
    assert_equal("S/he has not broken", n.conjugate(VerbComponents(1, 2, 0, "present-perfect")))
    assert_equal("We have broken", n.conjugate(VerbComponents(0, 0, 1, "present-perfect")))
    assert_equal("We have not broken", n.conjugate(VerbComponents(1, 0, 1, "present-perfect")))
    assert_equal("You all have broken", n.conjugate(VerbComponents(0, 1, 1, "present-perfect")))
    assert_equal("You all have not broken", n.conjugate(VerbComponents(1, 1, 1, "present-perfect")))
    assert_equal("They have broken", n.conjugate(VerbComponents(0, 2, 1, "present-perfect")))
    assert_equal("They have not broken", n.conjugate(VerbComponents(1, 2, 1, "present-perfect")))
    
