from random import choice

class Verb(object):

    def __init__(self, root):
        self.root = root

        self.tenses = [{"past" : "li",
                       "present" : "na",
                       "future" : "ta"},
                       {"past" : "ku",
                        "present" : "",
                        "future" : "ta"}]

        self.subjects = [[["ni", "u", "a"], ["tu", "m", "wa"]],
                         [["si", "hu", "ha"], ["hatu", "ham", "hawa"]]]

    def _conjugate(self, tense, person, plural, neg):
        subject_pre = self.subjects[neg][plural][person]
        tense_pre = self.tenses[neg][tense]
        conj = subject_pre + tense_pre + self.root

        if (tense == "present" and neg == 1 and self.root[-1] == "a"):
            return conj[:-1] + "i"
        else:
            return conj

    def conjugate(self):
        tense = choice(["past", "present", "future"])
        person = choice([0, 1, 2])
        plural = choice([0, 1])
        neg = choice([0, 1])
        return self._conjugate(tense, person, plural, neg)





