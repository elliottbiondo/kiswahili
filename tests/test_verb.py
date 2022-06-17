from nose.tools import assert_equal, assert_not_equal, assert_raises

from verb import VerbComponents, KisVerb, EngVerb

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

    verb = KisVerb("ruka", [EngVerb("jump")])

    vc = VerbComponents(0, 0, 0, "present")
    assert_equal("ninaruka", verb.conjugate(vc))

    vc = VerbComponents(0, 0, 1, "past")
    assert_equal("tuliruka", verb.conjugate(vc))

    vc = VerbComponents(0, 1, 0, "future")
    assert_equal("utaruka", verb.conjugate(vc))

    vc = VerbComponents(0, 2, 1, "present-perfect")
    assert_equal("wameruka", verb.conjugate(vc))


def test_kis_regular_negation():

    verb = KisVerb("ruka", [EngVerb("jump")])

    vc = VerbComponents(1, 0, 0, "present")
    assert_equal("siruki", verb.conjugate(vc))

    vc = VerbComponents(1, 0, 1, "past")
    assert_equal("hatukuruka", verb.conjugate(vc))

    vc = VerbComponents(1, 1, 0, "future")
    assert_equal("hutaruka", verb.conjugate(vc))

    vc = VerbComponents(1, 2, 1, "present-perfect")
    assert_equal("hawajaruka", verb.conjugate(vc))

def test_kis_regular_negation_arabic():

    verb = KisVerb("fikiri", [EngVerb("think")])

    vc = VerbComponents(1, 0, 0, "present")
    assert_equal("sifikiri", verb.conjugate(vc))

