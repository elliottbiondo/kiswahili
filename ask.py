from googletrans import Translator
from random import choice
from copy import copy

from parser import KisVerbParser
from verb import VerbComponents

def translate(phrase):
    translator = Translator()
    return translator.translate(phrase, src="sw", dest="en").text

def check_result(expected, actual):
    return expected.lower() == actual.lower()

def swa_to_eng(verb, vc):

    swa = verb.conjugate(vc)
    eng = translate(copy(swa))

    # Check if Google failed to translate
    if eng == swa:
        eng = str(vc) + "form of {}".format(verb.eng)

    inp = input("Translate to english: {}\n>> ".format(swa))

    if(check_result(eng, inp)):
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(eng))

def eng_to_swa(verb, vc):

    swa = verb.conjugate(vc)
    eng = translate(copy(swa))

    # Check if Google failed to translate
    if eng == swa:
        eng = str(vc) + "form of {}".format(verb.eng)

    # Differiate between you (singular) and you (plural) in English
    plural = ''
    if vc.person() == "second" and vc.plurality() == "plural":
        plural = '(plural)'

    inp = input("Translate to kiswahili: {0} {1}\n>> ".format(eng, plural))

    if(check_result(swa, inp)):
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(swa))

def main():
    vp = KisVerbParser(["vocab/verbs"])
    verbs = vp.parse()

    print("Read {} verbs".format(vp.num_verbs()))
    while (True):
        verb = choice(verbs)
        vc = VerbComponents.from_random_sample()
        a = choice([eng_to_swa, swa_to_eng])
        a(verb, vc)

if __name__ == "__main__":
    main()
