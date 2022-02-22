import sys
from .scanner import *

class NeurLang:
    def __init__(self, test=False, path = None):
        if path != None:
            self.test = test
            self.args = sys.argv

            self.start(self.args)
        else:
            self.start(path)
    def start(self, path):

        if self.test == True:
            pass
        elif len(path) == 2:
            self.run(self.load_file(path[1]))
        else:
            print("test-case-action")

    def load_file(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def run(self, source):

        scanner = Scanner(source)
