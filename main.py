from test import Test
from AllTheThings import Scanner
from AllTheThings import Commander

class Start:
    directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

    def run(self, wordSearch, wordBank):
        commander = Commander(wordSearch, wordBank)
        for direction in self.directions:
            scanner = Scanner(direction, wordSearch, wordBank)
            scanner.register(commander)
            scanner.scan_for_words()
        
        #be sure to call test.run in order to see if your code passes
        Test().run(commander.answers)