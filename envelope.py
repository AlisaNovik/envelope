import random

class Envelope:
    def __init__(self):
        """
        creat an envelope with random amount of money
        """
        self.money = random.randint(500)
        self.used = False


