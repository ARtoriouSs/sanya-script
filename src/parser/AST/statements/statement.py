import re

class Statement:
    def kind(self):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', self.__class__.__name__).lower()

    def set_line(self, line):
        self.line = line
