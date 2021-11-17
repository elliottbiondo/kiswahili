from random import choice
from copy import copy

from parser import KisVerbParser
from verb import VerbComponents, EngVerb

class Challenge(object):

    def __init__():
        pass

    def check_result(expected, actual):
        return expected.lower() == actual.lower()


def check_result(expected, actual, message):
    if expected.lower() == actual.lower():
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(message))


def swa_to_eng(kis_verb, eng_verb, vc):

    swa = kis_verb.conjugate(vc)
    eng = eng_verb.conjugate(vc, swa)

    # Check if Google failed to translate
    if eng == swa:
        eng = "{0} form of 'to {1}'".format(str(vc), eng_verb.inf)

    inp = input("Translate to English: {}\n>> ".format(swa))

    check_result(eng, inp, eng)


def eng_to_swa(kis_verb, eng_verb, vc):

    swa = kis_verb.conjugate(vc)
    eng = eng_verb.conjugate(vc, swa)

    # Check if Google failed to translate
    if eng == swa:
       eng = "{0} form of {1}".format(str(vc), eng_verb.inf)

    # Differiate between you (singular) and you (plural) in English
    plural = ''
    if vc.person() == "second" and vc.plurality() == "plural":
        plural = '(plural)'

    inp = input("Translate to Kiswahili: {0} {1}\n>> ".format(eng, plural))

    check_result(swa, inp, swa)

def main():
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
        a = choice([eng_to_swa, swa_to_eng])
        a(kis_verb, eng_verb, vc)

if __name__ == "__main__":
    main()
