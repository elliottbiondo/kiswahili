from random import choice
from google_trans_new import google_translator as Translator

class VerbComponents(object):

    # class variable defining cannonical sorting of verb components
    _polarity = ["affirmative", "negative"]
    _person = ["first", "second", "third"]
    _plurality = ["singular", "plural"]
    _tense = ["past", "past-perfect", "present", "future"]

    def __init__(self, polarity_idx, person_idx, plurality_idx, tense):

        self._polarity_idx = polarity_idx
        self._person_idx = person_idx
        self._plurality_idx = plurality_idx
        self._tense_idx = self._tense.index(tense)

    @classmethod
    def from_random_sample(cls):
        polarity = choice(range(len(cls._polarity)))
        person = choice(range(len(cls._person)))
        plurality = choice(range(len(cls._plurality)))
        tense = choice(cls._tense)
        return cls(polarity, person, plurality, tense)

    def polarity(self):
        return self._polarity[self._polarity_idx]

    def person(self):
        return self._person[self._person_idx]

    def plurality(self):
        return self._plurality[self._plurality_idx]

    def tense(self):
        return self._tense[self._tense_idx]

    def polarity_idx(self):
        return self._polarity_idx

    def person_idx(self):
        return self._person_idx

    def plurality_idx(self):
        return self._plurality_idx

    def tense_idx(self):
        return self._tense_idx

    def __hash__(self):
        return hash((self._polarity_idx,
                     self._person_idx,
                     self._plurality_idx,
                     self._tense_idx))

    def __eq__(self, other):
        return (self._polarity_idx, self._person_idx, self._plurality_idx, self._tense_idx) == \
               (other._polarity_idx, other._person_idx, other._plurality_idx, other._tense_idx)

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        out  = "{}, ".format(self._polarity[self._polarity_idx])
        out += "{} person, ".format(self._person[self._person_idx])
        out += "{}, ".format(self._plurality[self._plurality_idx])
        out += "{} tense".format(self._tense[self._tense_idx])
        return out


class KisVerb(object):

    _tenses = [["li", "me", "na", "ta"],
               ["ku",  "ja",  "", "ta"]]

    _subjects = [[["ni", "u", "a"], ["tu", "m", "wa"]],
                 [["si", "hu", "ha"], ["hatu", "ham", "hawa"]]]

    def __init__(self, root, eng):
        self.root = root
        self.eng = eng
        self.exceptions = {}


    def conjugate(self, vc):

        if vc in self.exceptions.keys():
            return self.exceptions[vc]

        subject_pre = self._subjects[vc.polarity_idx()][vc.plurality_idx()][vc.person_idx()]
        tense_pre = self._tenses[vc.polarity_idx()][vc.tense_idx()]
        conj = subject_pre + tense_pre + self.root

        if (vc.tense() == "present" and vc.polarity() == "negative" and self.is_bantu()):
            return conj[:-1] + "i"
        else:
            return conj

    def is_bantu(self):
        return self.root[-1] == "a"


class EngVerb(object):

    _translator = Translator()
    _subjects = [["I", "You", "S/he"], ["We", "You all", "They"]]
    _copula = [["am", "are", "is"], ["are", "are", "are"]]

    def __init__(self, inf):
        self.inf = inf

    def gerund(self):
        if self.inf[-1] == "e":
            root = self.inf[:-1]
        else:
            root = self.inf
        return root + "ing"

    def conjugate(self, vc, swa):

        if vc.tense() == "future":
            return self._conjugate_future(vc)
        else:
            return self._conjugate_google(swa)

    def _conjugate_future(self, vc):
        # All English verbs are regular in the future test
        subject = self._subjects[vc.plurality_idx()][vc.person_idx()]
        aux = "will" if vc.polarity() == "affirmative" else "will not"
        return "{0} {1} {2}".format(subject, aux, self.inf)


    def _conjugate_present(self, vc):
        # this doesn't work yet, and might not be something worth pursuing
        subject = self._subjects[vc.plurality_idx()][vc.person_idx()]
        aux = self._copula[vc.plurality_idx()][vc.person_idx()]

        if vc.polarity() == "negative":
            aux += " not"

        return "{0} {1} {2}".format(subject, aux, self.gerund())

    def _conjugate_google(self, phrase):
        return self._translator.translate(phrase, lang_src="sw", lang_tgt="en")