def test_eng_simple():

    ev = EngVerb("break")

    assert_equal("break", str(ev))
    assert_equal(EngVerb("break"), ev)
    assert_not_equal("break", ev)

    # present continuous
    assert_equal("I am breaking", ev.conjugate(VerbComponents(0, 0, 0, "present")))
    assert_equal("I am not breaking", ev.conjugate(VerbComponents(1, 0, 0, "present")))
    assert_equal("You are breaking", ev.conjugate(VerbComponents(0, 1, 0, "present")))
    assert_equal("You are not breaking", ev.conjugate(VerbComponents(1, 1, 0, "present")))
    assert_equal("S/he is breaking", ev.conjugate(VerbComponents(0, 2, 0, "present")))
    assert_equal("S/he is not breaking", ev.conjugate(VerbComponents(1, 2, 0, "present")))
    assert_equal("We are breaking", ev.conjugate(VerbComponents(0, 0, 1, "present")))
    assert_equal("We are not breaking", ev.conjugate(VerbComponents(1, 0, 1, "present")))
    assert_equal("You all are breaking", ev.conjugate(VerbComponents(0, 1, 1, "present")))
    assert_equal("You all are not breaking", ev.conjugate(VerbComponents(1, 1, 1, "present")))
    assert_equal("They are breaking", ev.conjugate(VerbComponents(0, 2, 1, "present")))
    assert_equal("They are not breaking", ev.conjugate(VerbComponents(1, 2, 1, "present")))

    # simple past
    assert_equal("I broke", ev.conjugate(VerbComponents(0, 0, 0, "past")))
    assert_equal("I did not break", ev.conjugate(VerbComponents(1, 0, 0, "past")))
    assert_equal("You broke", ev.conjugate(VerbComponents(0, 1, 0, "past")))
    assert_equal("You did not break", ev.conjugate(VerbComponents(1, 1, 0, "past")))
    assert_equal("S/he broke", ev.conjugate(VerbComponents(0, 2, 0, "past")))
    assert_equal("S/he did not break", ev.conjugate(VerbComponents(1, 2, 0, "past")))
    assert_equal("We broke", ev.conjugate(VerbComponents(0, 0, 1, "past")))
    assert_equal("We did not break", ev.conjugate(VerbComponents(1, 0, 1, "past")))
    assert_equal("You all broke", ev.conjugate(VerbComponents(0, 1, 1, "past")))
    assert_equal("You all did not break", ev.conjugate(VerbComponents(1, 1, 1, "past")))
    assert_equal("They broke", ev.conjugate(VerbComponents(0, 2, 1, "past")))
    assert_equal("They did not break", ev.conjugate(VerbComponents(1, 2, 1, "past")))

    # simple future
    assert_equal("I will break", ev.conjugate(VerbComponents(0, 0, 0, "future")))
    assert_equal("I will not break", ev.conjugate(VerbComponents(1, 0, 0, "future")))
    assert_equal("You will break", ev.conjugate(VerbComponents(0, 1, 0, "future")))
    assert_equal("You will not break", ev.conjugate(VerbComponents(1, 1, 0, "future")))
    assert_equal("S/he will break", ev.conjugate(VerbComponents(0, 2, 0, "future")))
    assert_equal("S/he will not break", ev.conjugate(VerbComponents(1, 2, 0, "future")))
    assert_equal("We will break", ev.conjugate(VerbComponents(0, 0, 1, "future")))
    assert_equal("We will not break", ev.conjugate(VerbComponents(1, 0, 1, "future")))
    assert_equal("You all will break", ev.conjugate(VerbComponents(0, 1, 1, "future")))
    assert_equal("You all will not break", ev.conjugate(VerbComponents(1, 1, 1, "future")))
    assert_equal("They will break", ev.conjugate(VerbComponents(0, 2, 1, "future")))
    assert_equal("They will not break", ev.conjugate(VerbComponents(1, 2, 1, "future")))

    # present-perfect
    assert_equal("I have broken", ev.conjugate(VerbComponents(0, 0, 0, "present-perfect")))
    assert_equal("I have not broken", ev.conjugate(VerbComponents(1, 0, 0, "present-perfect")))
    assert_equal("You have broken", ev.conjugate(VerbComponents(0, 1, 0, "present-perfect")))
    assert_equal("You have not broken", ev.conjugate(VerbComponents(1, 1, 0, "present-perfect")))
    assert_equal("S/he has broken", ev.conjugate(VerbComponents(0, 2, 0, "present-perfect")))
    assert_equal("S/he has not broken", ev.conjugate(VerbComponents(1, 2, 0, "present-perfect")))
    assert_equal("We have broken", ev.conjugate(VerbComponents(0, 0, 1, "present-perfect")))
    assert_equal("We have not broken", ev.conjugate(VerbComponents(1, 0, 1, "present-perfect")))
    assert_equal("You all have broken", ev.conjugate(VerbComponents(0, 1, 1, "present-perfect")))
    assert_equal("You all have not broken", ev.conjugate(VerbComponents(1, 1, 1, "present-perfect")))
    assert_equal("They have broken", ev.conjugate(VerbComponents(0, 2, 1, "present-perfect")))
    assert_equal("They have not broken", ev.conjugate(VerbComponents(1, 2, 1, "present-perfect")))

