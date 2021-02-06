from googletrans import Translator
from random import choice

def trans(phrase):
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



while (True):
    phrase = choice(subjects) + choice(tense) + choice(verb_roots)
    val = input("Translate the following: {}\n".format(phrase))

    t = trans(phrase)

    if (val == t):
        print("CORRECT\n")
    else:
        print("INCORRECT! answer: {}\n".format(t))
