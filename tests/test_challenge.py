from nose.tools import assert_equal, assert_true, assert_false

from challenge import Challenge

class ChallengeMock(Challenge):
    def __init__(self):
        pass
    
def test_standardize_prounouns():

    c = ChallengeMock()

    assert_equal("you all run", c._standardize_pronouns("y'all run"))
    assert_equal("s/he runs", c._standardize_pronouns("he runs"))
    assert_equal("s/he runs", c._standardize_pronouns("she runs"))

def test_check():

    c = ChallengeMock()
    assert_true(c._check(["They thought", "They pondered"], "they pondered"))
    assert_true(c._check(["They thought", "They pondered"], "they thought"))
    assert_false(c._check(["They thought", "They pondered"], "they walked"))

def test_gen_correct_response_string():

    c = ChallengeMock()

    assert_equal('You will run *or* You will flee',
                 c._gen_correct_response_string(["You will run", "You will flee"]))

