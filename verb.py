from random import choice

class Verb_Components:

    def __init__(self, pos_neg, person, sing_plur, tense):
        self.pos_neg = pos_neg
        self.person = person
        self.sing_plur = sing_plur
        self.tense = tense

    @classmethod
    def from_random_sample(cls):
        pos_neg = choice([0, 1])
        person = choice([0, 1, 2])
        sing_plur = choice([0, 1])
        tense = choice(["past", "present", "future", "past-perfect"])
        return cls(pos_neg, person, sing_plur, tense)

class Conjugated_Verb():
    def __init__(self):
        pass


class Verb(object):

    def __init__(self, root, eng):
        self.root = root
        self.eng = eng

        self.tenses = [{"past" : "li",
                       "present" : "na",
                       "future" : "ta",
                       "past-perfect" : "me"},
                       {"past" : "ku",
                        "present" : "",
                        "future" : "ta",
                        "past-perfect" : "ja"}]

        self.subjects = [[["ni", "u", "a"], ["tu", "m", "wa"]],
                         [["si", "hu", "ha"], ["hatu", "ham", "hawa"]]]

        self.exceptions = {}

    def conjugate(self):

        vc = Verb_Components.from_random_sample()

        if (vc.pos_neg, vc.person, vc.sing_plur, vc.tense) in self.exceptions.keys():
            return self.exceptions[vc.pos_neg, vc.person, vc.sing_plur, vc.tense]

        subject_pre = self.subjects[vc.pos_neg][vc.sing_plur][vc.person]
        tense_pre = self.tenses[vc.pos_neg][vc.tense]
        conj = subject_pre + tense_pre + self.root

        if (vc.tense == "present" and vc.pos_neg == 1 and self.root[-1] == "a"):
            return conj[:-1] + "i"
        else:
            return conj
