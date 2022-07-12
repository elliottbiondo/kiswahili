from random import choice, uniform

from parser import KisVerbParser, KisNounParser
from mashariki.verb import VerbComponents, EngVerb

from abc import ABC

class Challenge(ABC):

    _checkmark = u'\u2713'
    _xmark = u'\u2717'

    def __init__():
        pass

    def _print_result(self, is_correct, correct_response):

        if not isinstance(is_correct, bool):
            raise ValueError("Argument <is_correct> must be a bool")
        if not isinstance(correct_response, str):
            raise ValueError("Argument <correct_response> must be a str")

        if is_correct:
            print("{}\n".format(self._checkmark))
        else:
            print("{} {}\n".format(self._xmark, correct_response))

    def _gen_correct_response_string(self, correct_responses):
        if not self._is_list_of_strings(correct_responses):
            raise ValueError("Argument <expected> must be a list of strings")
        return " *or* ".join(correct_responses)

    def _coin_flip(self):
        return uniform(0, 1) < 0.5

    def _is_list_of_strings(self, inp):
        if inp and isinstance(inp, list): 
            return all(isinstance(x, str) for x in inp)
        else:
            return False

    def _standardize_pronouns(self, string):
        words = string.lower().split()
        for i in range(len(words)):
            if words[i] in ("he", "she"):
                words[i] = "s/he"
            elif words[i] == "y'all":
                words[i] = "you all"

        return " ".join(words)

    def _check(self, expected, actual):

        if not self._is_list_of_strings(expected):
            raise ValueError("Argument <expected> must be a list of strings")

        actual = actual.lower().split()
        for x in expected:
            if x.lower().split() == actual:
                return True
        
        return False

class Verb_Challenge(Challenge):

    def __init__(self, paths):
        vp = KisVerbParser(paths)
        self._verbs = vp.parse()
        print("Read {} verbs".format(vp.num_verbs()))

    def select_kis_eng(self):
        kis_verb = choice(self._verbs)
        vc = VerbComponents.from_random_sample()
        kis = kis_verb.conjugate(vc)
        eng = [x.conjugate(vc) for x in kis_verb.eng]

        return kis, eng, vc
