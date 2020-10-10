from BaseStrategy import BaseStrategy
import random
class Automatic_BaseStrategy:
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def play(self):
        int = random.randint(0,99)
        while self.envelopes[int].used==True:
            int = random.randint(0, 99)
        return self.envelopes[int]

    def display(self):
        return "the random envelope that was chosen is: "+self.play()