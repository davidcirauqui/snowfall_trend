class snowFall:
    def __init__(self, startDate, endDate, startDepth, endDepth):
        self.startDate = startDate
        self.endDate = endDate
        self.duration = abs((startDate - endDate).days) + 1
        
        self.startDepth = startDepth
        self.endDepth = endDepth
        self.newSnow = endDepth - startDepth
        
        self.averageRate = self.newSnow / self.duration
        