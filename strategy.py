from  abc import ABC
import random
class abstractStrategy(ABC):
    """
    abstract class all other classes inherit from
    """
    def display(self):
        pass
    def play(self):
        pass
class BaseStrategy(abstractStrategy):
    # user select manually envelopes
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def play(self):
        last_en = self.envelopes[0]
        for i in range(100):
            if self.envelopes[i].used == False:
                print("the money in the envelope:" + self.envelopes[i].money)
                self.envelopes[i].used = True
                answer = input("do you want to keep this envelope - yes/no?")
                if answer == "no":
                    last_en = self.envelopes[i]
                if answer == "yes":
                    return self.envelopes[i]
        return last_en
    def display(self):
        return "player chooses envelope"


class Automatic_BaseStrategy:
    # random selection of envelop
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def play(self):
        int = random.randint(0,99)
        while self.envelopes[int].used==True:
            int = random.randint(0, 99)
        return self.envelopes[int]

    def display(self):
        return "select random envelop"


class N_max_strategy(abstractStrategy):
    # return envelope after N max values (defualt N=3)
    def __init__(self, envelopes, N = None):
        self.envelopes = envelopes
        if N is None:# set defualt
            self.N = 3
        else:
            self.N = N

    def display(self):
        return f"finding the first [{self.N}] envelopes with most money"

    def play(self):
        max = 0  # most money
        num = 0  # number of envelopes with more money then previous
        e = self.envelopes[0]
        for i in self.envelopes:
            if num >= self.N:
                break
            if (i.money > max) and (i.used == False):
                max = i.money
                e = i
                num += 1
            self.envelopes[i].used = True
        return e


class More_then_N_percent_group_strategy(abstractStrategy):
    # return envelope with more money that in the highest of N% group
    def __init__(self, envelopes, percent):
        self.envelopes = envelopes
        self.percent = percent # default is 0.25%

    def play(self):
        num = int(len(self.envelopes)*self.percent)
        max = 0
        for i in range(num):
            if self.envelopes[i].money > max:
                max = self.envelopes[i].money
            self.envelopes[i].used = True
        for j in range(num, len(self.envelopes)):
            if (self.envelopes[j].money > max) and (self.envelopes[j].used == False):
                return self.envelopes[j]
            self.envelopes[j].used = True
        return self.envelopes
    def display(self):
        return "find the envelope with more money that in the highest of N% group"
