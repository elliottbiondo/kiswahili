from googletrans import Translator
import pyttsx3
from random import choice

def translate(phrase):
    translator = Translator()
    return translator.translate(phrase, src="sw", dest="en").text

verb_roots = []
with open("verbs", 'r') as f:
    lines = f.readlines()
    for line in lines:
        if len(line.strip()) > 0:
            verb_roots.append(line.split("&")[0].strip().strip("-"))

subjects = ["ni", "u", "a", "tu", "m", "wa"]
#tense = ["li", "na", "ta"]
tense = ["na"]

engine = pyttsx3.init()
engine.setProperty('rate', 125)


def print_result(expected, actual):
    pass


def swa_to_eng():
    phrase = choice(subjects) + choice(tense) + choice(verb_roots)
    engine.say(phrase)
    engine.runAndWait()
    val = input("Translate the following: {}\n>> ".format(phrase))

    trans = translate(phrase)

    if (val.lower() == trans.lower()):
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(trans))

def eng_to_swa():
    swa = choice(subjects) + choice(tense) + choice(verb_roots)
    eng = translate(swa)
    inp = input("Translate the following: {}\n>> ".format(eng))

    if (inp.lower() == swa.lower()):
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(swa))

while (True):
    eng_to_swa()
    swa_to_eng()
