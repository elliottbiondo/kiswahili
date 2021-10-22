from verb import Verb

def parse():
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
    return verbs

