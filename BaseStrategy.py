

class BaseStrategy:
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def play(self):
        for i in range(100):
            print(self.envelopes[i])
            answer=input("do you want to keep this envelope - yes/no?")
            if answer=="yes":
                return self.envelopes[i]
        return self.envelopes[99]