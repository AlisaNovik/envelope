from  abc import ABC
class abstractStrategy(ABC):
    def display(self):
        pass
    def play(self):
        pass
class BaseStrategy(abstractStrategy):
    class BaseStrategy:
        def __init__(self, envelopes):
            self.envelopes = envelopes

        def play(self):
            last_en = self.envelopes[0]
            for i in range(100):
                if self.envelopes[i].used == False:
                    print("the money in the envelope:" + self.envelopes[i].money)
                    answer = input("do you want to keep this envelope - yes/no?")
                    if answer == "no":
                        last_en = self.envelopes[i]
                    if answer == "yes":
                        self.envelopes[i].used = True
                        return self.envelopes[i]
            return last_en
    def display(self):
        return "player chooses envelope"


class Automatic_BaseStrategy(abstractStrategy):
    def __init__(self, envelopes):
        self.envelopes = envelopes


class N_max_strategy(abstractStrategy):
    def __init__(self, envelopes, N = None):
        self.envelopes = envelopes
        if N is None:# set defualt
            self.N = 3
        else:
            self.N = N

    def display(self):
        return f"finding the first [{self.N}]'s envelopes with most money"

    def play(self):
        max = 0  # most money
        num = 0  # number of envelopes with more money then previous
        for i in self.envelopes:
            if num >= self.N:
                break
            if i > max:
                max = i
                num += 1
            self.envelopes[i].used = True
        return max


class More_then_N_percent_group_strategy(abstractStrategy):
    def __init__(self, envelopes, percent):
        self.envelopes = envelopes
        self.percent = percent
