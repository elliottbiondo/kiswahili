from nose.tools import assert_equal, with_setup, assert_raises

from parser import KisVerbParser, KisNounParser
from verb import EngVerb

def test_verbs():
    parser = KisVerbParser(["input/verbs"])
    verbs = parser.parse()

    assert_equal(5, len(verbs))

    assert_equal("kubali", verbs[0].root)
    assert_equal([EngVerb("agree"), EngVerb("accept")],  verbs[0].eng)

    assert_equal("kimbia", verbs[1].root)
    assert_equal([EngVerb("run"), EngVerb("flee")],  verbs[1].eng)

    assert_equal("fikiri", verbs[2].root)
    assert_equal([EngVerb("think")],  verbs[2].eng)

    assert_equal("nawa", verbs[3].root)
    assert_equal([EngVerb("wash", compound_component="hands")],  verbs[3].eng)

    assert_equal("tosha", verbs[4].root)
    assert_equal([EngVerb("be", compound_component="enough"), EngVerb("satisfy")],  verbs[4].eng)

def test_nouns():
    parser = KisNounParser(["input/nouns"])
    nouns = parser.parse()

    assert_equal(5, len(nouns))

    n = nouns[0]
    assert_equal("ndizi", n.sing)
    assert_equal("ndizi", n.plur)
    assert_equal(["banana"], n.eng_sing)
    assert_equal(["bananas"], n.eng_plur)
    assert_equal("n", n.noun_class)

    n = nouns[1]
    assert_equal("muuguzi", n.sing)
    assert_equal("wauguzi", n.plur)
    assert_equal(["nurse"], n.eng_sing)
    assert_equal(["nurses"], n.eng_plur)
    assert_equal("m-wa", n.noun_class)

    n = nouns[2]
    assert_equal("ujasiri", n.sing)
    assert_equal("ujasiri", n.plur)
    assert_equal(["confidence", "courage", "bravery"], n.eng_sing)
    assert_equal(["confidence", "courage", "bravery"], n.eng_plur)
    assert_equal("u", n.noun_class)

    n = nouns[3]
    assert_equal("motisha", n.sing)
    assert_equal("motisha", n.plur)
    assert_equal(["motivation", "incentive"], n.eng_sing)
    assert_equal(["motivations", "incentives"], n.eng_plur)
    assert_equal("n", n.noun_class)

    n = nouns[4]
    assert_equal("kipaji", n.sing)
    assert_equal("vipaji", n.plur)
    assert_equal(["talent", "gift", "donation"], n.eng_sing)
    assert_equal(["talents", "gifts", "donations"], n.eng_plur)
    assert_equal("ki-vi", n.noun_class)


