from random import choice, uniform
from copy import copy

from parser import KisVerbParser, KisNounParser
from verb import VerbComponents, EngVerb

class Challenge(object):

    def __init__():
        pass

    def check_result(expected, actual):
        return expected.lower() == actual.lower()


def check_result(expected, actual, message):
    if expected.lower().split() == actual.lower().split():
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(message))


def kis_to_eng(kis_verb, eng_verb, vc):

    kis = kis_verb.conjugate(vc)
    eng = eng_verb.conjugate(vc, kis)

    # Check if Google failed to translate
    if eng == kis:
        eng = "{0} form of 'to {1}'".format(str(vc), eng_verb.inf)

    inp = input("Translate to English: {}\n>> ".format(kis))

    check_result(eng, inp, eng)


def eng_to_kis(kis_verb, eng_verb, vc):

    kis = kis_verb.conjugate(vc)
    eng = eng_verb.conjugate(vc, kis)

    # Check if Google failed to translate
    if eng == kis:
       eng = "{0} form of {1}".format(str(vc), eng_verb.inf)

    # Differiate between you (singular) and you (plural) in English
    plural = ''
    if vc.person() == "second" and vc.plurality() == "plural":
        plural = '(plural)'

    inp = input("Translate to Kiswahili: {0} {1}\n>> ".format(eng, plural))

    check_result(kis, inp, kis)

def verb_game():
    vp = KisVerbParser(["vocab/verbs"])
    verbs = vp.parse()

    print("Read {} verbs".format(vp.num_verbs()))
    while (True):

        # select a random kiswahili verb
        kis_verb = choice(verbs)

        # Since the verb may have multiple English translates, randomly select
        # an English infinative and convert to EngVerb
        eng_verb = EngVerb(choice(kis_verb.eng))

        vc = VerbComponents.from_random_sample()
        a = choice([eng_to_kis, kis_to_eng])
        a(kis_verb, eng_verb, vc)

def noun_game():
    np = KisNounParser(["vocab/flashcards"])
    nouns = np.parse()

    print("Read {} nouns".format(np.num_nouns()))
    while (True):

        # select a random kiswahili verb
        noun = choice(nouns)

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
            check_result(kis, inp, kis)
        else:
            inp = input("Translate to English: {0} {1}\n>> ".format(kis, plural))
            check_result(eng, inp, eng)

def main():
    #verb_game()
    noun_game()


if __name__ == "__main__":
    main()
