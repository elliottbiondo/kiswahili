
class KisNoun(object):

    _noun_classes = ["m-wa", "m-mi", "ji-ma", "ki-vi", "n", "u", "m-wa*", "m-wa-n*", "m-wa-n**", "ma"]

    _subject_prefixs = [[ "a", "wa"], # m-wa
                        [ "u",  "i"], # m-mi
                        ["li", "ya"], # ji-ma
                        ["ki", "vi"], # ki-vi
                        [ "i", "zi"], # n
                        [ "u",  "u"]] # u

    _possessive_prefixs = [["wa", "wa"], # m-wa
                           ["wa", "ya"], # m-mi
                           ["la", "ya"], # ji-ma
                           ["cha", "vya"], # ki-vi
                           [ "ya",  "za"], # n
                           ["wa", "wa"]] # u

    _adjective_prefixs = [[ "m", "wa"], # m-wa
                          [ "m", "mi"], # m-mi
                          [  "", "ma"], # ji-ma
                          ["ki", "vi"], # ki-vi
                          [ "n",  "n"], # n
                          [ "m",  "m"]] # u

    def __init__(self, sing, plur, eng_sing, eng_plur, noun_class):
        self._sing = sing
        self._plur = plur
        self._eng_sing = eng_sing
        self._eng_plur = eng_plur

        try:
            self._noun_class_index = self._noun_classes.index(noun_class)
        except ValueError:
            raise ValueError(
                "Invalid noun class '{0}' for noun {1}".format(noun_class,
                                                               sing))

    def _check_noun_class_supported(self):
        if self._noun_class_index >= 7:
            raise NotImplementedError("Noun class {} does not yet support prefixes".format(self.noun_class))

    @property
    def sing(self):
        return self._sing

    @property
    def plur(self):
        return self._plur

    @property
    def eng_sing(self):
        return self._eng_sing

    @property
    def eng_plur(self):
        return self._eng_plur

    @property
    def noun_class(self):
        return self._noun_classes[self._noun_class_index]
        
    @property
    def subject_prefixes(self):
        self._check_noun_class_supported()
        return self._subject_prefixs[self._noun_class_index]

    @property
    def possessive_prefixes(self):
        self._check_noun_class_supported()
        return self._possessive_prefixs[self._noun_class_index]

    @property
    def adjective_prefixes(self):
        self._check_noun_class_supported()
        return self._adjective_prefixs[self._noun_class_index]

