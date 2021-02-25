from googletrans import Translator
import pyttsx3
from random import choice

from verb import Verb

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

verbs = []
with open("vocab/verbs", 'r') as f:
    lines = f.readlines()
    i= 0
    while i < len(lines):
        if len(lines[i].strip()) > 0 and lines[i].strip()[0] != "#":
            verb = Verb(lines[i].split("#")[0].strip().strip("-"))
            i += 1
            while lines[i].strip() != '':
                line = lines[i].strip("#")
                if line.strip()[0] == "exception":
                    pos_neg, person, sing_plur, tense, value = line.strip()[1:]
                    pos_neg = 0 if pos_neg == "pos" else 1
                    person -= 1
                    sing_plur = 0 if sing_plur == "sing" else 1
                    verb.exceptions[(pos_neg, person, sing_plur, tense)] = value
                i += 1
            verbs.append(verb)
        else:
            i += 1

engine = pyttsx3.init()
engine.setProperty('rate', 150)

while (True):
    a = choice([eng_to_swa(), swa_to_eng()])
