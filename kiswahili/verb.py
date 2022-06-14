from random import choice

try:
    import mlconjug3
except ImportError:
    error = ("Missing dependency: mlconjug3\n"
             "\tThis is needed for conjugating English verbs. Install via:\n"
             "\tpip3 install mlconjug3\n")
    raise ImportError(error)
    
class VerbComponents(object):

    # class variable defining cannonical sorting of verb components
    _polarity = ["affirmative", "negative"]
    _person = ["first", "second", "third"]
    _plurality = ["singular", "plural"]
    _tense = ["past", "present-perfect", "present", "future"]

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

    @property
    def polarity(self):
        return self._polarity[self._polarity_idx]

    @property
    def person(self):
        return self._person[self._person_idx]

    @property
    def plurality(self):
        return self._plurality[self._plurality_idx]

    @property
    def tense(self):
        return self._tense[self._tense_idx]

    @property
    def polarity_idx(self):
        return self._polarity_idx

    @property
    def person_idx(self):
        return self._person_idx

    @property
    def plurality_idx(self):
        return self._plurality_idx

    @property
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
        """
        Instantiate KisVerb object.

        Parameters
        ----------
        root : str
            The root of the Kiswahili verb
        eng : list of EngVerb
            The EngVerb objects representing all availible English translations
        """
        self.root = root

        for e in eng:
            if not isinstance(e, EngVerb):
                raise ValueError("Argument <eng> must be a list of EngVerb objects")
        self.eng = eng
        self.exceptions = {}

    def conjugate(self, vc):
        """
        Conjugate the verb for the supplied parameters

        Parameters
        ----------
        vc : verb_components
            The parameters necessary to cojugate the verb

        Returns
        -------
        str
            The conjugated verb
        """

        if vc in self.exceptions.keys():
            return self.exceptions[vc]

        subject_pre = self._subjects[vc.polarity_idx][vc.plurality_idx][vc.person_idx]
        tense_pre = self._tenses[vc.polarity_idx][vc.tense_idx]
        conj = subject_pre + tense_pre + self.root

        if (vc.tense == "present" and vc.polarity == "negative" and self._is_bantu):
            return conj[:-1] + "i"
        else:
            return conj

    @property
    def _is_bantu(self):
        """
        Determine if this verb is of Bantu origin, i.e., not Arabic

        Returns
        -------
        bool
            True if the verb of Bantu origin
        """
        return self.root[-1] == "a"


class EngVerb(object):

    _conj = mlconjug3.Conjugator(language='en')
    _subjects = [["I", "You", "S/he"], ["We", "You all", "They"]]
    _copula_present = [["am", "are", "is"], ["are", "are", "are"]]
    _copula_present_perfect = [["have", "have", "has"], ["have", "have", "have"]]

    def __init__(self, inf):
        self.inf = inf

    def __str__(self):
        return self.inf

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        else:
            return self.inf == str(other)

    def conjugate(self, vc):

        subject = self._subjects[vc.plurality_idx][vc.person_idx]

        if vc.tense == "future":
            conj_verb = self._conjugate_future(vc)
        else:
            conj_verb = self._conjugate_mlconj3(vc)

        return "{0} {1}".format(subject, conj_verb)

    def _conjugate_future(self, vc):
        # All English verbs are regular in the future test
        aux = "will" if vc.polarity == "affirmative" else "will not"
        return "{0} {1}".format(aux, self.inf)

    def _conjugate_mlconj3(self, vc):

        per_plur = "{0}{1}".format(vc.person_idx + 1, "s" if vc.plurality == "singular" else "p")

        if vc.tense == "past":
            if vc.polarity == "affirmative":
                aux = ""
                conj_root = self._conj.conjugate(self.inf).conjug_info['indicative']['indicative past tense'][per_plur]
            else:
                aux = "did not"
                conj_root = self.inf
                
        elif vc.tense == "present-perfect":
            cop = self._copula_present_perfect[vc.plurality_idx][vc.person_idx]
            aux = cop if vc.polarity == "affirmative" else "{0} not".format(cop)
            conj_root = self._conj.conjugate(self.inf).conjug_info['indicative']['indicative present perfect'][per_plur]

        elif vc.tense == "present":
            cop = self._copula_present[vc.plurality_idx][vc.person_idx]
            aux = cop if vc.polarity == "affirmative" else "{0} not".format(cop)
            conj_root = self._conj.conjugate(self.inf).conjug_info['indicative']['indicative present continuous'][per_plur]

        else:
            raise ValueError("Unrecognized tense: {}".format(vc.tense))

        return "{0}{1}{2}".format(aux, " " if aux else "", conj_root)


