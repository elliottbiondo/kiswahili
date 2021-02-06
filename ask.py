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
    if (expected == actual):
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(expected))

def swa_to_eng():
    swa = choice(subjects) + choice(tense) + choice(verb_roots)
    eng = translate(swa)

    engine.say(swa)
    engine.runAndWait()

    inp = input("Translate the following: {}\n>> ".format(swa))

    print_result(eng, inp)

def eng_to_swa():
    swa = choice(subjects) + choice(tense) + choice(verb_roots)
    eng = translate(swa)

    inp = input("Translate the following: {}\n>> ".format(eng))

    print_result(swa, inp)

while (True):
    eng_to_swa()
    swa_to_eng()
