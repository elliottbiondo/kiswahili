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
tense = ["li", "na", "ta"]

engine = pyttsx3.init()
engine.setProperty('rate', 125)

def check_result(expected, actual):
    if (expected.lower() == actual.lower()):
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(expected))

def swa_to_eng():
    swa = choice(subjects) + choice(tense) + choice(verb_roots)
    eng = translate(swa)

    engine.say(swa)
    engine.runAndWait()

    inp = input("Translate the following: {}\n>> ".format(swa))

    check_result(eng, inp)

def eng_to_swa():
    swa = choice(subjects) + choice(tense) + choice(verb_roots)
    eng = translate(swa)

    inp = input("Translate the following: {}\n>> ".format(eng))

    check_result(swa, inp)

while (True):
    a = choice([eng_to_swa(), swa_to_eng()])
