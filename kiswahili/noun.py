
class KisNoun(object):

    _noun_classes = ["m-wa", "m-mi", "ji-ma", "ma", "ki-vi", "n", "u", "m-wa*", "m-wa-n*", "m-wa-n**"]

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
        
