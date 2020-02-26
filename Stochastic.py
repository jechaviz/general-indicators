
class stochastic:
    def __init__(self, high=[], low=[], close=[], open = [], K_period = 14, D_period = 14, smoothing = 3):
        self.high = high
        self.low = low
        self.close = close
        self.open = open
        self.K_period = K_period
        self.D_period = D_period
        self.smoothing = smoothing
        self.K = []
        self.D = []

    def calc_K(self, period):
        minLows = self.get_rolling_min(self.low, period)
        maxHighs = self.get_rolling_max(self.high, period)
        result = []
        for i in xrange(0, len(self.open)):
            result.append(100 * (self.close[i] - minLows[i]) / (maxHighs[i] - minLows[i]))
        return result

    def set(self):
        k_list = self.calc_K(self.D_period)
        self.D = self.get_rolling_mean(k_list, self.smoothing)
        if self.K_period == self.D_period:
            self.K = k_list
        else:
            self.K = self.calc_K(self.K_period)

    def get_K(self):
        return self.K

    def get_D(self):
        return self.D

    def get_K_period(self):
        return self.K_period

    def get_D_period(self):
        return self.D_period

    def get_smoothing(self):
        return self.smoothing

    def get_rolling_min(self, List, period):
        if period <= 1:
            return List
        result = []
        for i in xrange(0, len(List)):
            temp = List[i]
            end = i - period
            if i - period < -1:
                end = -1
            for j in xrange(i, end, -1):
                if temp > List[j]:
                    temp = List[j]
            result.append(temp)
        return result

    def get_rolling_max(self, List, period):
        if period <= 1:
            return List
        result = []
        for i in xrange(0, len(List)):
            temp = List[i]
            end = i - period
            if i - period < -1:
                end = -1
            for j in xrange(i, end, -1):
                if temp < List[j]:
                    temp = List[j]
            result.append(temp)
        return result

    def get_rolling_mean(self, List, period):
        if period <= 1:
            return List
        result = []
        for i in xrange(0, len(List)):
            end = i - period
            if i - period < -1:
                end = -1
            temp = 0
            for j in xrange(i, end, -1):
                temp += List[j]
            temp = temp / period
            result.append(temp)
        return result

