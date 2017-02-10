class Test:
    
    #expected output arranged by array of array of tuples showing xy coordinates of each word's letter
    expectedOutput = [
        #dolphin
        [(13,17), (14,16),(15,15),(16,14),(17,13),(18,12),(19,11)],
        #finneaus
        [(30,30),(31,30),(32,30),(33,30),(34,30),(35,30),(36,30),(37,30)],
        #deliverable
        [(48,4),(48,5),(48,6),(48,7),(48,8),(48,9),(48,10),(48,11),(48,12),(48,13),(48,14)],
        #programmer
        [(47,38),(46,38),(45,38),(44,38),(43,38),(42,38),(41,38),(40,38),(39,38),(38,38)],
        #email
        [(3,5),(4,6),(5,7),(6,8),(7,9)],
        #computer
        [(1,25),(1,24),(1,23),(1,22),(1,21),(1,20),(1,19),(1,18)],
        #mobile
        [(13,35),(12,34),(11,33),(10,32),(9,31),(8,30)],
        #portal
        [(24,43),(24,44),(24,45),(24,46),(24,47),(24,48)],
        #strategy
        [(32,15),(32,14),(32,13),(32,12),(32,11),(32,10),(32,9),(32,8)],
        #jorts
        [(16,0),(17,0),(18,0),(19,0),(20,0)]
    ]

    def run(self, output):
        checkCounter = 0
        for row in output:
            for expectedRow in self.expectedOutput:
                if row == expectedRow:
                    checkCounter += 1
        if checkCounter == len(self.expectedOutput):
            print("Test passed")
            return
        print("Test failed")
        