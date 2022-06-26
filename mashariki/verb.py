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
        """
        Initialize VerbComponents object

        Parameters
        ----------
        polarity_idx : int 
            affirmative (0) or negative (1) verb form, e.g. "do" vs. do not
        person_idx : int 
            1st (0), 2nd (1), or 3rd (2) person verb form, e.g. I do, you do, he/she/it does
        plurality_idx : int
            singular (0) or plural (0) verb form, e.g., I do, we do
        tense : str
            any tense in self._tense
        """

        self._polarity_idx = polarity_idx
        self._person_idx = person_idx
        self._plurality_idx = plurality_idx
        self._tense_idx = self._tense.index(tense)
    
    @classmethod
    def from_random_sample(cls, third_person=False):
        """
        Create a randomly generated VerbComponent object

        Parameters
        ----------
        third_person : bool
            If True, VerbComponent is guarenteed to be third person

        Returns
        -------
        vc : VerbComponents
            Randomly generated object
        """
        polarity = choice(range(len(cls._polarity)))
        if third_person:
            person = 2
        else:
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

    def conjugate(self, vc, subject_pre=None):
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

        if subject_pre is None:
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

    def __init__(self, inf, compound_component=""):
        self._inf = inf
        self._compound_component = compound_component

    def __str__(self):
        if self._compound_component:
            return "{0} {1}".format(self._inf, self._compound_component)
        else:
            return self._inf

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        else:
            return str(self) == str(other)

    def conjugate(self, vc):

        subject = self._subjects[vc.plurality_idx][vc.person_idx]

        if vc.tense == "future":
            conj_verb = self._conjugate_future(vc)
        else:
            conj_verb = self._conjugate_mlconj3(vc)

        out =  "{0} {1}".format(subject, conj_verb)
        if self._compound_component:
            out += " {0}".format(self._compound_component)
        return out

    def _conjugate_future(self, vc):
        # All English verbs are regular in the future test
        aux = "will" if vc.polarity == "affirmative" else "will not"
        return "{0} {1}".format(aux, self._inf)

    def _conjugate_mlconj3(self, vc):

        per_plur = "{0}{1}".format(vc.person_idx + 1, "s" if vc.plurality == "singular" else "p")

        if vc.tense == "past":
            aux = ""
            if vc.polarity == "affirmative":
                conj_root = self._conj.conjugate(self._inf).conjug_info['indicative']['indicative past tense'][per_plur]
            else:
                if self._inf == "be":
                    conj_root = self._conj.conjugate(self._inf).conjug_info['indicative']['indicative past tense'][per_plur]
                    conj_root += " not"
                else:
                    aux = "did not"
                    conj_root = self._inf
                
        elif vc.tense == "present-perfect":
            cop = self._copula_present_perfect[vc.plurality_idx][vc.person_idx]
            aux = cop if vc.polarity == "affirmative" else "{0} not".format(cop)
            conj_root = self._conj.conjugate(self._inf).conjug_info['indicative']['indicative present perfect'][per_plur]

        elif vc.tense == "present":
            cop = self._copula_present[vc.plurality_idx][vc.person_idx]
            aux = cop if vc.polarity == "affirmative" else "{0} not".format(cop)
            conj_root = self._conj.conjugate(self._inf).conjug_info['indicative']['indicative present continuous'][per_plur]

        else:
            raise ValueError("Unrecognized tense: {}".format(vc.tense))

        return "{0}{1}{2}".format(aux, " " if aux else "", conj_root)


