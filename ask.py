from googletrans import Translator
import pyttsx3
from random import choice

from parser import parse

def translate(phrase):
    translator = Translator()
    return translator.translate(phrase, src="sw", dest="en").text

def check_result(expected, actual):
    if (expected.lower() == actual.lower()):
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(expected))

def swa_to_eng():

    verb = choice(verbs)
    swa = verb.conjugate()

    eng = translate(swa)

    engine.say(swa)
    engine.runAndWait()

    inp = input("Translate the following: {}\n>> ".format(swa))

    check_result(eng, inp)

def eng_to_swa():
    verb = choice(verbs)
    swa = verb.conjugate()

    eng = translate(swa)

    inp = input("Translate the following: {}\n>> ".format(eng))

    check_result(swa, inp)

verbs = parse()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

while (True):
    a = choice([eng_to_swa(), swa_to_eng()])
