
class CCI:
    def __init__(self, high, low, close, period=14):
        self.high = high
        self.low = low
        self.close = close
        self.period = period
        self.cci = []

    def set(self):

        if self.period <= 1:
            return False

        if len(self.high) <= self.period:
            return False

        ExtPriceBuffer = []
        ExtMovBuffer = []

        for i in range(self.period):
            self.cci.append(0.0)
            ExtPriceBuffer.append((self.high[i] + self.low[i] + self.close[i]) / 3)
            ExtMovBuffer.append(0.0)

        pos = self.period
        for i in range(pos, len(self.high)):
            ExtPriceBuffer.append((self.high[i] + self.low[i] + self.close[i]) / 3)
            ExtMovBuffer.append(self.simple_ma(i, self.period, ExtPriceBuffer))
        dMul = 0.015 / self.period
        pos = self.period - 1
        i = pos
        while i < len(self.high):
            dSum = 0.0
            k = i + 1 - self.period
            while k <= i:
                dSum += abs(ExtPriceBuffer[k] - ExtMovBuffer[i])
                k += 1
            dSum *= dMul
            if dSum == 0.0:
                if i >= len(self.cci):
                    self.cci.append(0.0)
                else:
                    self.cci[i] = 0.0
            else:
                if i >= len(self.cci):
                    self.cci.append((ExtPriceBuffer[i] - ExtMovBuffer[i]) / dSum)
                else:
                    self.cci[i] = (ExtPriceBuffer[i] - ExtMovBuffer[i]) / dSum
            i += 1
        return True

    def get(self):
        return self.cci

    def get_period(self):
        return self.period

    def simple_ma(self, position, period, price):
        result = 0.0
        if position >= period - 1 and period > 0:
            for i in range(period):
                result += price[position - i]
            result /= period
        return result

