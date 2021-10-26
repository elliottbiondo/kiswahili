from verb import Verb

class Verb_Parser(object):

    def __init__(self, paths):
        self.paths = paths
        self.verbs = []

    def _blank_line(self, line):
        return len(line.strip()) == 0

    def _comment_line(self, line):
        if self._blank_line(line):
            return False
        else:
            return line.strip()[0] == "#"

    def _valid_line(self, line):
        return (not self._comment_line(line)) \
            and (not self._blank_line(line))

    def _parse_verb_line(self, line):
        return line.split("#")[0].strip().strip("-")

    def _process_exceptions(self, verb, exception_lines):
        for line in exception_lines:
           if line.split()[0] == "exception":
               pos_neg, person, sing_plur, tense, value \
                   = line.split()[1:]

               pos_neg = 0 if pos_neg == "pos" else 1
               person = int(person) - 1
               sing_plur = 0 if sing_plur == "sing" else 1
               verb.exceptions[(pos_neg, person, sing_plur, tense)] = value

    def _parse_file(self, path):
        with open(path, 'r') as f:
            lines = f.readlines()
        
        i = 0
        while i < len(lines):
            if self._valid_line(lines[i]):
                verb = Verb(self._parse_verb_line(lines[i]))
                i += 1

                exception_lines = []
                while i < len(lines) and not self._blank_line(lines[i]):
                    exception_lines.append(lines[i])
                    i += 1

                if len(exception_lines) > 0:
                    self._process_exceptions(verb, exception_lines)

                self.verbs.append(verb)
            else:
                i += 1

    def parse(self):
        for path in self.paths:
            self._parse_file(path)
        return self.verbs

