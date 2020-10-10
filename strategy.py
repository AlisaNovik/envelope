

class BaseStrategy:
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def play(self):
        last_en = self.envelopes[0]
        for i in range(100):
            if self.envelopes[i].used==False:
                print("the money in the envelope:"+self.envelopes[i].money)
                answer=input("do you want to keep this envelope - yes/no?")
                if answer=="no":
                        last_en=self.envelopes[i]
                if answer=="yes":
                    self.envelopes[i].used = True
                    return self.envelopes[i]
        return last_en