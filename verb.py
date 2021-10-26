from random import choice

class Verb(object):

    def __init__(self, root):
        self.root = root

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

    def _conjugate(self, pos_neg, person, sing_plur, tense):

        if (pos_neg, person, sing_plur, tense) in self.exceptions.keys():
            return self.exceptions[pos_neg, person, sing_plur, tense]

        subject_pre = self.subjects[pos_neg][sing_plur][person]
        tense_pre = self.tenses[pos_neg][tense]
        conj = subject_pre + tense_pre + self.root

        if (tense == "present" and pos_neg == 1 and self.root[-1] == "a"):
            return conj[:-1] + "i"
        else:
            return conj

    def conjugate(self):
        tense = choice(["past", "present", "future", "past-perfect"])
        person = choice([0, 1, 2])
        sing_plur = choice([0, 1])
        pos_neg = choice([0, 1])
        return self._conjugate(pos_neg, person, sing_plur, tense)


