from nose.tools import assert_equal, with_setup, assert_raises

from parser import Verb_Parser

def test_simple():
    parser = Verb_Parser(["input/verbs"])
    verbs = parser.parse()

    assert_equal(3, len(verbs))

    assert_equal("kubali", verbs[0].root)
    assert_equal(["agree", "accept"],  verbs[0].eng)

    assert_equal("kimbia", verbs[1].root)
    assert_equal(["run", "flee"],  verbs[1].eng)

    assert_equal("fikiri", verbs[2].root)
    assert_equal(["think"],  verbs[2].eng)

