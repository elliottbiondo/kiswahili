from random import choice, uniform
from copy import copy

from mashariki.parser import KisVerbParser, KisNounParser
from mashariki.verb import VerbComponents, EngVerb
from mashariki.challenge import Challenge

class Verb_Challenge(Challenge):

    def __init__(self, paths):
        vp = KisVerbParser(paths)
        self._verbs = vp.parse()
        print("Read {} verbs".format(vp.num_verbs()))

    def play(self):
        kis_verb = choice(self._verbs)
        vc = VerbComponents.from_random_sample()
        kis = kis_verb.conjugate(vc)
        eng = [x.conjugate(vc) for x in kis_verb.eng]

        if self._coin_flip():
            inp = input("Translate to English: {}\n> ".format(kis))
            inp = self._standardize_pronouns(inp)
            result = self._check(eng, inp)
            message = self._gen_correct_response_string(eng)
            self._print_result(result, message)
        else:
            # Must choose a single English translation
            eng = choice(eng)
            inp = input("Translate to Kiswahili: {0}\n> ".format(eng))
            result = self._check([kis], inp)
            self._print_result(result, kis)

class Noun_Challenge(Challenge):

    def __init__(self, paths):
        np = KisNounParser(paths)
        self._nouns = np.parse()
        print("Read {} nouns".format(np.num_nouns()))

    def play(self):

        # select a random kiswahili noun
        noun = choice(self._nouns)

        plurality_message = ""
        if self._coin_flip():
            kis = noun.sing
            eng = noun.eng_sing
            if noun.noun_class in ("n", "u", "m-w-n"):
                plurality_message = "(singular)"
        else:
            kis = noun.plur
            eng = noun.eng_plur
            if noun.noun_class in ("n", "u", "m-w-n"):
                plurality_message = "(plural)"

        if self._coin_flip():
            inp = input("Translate to Kiswahili: {0} {1}\n> ".format(choice(eng), plurality_message))
            result = self._check([kis], inp)
            self._print_result(result, kis)
        else:
            inp = input("Translate to English: {0} {1}\n> ".format(kis, plurality_message))
            result = self._check(eng, inp)
            message = self._gen_correct_response_string(eng)
            self._print_result(result, message)

#class Sentence_Challenge(Challenge):
#
#    def __init__(self, noun_paths, verb_paths):
#        np = KisNounParser(noun_paths)
#        vp = KisNounParser(verb_paths)
#        self._nouns = np.parse()
#        self._verbs = vp.parse()
#        print("Read {} nouns".format(np.num_nouns()))
#
#    def play(self):
#
#        # select a random kiswahili noun
#        noun = choice(self._nouns)
#
#        plurality_message = ""
#        if self._coin_flip():
#            kis = noun.sing
#            eng = noun.eng_sing
#            if noun.noun_class in ("n", "u", "m-wa-n"):
#                plurality_message = "(singular)"
#        else:
#            kis = noun.plur
#            eng = noun.eng_plur
#            if noun.noun_class in ("n", "u", "m-wa-m"):
#                plurality_message = "(plural)"
#
#        if self._coin_flip():
#            inp = input("Translate to Kiswahili: {0} {1}\n> ".format(choice(eng), plurality_message))
#            result = self._check([kis], inp)
#            self._print_result(result, kis)
#        else:
#            inp = input("Translate to English: {0} {1}\n> ".format(kis, plurality_message))
#            result = self._check(eng, inp)
#            message = self._gen_correct_response_string(eng)
#            self._print_result(result, message)


def main():
    nc = Noun_Challenge(["vocab/nouns"])
    vc = Verb_Challenge(["vocab/verbs"])

    while True:
        play = choice([nc.play, vc.play])
        play()

if __name__ == "__main__":
    main()