def test_eng_compound():

    # Regular compound verb

    ev = EngVerb("throw", compound_component="out")

    assert_equal("throw out", str(ev))
    assert_equal(EngVerb("throw", compound_component="out"), ev)
    assert_not_equal("throw out", ev)

    # present continuous
    assert_equal("I am throwing out", ev.conjugate(VerbComponents(0, 0, 0, "present")))
    assert_equal("I am not throwing out", ev.conjugate(VerbComponents(1, 0, 0, "present")))
    assert_equal("You are throwing out", ev.conjugate(VerbComponents(0, 1, 0, "present")))
    assert_equal("You are not throwing out", ev.conjugate(VerbComponents(1, 1, 0, "present")))
    assert_equal("S/he is throwing out", ev.conjugate(VerbComponents(0, 2, 0, "present")))
    assert_equal("S/he is not throwing out", ev.conjugate(VerbComponents(1, 2, 0, "present")))
    assert_equal("We are throwing out", ev.conjugate(VerbComponents(0, 0, 1, "present")))
    assert_equal("We are not throwing out", ev.conjugate(VerbComponents(1, 0, 1, "present")))
    assert_equal("You all are throwing out", ev.conjugate(VerbComponents(0, 1, 1, "present")))
    assert_equal("You all are not throwing out", ev.conjugate(VerbComponents(1, 1, 1, "present")))
    assert_equal("They are throwing out", ev.conjugate(VerbComponents(0, 2, 1, "present")))
    assert_equal("They are not throwing out", ev.conjugate(VerbComponents(1, 2, 1, "present")))

    # simple past
    assert_equal("I threw out", ev.conjugate(VerbComponents(0, 0, 0, "past")))
    assert_equal("I did not throw out", ev.conjugate(VerbComponents(1, 0, 0, "past")))
    assert_equal("You threw out", ev.conjugate(VerbComponents(0, 1, 0, "past")))
    assert_equal("You did not throw out", ev.conjugate(VerbComponents(1, 1, 0, "past")))
    assert_equal("S/he threw out", ev.conjugate(VerbComponents(0, 2, 0, "past")))
    assert_equal("S/he did not throw out", ev.conjugate(VerbComponents(1, 2, 0, "past")))
    assert_equal("We threw out", ev.conjugate(VerbComponents(0, 0, 1, "past")))
    assert_equal("We did not throw out", ev.conjugate(VerbComponents(1, 0, 1, "past")))
    assert_equal("You all threw out", ev.conjugate(VerbComponents(0, 1, 1, "past")))
    assert_equal("You all did not throw out", ev.conjugate(VerbComponents(1, 1, 1, "past")))
    assert_equal("They threw out", ev.conjugate(VerbComponents(0, 2, 1, "past")))
    assert_equal("They did not throw out", ev.conjugate(VerbComponents(1, 2, 1, "past")))

    # simple future
    assert_equal("I will throw out", ev.conjugate(VerbComponents(0, 0, 0, "future")))
    assert_equal("I will not throw out", ev.conjugate(VerbComponents(1, 0, 0, "future")))
    assert_equal("You will throw out", ev.conjugate(VerbComponents(0, 1, 0, "future")))
    assert_equal("You will not throw out", ev.conjugate(VerbComponents(1, 1, 0, "future")))
    assert_equal("S/he will throw out", ev.conjugate(VerbComponents(0, 2, 0, "future")))
    assert_equal("S/he will not throw out", ev.conjugate(VerbComponents(1, 2, 0, "future")))
    assert_equal("We will throw out", ev.conjugate(VerbComponents(0, 0, 1, "future")))
    assert_equal("We will not throw out", ev.conjugate(VerbComponents(1, 0, 1, "future")))
    assert_equal("You all will throw out", ev.conjugate(VerbComponents(0, 1, 1, "future")))
    assert_equal("You all will not throw out", ev.conjugate(VerbComponents(1, 1, 1, "future")))
    assert_equal("They will throw out", ev.conjugate(VerbComponents(0, 2, 1, "future")))
    assert_equal("They will not throw out", ev.conjugate(VerbComponents(1, 2, 1, "future")))

    # present-perfect
    assert_equal("I have thrown out", ev.conjugate(VerbComponents(0, 0, 0, "present-perfect")))
    assert_equal("I have not thrown out", ev.conjugate(VerbComponents(1, 0, 0, "present-perfect")))
    assert_equal("You have thrown out", ev.conjugate(VerbComponents(0, 1, 0, "present-perfect")))
    assert_equal("You have not thrown out", ev.conjugate(VerbComponents(1, 1, 0, "present-perfect")))
    assert_equal("S/he has thrown out", ev.conjugate(VerbComponents(0, 2, 0, "present-perfect")))
    assert_equal("S/he has not thrown out", ev.conjugate(VerbComponents(1, 2, 0, "present-perfect")))
    assert_equal("We have thrown out", ev.conjugate(VerbComponents(0, 0, 1, "present-perfect")))
    assert_equal("We have not thrown out", ev.conjugate(VerbComponents(1, 0, 1, "present-perfect")))
    assert_equal("You all have thrown out", ev.conjugate(VerbComponents(0, 1, 1, "present-perfect")))
    assert_equal("You all have not thrown out", ev.conjugate(VerbComponents(1, 1, 1, "present-perfect")))
    assert_equal("They have thrown out", ev.conjugate(VerbComponents(0, 2, 1, "present-perfect")))
    assert_equal("They have not thrown out", ev.conjugate(VerbComponents(1, 2, 1, "present-perfect")))

    
