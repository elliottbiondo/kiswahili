
class Noun(object):

    self._noun_classes = ["m-wa", "m-mi", "ji-ma", "ki-vi", "n", "u"]

    self._subject_prefixs = [[ "a", "wa"], # m-wa
                             [ "u",  "i"], # m-mi
                             ["li", "ya"], # ji-ma
                             ["ki", "vi"], # ki-vi
                             [ "i", "zi"], # n
                             [ "u",  "u"]] # u

    self._possessive_prefixs = [["wa", "wa"], # m-wa
                                ["wa", "ya"], # m-mi
                                ["la", "ya"], # ji-ma
                                ["cha", "vya"], # ki-vi
                                [ "ya",  "za"], # n
                                ["wa", "wa"]] # u

    self._adjective_prefixs = [[ "m", "wa"], # m-wa
                               [ "m", "mi"], # m-mi
                               [  "", "ma"], # ji-ma
                               ["ki", "vi"], # ki-vi
                               [ "n",  "n"], # n
                               [ "m",  "m"]] # u

    def __init__(self, sing, plur, eng_sing, eng_plural, noun_class):
        self.sing = sing
        self.plur = plur
        self.eng_sing = eng_sing
        self.eng_plur = eng_plur
        self.noun_class = noun_class
