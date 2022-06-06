from random import choice, uniform
from copy import copy

from kiswahili.parser import KisVerbParser, KisNounParser
from kiswahili.verb import VerbComponents, EngVerb

class Challenge(object):

    def __init__():
        pass

    def _check(self, expected, actual, message):
        if expected.lower().split() == actual.lower().split():
            print("CORRECT\n")
        else:
            print("INCORRECT! answer: {}\n".format(message))

class Verb_Challenge(Challenge):

    def __init__(self):
        vp = KisVerbParser(["vocab/verbs"])
        self._verbs = vp.parse()
        print("Read {} verbs".format(vp.num_verbs()))

    def play(self):

        # select a random kiswahili verb
        kis_verb = choice(self._verbs)

        # Since the verb may have multiple English translates, randomly select
        # an English infinative and convert to EngVerb
        eng_verb = EngVerb(choice(kis_verb.eng))

        vc = VerbComponents.from_random_sample()
        kis = kis_verb.conjugate(vc)
        eng = eng_verb.conjugate(vc)

        if uniform(0, 1) < 0.5:
            inp = input("Translate to English: {}\n>> ".format(kis))
            self._check(eng, inp, eng)

        else:
            # Differiate between you (singular) and you (plural) in English
            plural = ''
            if vc.person == "second" and vc.plurality == "plural":
                plural = '(plural)'

            inp = input("Translate to Kiswahili: {0} {1}\n>> ".format(eng, plural))
            self._check(kis, inp, kis)


class Noun_Challenge(Challenge):

    def __init__(self):
        np = KisNounParser(["vocab/flashcards"])
        self._nouns = np.parse()
        print("Read {} nouns".format(np.num_nouns()))

    def play(self):

        # select a random kiswahili verb
        noun = choice(self._nouns)

        plural = ""
        if uniform(0, 1) < 0.5:
            kis = noun.sing
            eng = choice(noun.eng_sing)
        else:
            kis = noun.plur
            eng = choice(noun.eng_plur)
            if noun.noun_class in ("n", "u"):
                plural = "(plural)"

        if uniform(0, 1) < 0.5:
            inp = input("Translate to Kiswahili: {0} {1}\n>> ".format(eng, plural))
            self._check(kis, inp, kis)
        else:
            inp = input("Translate to English: {0} {1}\n>> ".format(kis, plural))
            self._check(eng, inp, eng)

def main():
    nc = Noun_Challenge()
    vc = Verb_Challenge()

    while True:
        play = choice([nc.play, vc.play])
        play()

if __name__ == "__main__":
    main()
