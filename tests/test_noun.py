from nose.tools import assert_equal, with_setup, assert_raises

from noun import KisNoun

def test_basic():

    n = KisNoun("kipaji",
                "vipaji",
                ["talent", "gift", "donation"],
                ["talents", "gifts", "donations"],
                "ki-vi")

    assert_equal("kipaji", n.sing)
    assert_equal("vipaji", n.plur)
    assert_equal(["talent", "gift", "donation"], n.eng_sing)
    assert_equal(["talents", "gifts", "donations"], n.eng_plur)
    assert_equal("ki-vi", n.noun_class)

    assert_equal(["ki", "vi"], n.subject_prefixes)
    assert_equal(["cha", "vya"], n.possessive_prefixes)
    assert_equal(["ki", "vi"], n.adjective_prefixes)

    # Throw an error if the noun class is not valid
    with assert_raises(ValueError):
        KisNoun("jiwe", "mawe", "stone", "stones", "x")

    # Throw and error if the prefixes are not yet supported
    #with assert_raises(NotImplementedError):
    #   n2 = KisNoun("maji", "maji", "water", "water", "ma")
    #   n2.subject_prefixes

