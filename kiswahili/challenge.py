from random import uniform

from abc import ABC

class Challenge(ABC):

    _checkmark = u'\u2713'
    _xmark = u'\u2717'

    def __init__():
        pass

    def _print_result(self, is_correct, message):
        if is_correct:
            print("{}\n".format(self._checkmark))
        else:
            print("{} {}\n".format(self._xmark, message))

    def _coin_flip(self):
        return uniform(0, 1) < 0.5

    def _standardize_pronouns(self, string):
        words = string.lower().split()
        for i in range(len(words)):
            if words[i] in ("he", "she"):
                words[i] = "s/he"
            elif words[i] == "y'all":
                words[i] = "you all"

        return " ".join(words)

    def _check(self, expected, actual):
        actual = actual.lower().split()
        for x in expected:
            if x.lower().split() == actual:
                return True
        
        return False