def test_eng_compound_be():

    # Irreglar compound verb

    ev = EngVerb("be", compound_component="dissapointed")

    assert_equal("be dissapointed", str(ev))
    assert_equal(EngVerb("be", compound_component="dissapointed"), ev)
    assert_not_equal("be dissapointed", ev)

    # present continuous
    assert_equal("I am being dissapointed", ev.conjugate(VerbComponents(0, 0, 0, "present")))
    assert_equal("I am not being dissapointed", ev.conjugate(VerbComponents(1, 0, 0, "present")))
    assert_equal("You are being dissapointed", ev.conjugate(VerbComponents(0, 1, 0, "present")))
    assert_equal("You are not being dissapointed", ev.conjugate(VerbComponents(1, 1, 0, "present")))
    assert_equal("S/he is being dissapointed", ev.conjugate(VerbComponents(0, 2, 0, "present")))
    assert_equal("S/he is not being dissapointed", ev.conjugate(VerbComponents(1, 2, 0, "present")))
    assert_equal("We are being dissapointed", ev.conjugate(VerbComponents(0, 0, 1, "present")))
    assert_equal("We are not being dissapointed", ev.conjugate(VerbComponents(1, 0, 1, "present")))
    assert_equal("You all are being dissapointed", ev.conjugate(VerbComponents(0, 1, 1, "present")))
    assert_equal("You all are not being dissapointed", ev.conjugate(VerbComponents(1, 1, 1, "present")))
    assert_equal("They are being dissapointed", ev.conjugate(VerbComponents(0, 2, 1, "present")))
    assert_equal("They are not being dissapointed", ev.conjugate(VerbComponents(1, 2, 1, "present")))

    # simple past
    assert_equal("I was dissapointed", ev.conjugate(VerbComponents(0, 0, 0, "past")))
    assert_equal("I was not dissapointed", ev.conjugate(VerbComponents(1, 0, 0, "past")))
    assert_equal("You were dissapointed", ev.conjugate(VerbComponents(0, 1, 0, "past")))
    assert_equal("You were not dissapointed", ev.conjugate(VerbComponents(1, 1, 0, "past")))
    assert_equal("S/he was dissapointed", ev.conjugate(VerbComponents(0, 2, 0, "past")))
    assert_equal("S/he was not dissapointed", ev.conjugate(VerbComponents(1, 2, 0, "past")))
    assert_equal("We were dissapointed", ev.conjugate(VerbComponents(0, 0, 1, "past")))
    assert_equal("We were not dissapointed", ev.conjugate(VerbComponents(1, 0, 1, "past")))
    assert_equal("You all were dissapointed", ev.conjugate(VerbComponents(0, 1, 1, "past")))
    assert_equal("You all were not dissapointed", ev.conjugate(VerbComponents(1, 1, 1, "past")))
    assert_equal("They were dissapointed", ev.conjugate(VerbComponents(0, 2, 1, "past")))
    assert_equal("They were not dissapointed", ev.conjugate(VerbComponents(1, 2, 1, "past")))

    # simple future
    assert_equal("I will be dissapointed", ev.conjugate(VerbComponents(0, 0, 0, "future")))
    assert_equal("I will not be dissapointed", ev.conjugate(VerbComponents(1, 0, 0, "future")))
    assert_equal("You will be dissapointed", ev.conjugate(VerbComponents(0, 1, 0, "future")))
    assert_equal("You will not be dissapointed", ev.conjugate(VerbComponents(1, 1, 0, "future")))
    assert_equal("S/he will be dissapointed", ev.conjugate(VerbComponents(0, 2, 0, "future")))
    assert_equal("S/he will not be dissapointed", ev.conjugate(VerbComponents(1, 2, 0, "future")))
    assert_equal("We will be dissapointed", ev.conjugate(VerbComponents(0, 0, 1, "future")))
    assert_equal("We will not be dissapointed", ev.conjugate(VerbComponents(1, 0, 1, "future")))
    assert_equal("You all will be dissapointed", ev.conjugate(VerbComponents(0, 1, 1, "future")))
    assert_equal("You all will not be dissapointed", ev.conjugate(VerbComponents(1, 1, 1, "future")))
    assert_equal("They will be dissapointed", ev.conjugate(VerbComponents(0, 2, 1, "future")))
    assert_equal("They will not be dissapointed", ev.conjugate(VerbComponents(1, 2, 1, "future")))

    # present-perfect
    assert_equal("I have been dissapointed", ev.conjugate(VerbComponents(0, 0, 0, "present-perfect")))
    assert_equal("I have not been dissapointed", ev.conjugate(VerbComponents(1, 0, 0, "present-perfect")))
    assert_equal("You have been dissapointed", ev.conjugate(VerbComponents(0, 1, 0, "present-perfect")))
    assert_equal("You have not been dissapointed", ev.conjugate(VerbComponents(1, 1, 0, "present-perfect")))
    assert_equal("S/he has been dissapointed", ev.conjugate(VerbComponents(0, 2, 0, "present-perfect")))
    assert_equal("S/he has not been dissapointed", ev.conjugate(VerbComponents(1, 2, 0, "present-perfect")))
    assert_equal("We have been dissapointed", ev.conjugate(VerbComponents(0, 0, 1, "present-perfect")))
    assert_equal("We have not been dissapointed", ev.conjugate(VerbComponents(1, 0, 1, "present-perfect")))
    assert_equal("You all have been dissapointed", ev.conjugate(VerbComponents(0, 1, 1, "present-perfect")))
    assert_equal("You all have not been dissapointed", ev.conjugate(VerbComponents(1, 1, 1, "present-perfect")))
    assert_equal("They have been dissapointed", ev.conjugate(VerbComponents(0, 2, 1, "present-perfect")))
    assert_equal("They have not been dissapointed", ev.conjugate(VerbComponents(1, 2, 1, "present-perfect")))

