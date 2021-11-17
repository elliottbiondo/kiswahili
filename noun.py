
class Noun(object):

    self.noun_classes = ["m-wa", "m-mi", "ji-ma", "ki-vi", "n", "u"]

    def __init__(self, sing, plur, eng_sing, eng_plural, noun_class):
        self.sing = sing
        self.plur = plur
        self.eng_sing = eng_sing
        self.eng_plur = eng_plur
        self.noun_class = noun_class
