from verb import Verb

class Verb_Parser(object):

    def __init__(self, paths):
        self.paths = paths
        self.verbs = []

    def _valid_line(self, line):
        return len(line.strip()) > 0 and line.strip()[0] != "#"

    def _parse_verb_line(self, line):
        return line.split("#")[0].strip().strip("-")

    def _parse_file(self, path):
        with open(path, 'r') as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                if self._valid_line(lines[i]):
                    verb = Verb(self._parse_verb_line(lines[i]))
                    i += 1
                    while lines[i].strip() != '':
                        line = lines[i].strip("#")
                        if line.strip()[0] == "exception":
                            pos_neg, person, sing_plur, tense, value \
                                = line.strip()[1:]
    
                            pos_neg = 0 if pos_neg == "pos" else 1
                            person -= 1
                            sing_plur = 0 if sing_plur == "sing" else 1
                            verb.exceptions[(pos_neg, person, sing_plur, tense)] = value
                        i += 1
                    self.verbs.append(verb)
                else:
                    i += 1

    def parse(self):
        for path in self.paths:
            self._parse_file(path)
        return self.verbs