def test_eng_compound_get():

    # "get X" is actually a regular verb. This test is present to remind me of this.

    ev = EngVerb("get", compound_component="lost")

    assert_equal("get lost", str(ev))
    assert_equal(EngVerb("get", compound_component="lost"), ev)
    assert_not_equal("get lost", ev)

    # present continuous
    assert_equal("I am getting lost", ev.conjugate(VerbComponents(0, 0, 0, "present")))
    assert_equal("I am not getting lost", ev.conjugate(VerbComponents(1, 0, 0, "present")))
    assert_equal("You are getting lost", ev.conjugate(VerbComponents(0, 1, 0, "present")))
    assert_equal("You are not getting lost", ev.conjugate(VerbComponents(1, 1, 0, "present")))
    assert_equal("S/he is getting lost", ev.conjugate(VerbComponents(0, 2, 0, "present")))
    assert_equal("S/he is not getting lost", ev.conjugate(VerbComponents(1, 2, 0, "present")))
    assert_equal("We are getting lost", ev.conjugate(VerbComponents(0, 0, 1, "present")))
    assert_equal("We are not getting lost", ev.conjugate(VerbComponents(1, 0, 1, "present")))
    assert_equal("You all are getting lost", ev.conjugate(VerbComponents(0, 1, 1, "present")))
    assert_equal("You all are not getting lost", ev.conjugate(VerbComponents(1, 1, 1, "present")))
    assert_equal("They are getting lost", ev.conjugate(VerbComponents(0, 2, 1, "present")))
    assert_equal("They are not getting lost", ev.conjugate(VerbComponents(1, 2, 1, "present")))

    # simple past
    assert_equal("I got lost", ev.conjugate(VerbComponents(0, 0, 0, "past")))
    assert_equal("I did not get lost", ev.conjugate(VerbComponents(1, 0, 0, "past")))
    assert_equal("You got lost", ev.conjugate(VerbComponents(0, 1, 0, "past")))
    assert_equal("You did not get lost", ev.conjugate(VerbComponents(1, 1, 0, "past")))
    assert_equal("S/he got lost", ev.conjugate(VerbComponents(0, 2, 0, "past")))
    assert_equal("S/he did not get lost", ev.conjugate(VerbComponents(1, 2, 0, "past")))
    assert_equal("We got lost", ev.conjugate(VerbComponents(0, 0, 1, "past")))
    assert_equal("We did not get lost", ev.conjugate(VerbComponents(1, 0, 1, "past")))
    assert_equal("You all got lost", ev.conjugate(VerbComponents(0, 1, 1, "past")))
    assert_equal("You all did not get lost", ev.conjugate(VerbComponents(1, 1, 1, "past")))
    assert_equal("They got lost", ev.conjugate(VerbComponents(0, 2, 1, "past")))
    assert_equal("They did not get lost", ev.conjugate(VerbComponents(1, 2, 1, "past")))

    # simple future
    assert_equal("I will get lost", ev.conjugate(VerbComponents(0, 0, 0, "future")))
    assert_equal("I will not get lost", ev.conjugate(VerbComponents(1, 0, 0, "future")))
    assert_equal("You will get lost", ev.conjugate(VerbComponents(0, 1, 0, "future")))
    assert_equal("You will not get lost", ev.conjugate(VerbComponents(1, 1, 0, "future")))
    assert_equal("S/he will get lost", ev.conjugate(VerbComponents(0, 2, 0, "future")))
    assert_equal("S/he will not get lost", ev.conjugate(VerbComponents(1, 2, 0, "future")))
    assert_equal("We will get lost", ev.conjugate(VerbComponents(0, 0, 1, "future")))
    assert_equal("We will not get lost", ev.conjugate(VerbComponents(1, 0, 1, "future")))
    assert_equal("You all will get lost", ev.conjugate(VerbComponents(0, 1, 1, "future")))
    assert_equal("You all will not get lost", ev.conjugate(VerbComponents(1, 1, 1, "future")))
    assert_equal("They will get lost", ev.conjugate(VerbComponents(0, 2, 1, "future")))
    assert_equal("They will not get lost", ev.conjugate(VerbComponents(1, 2, 1, "future")))

    # present-perfect
    assert_equal("I have gotten lost", ev.conjugate(VerbComponents(0, 0, 0, "present-perfect")))
    assert_equal("I have not gotten lost", ev.conjugate(VerbComponents(1, 0, 0, "present-perfect")))
    assert_equal("You have gotten lost", ev.conjugate(VerbComponents(0, 1, 0, "present-perfect")))
    assert_equal("You have not gotten lost", ev.conjugate(VerbComponents(1, 1, 0, "present-perfect")))
    assert_equal("S/he has gotten lost", ev.conjugate(VerbComponents(0, 2, 0, "present-perfect")))
    assert_equal("S/he has not gotten lost", ev.conjugate(VerbComponents(1, 2, 0, "present-perfect")))
    assert_equal("We have gotten lost", ev.conjugate(VerbComponents(0, 0, 1, "present-perfect")))
    assert_equal("We have not gotten lost", ev.conjugate(VerbComponents(1, 0, 1, "present-perfect")))
    assert_equal("You all have gotten lost", ev.conjugate(VerbComponents(0, 1, 1, "present-perfect")))
    assert_equal("You all have not gotten lost", ev.conjugate(VerbComponents(1, 1, 1, "present-perfect")))
    assert_equal("They have gotten lost", ev.conjugate(VerbComponents(0, 2, 1, "present-perfect")))
    assert_equal("They have not gotten lost", ev.conjugate(VerbComponents(1, 2, 1, "present-perfect")))

