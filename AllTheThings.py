from observable import Observable
from observer import Observer

class Commander(Observer):
    answers = []
    scanners = []

    def __init__(self, puzzleToSearch, wordsToSearchFor):
        self.puzzleToSearch = puzzleToSearch
        self.wordsToSearchFor = wordsToSearchFor

    def test(self):
        print self.wordsToSearchFor[0]

    def update(self, *args, **kwargs):
        print("Word received: {0}".format(args))

class Scanner():

    def __init__(self, direction, puzzle, wordsToFind):
        self.observable = Observable()
        self.direction = direction
        self.puzzle = puzzle
        self.puzzleRows = len(puzzle)
        self.puzzleColumns = len(puzzle[0])
        self.wordsToFind = wordsToFind

    def scan_for_words(self):
        for row, letters in enumerate(self.puzzle):
            for column, letter in enumerate(letters):
                for word in self.__get_first_letter_matches(letter):
                    if self.__enough_room_for_word(len(word), row, column):
                        if self.__search_for_word(word, row, column):
                            self.observable.update_observers(word)

    def register(self, observer):
        self.observable.register(observer)

    def __enough_room_for_word(self, lengthOfWord, row, column):
        if row + lengthOfWord * self.direction[1] > self.puzzleColumns:
            return False
        elif column + lengthOfWord * self.direction[0] > self.puzzleRows:
            return False
        else:
            return True

    def __get_first_letter_matches(self, letter):
        matches = []
        for word in self.wordsToFind:
            if word[0] == letter:
                matches.append(word)
        return matches

    def __search_for_word(self, word, row, column):
        for position, letter in enumerate(word[1:]):
            rowOffset = (position + 1) * self.direction[1]
            columnOffset = (position + 1) * self.direction[0]
            if not self.puzzle[row + rowOffset][column + columnOffset] == letter:
                return False
        return True

