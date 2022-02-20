import sys

class NeurLang:
    def __init__(self, test=False):
        self.start(self.args)

    def start(self, path):

        if self.test == True:
            pass
        elif len(path) == 2:
            self.run(self.load_file(path))
        else:
            print("test-case-action")

    def load_file(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def run(self, source):
        print("Run_OK")
        pass
