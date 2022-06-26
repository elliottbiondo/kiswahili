from nose.tools import assert_equal, with_setup, assert_raises

from noun import KisNoun
from verb import VerbComponents

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


def test_subject_prefixs():

    n = KisNoun("kisu", "visu", ["knife"], ["knives"], "ki-vi")

    vc = VerbComponents(0, 2, 0, "present")
    assert_equal("ki", n.calc_subject_prefix(vc))

    vc = VerbComponents(0, 2, 1, "future")
    assert_equal("vi", n.calc_subject_prefix(vc))

    vc = VerbComponents(1, 2, 0, "present-perfect")
    assert_equal("haki", n.calc_subject_prefix(vc))

    vc = VerbComponents(1, 2, 1, "past")
    assert_equal("havi", n.calc_subject_prefix(vc))
