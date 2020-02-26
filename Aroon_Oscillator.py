
class AroonOscillator:
    def __init__(self, high, low, period=14):
        self.high = high
        self.low = low
        self.period = period
        self.bars = len(high)
        self.aroc = []

    def set(self):
        if self.bars < 0:
            return False
        HighBarBuffer = []
        LowBarBuffer = []

        for i in range(0, self.period - 1):
            HighBarBuffer.append(0.0)
            LowBarBuffer.append(0.0)
            self.aroc.append(0.0)

        for i in range(self.period - 1, self.bars):
            HighBarBuffer.append(self.iHighest(self.period, i))
            LowBarBuffer.append(self.iLowest(self.period, i))
            self.aroc.append(100.0 * (HighBarBuffer[i] - LowBarBuffer[i]) / self.period)
        return True

    def get(self):
        return self.aroc

    def get_period(self):
        return self.period

    def iHighest(self, count, index):
        high = 0.0
        result = index - count + 1
        for i in range(index - count + 1, index + 1):
            if high < self.high[i]:
                high = self.high[i]
                result = i
        return float(result)

    def iLowest(self, count, index):
        low = 999999999
        result = index - count + 1
        for i in range(index - count + 1, index + 1):
            if low > self.low[i]:
                low = self.low[i]
                result = i
        return float(result)


