import numpy as np

class RSI:
    def __init__(self, array=[], period=14):
        self.array = array
        self.period = period
        self.rsi = []

    def set(self):
        if len(self.array) <= self.period:
            return False
        PosBuffer = []
        NegBuffer = []
        self.rsi.append(0.0)
        PosBuffer.append(0.0)
        NegBuffer.append(0.0)
        SumP = 0.0
        SumN = 0.0
        for i in xrange(1, self.period + 1):
            self.rsi.append(0.0)
            PosBuffer.append(0.0)
            NegBuffer.append(0.0)
            diff = self.array[i] - self.array[i - 1]
            if diff > 0:
                SumP += diff
            if diff < 0:
                SumN -= diff
        PosBuffer[self.period] = SumP / self.period
        NegBuffer[self.period] = SumN / self.period

        if NegBuffer[self.period] != 0.0:
            temp = 1.0 + PosBuffer[self.period] / NegBuffer[self.period]
            self.rsi[self.period] = 100.0 - (100.0 / temp)
        else:
            if PosBuffer[self.period] != 0.0:
                self.rsi[self.period] = 100.0
            else:
                self.rsi[self.period] = 50.0
        for i in xrange(self.period + 1, len(self.array)):
            diff = self.array[i] - self.array[i - 1]
            pos = 0.0
            neg = 0.0
            if diff > 0.0:
                pos = float(diff)
            if diff < 0.0:
                neg = float(-diff)

            PosBuffer.append((PosBuffer[i - 1] * (self.period - 1) + pos) / self.period)
            NegBuffer.append((NegBuffer[i - 1] * (self.period - 1) + neg) / self.period)
            if NegBuffer[i] != 0.0:
                self.rsi.append(100.0 - 100.0 / (1.0 + PosBuffer[i] / NegBuffer[i]))
            else:
                if PosBuffer[i] != 0.0:
                    self.rsi.append(100.0)
                else:
                    self.rsi.append(50.0)
        return True

    def get(self):
        return self.rsi

    def get_period(self):
        return self.period


