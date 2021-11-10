from googletrans import Translator
from random import choice

from parser import Verb_Parser
from verb import Verb_Components

def translate(phrase):
    translator = Translator()
    return translator.translate(phrase, src="sw", dest="en").text

def check_result(expected, actual):
    if (expected.lower() == actual.lower()):
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(expected))

def swa_to_eng(verbs):

    verb = choice(verbs)
    vc = Verb_Components.from_random_sample()
    swa = verb.conjugate(vc)

    eng = translate(swa)

    inp = input("Translate the following: {}\n>> ".format(swa))

    check_result(eng, inp)

def eng_to_swa(verbs):

    verb = choice(verbs)
    vc = Verb_Components.from_random_sample()
    swa = verb.conjugate(vc)

    eng = translate(swa)

    # Differiate between you (singular) and you (plural) in English
    plural = ''
    if vc.person == 1 and vc.sing_plur == 1:
        plural = '(plural)'

    inp = input("Translate the following: {0} {1}\n>> ".format(eng, plural))

    check_result(swa, inp)

def main():
    vp = Verb_Parser(["vocab/verbs"])
    verbs = vp.parse()
    print("Read {} verbs".format(vp.num_verbs()))
    while (True):
        a = choice([eng_to_swa(verbs), swa_to_eng(verbs)])

if __name__ == "__main__":
    main()
