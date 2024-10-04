import snowFall as sf

class snowSeason:
    
    def __init__(self, snowDepth, dates):
        self.dates = dates
        
        self.snowDepth = snowDepth
        self.snowFalls = self.detectSonwFalls()
        self.totalAccumulatedSnow = self.computeTotalAccumulatedSnow()
        
        self.startDate = self.startOfSeasonDate()
        self.endDate = self.endOfSeasonDate()
        self.duration = abs((self.startDate - self.endDate).days) + 1

        
        
    def detectSonwFalls(self):
        """
        function to detect snowfalls within a season, based on the increase of the snow depth
        """

        snowFalls = []
        itwasSnowing = False
        itsSnowing = False

        # for all days in the season
        for i in range(1, len(self.snowDepth)):
            itsSnowing = self.snowDepth[i - 1] < self.snowDepth[i]    # if snow depth increases, it is snowing
            if (itsSnowing == True) :         # if it is snowing but previously was not, a snowfall has started
                if (itwasSnowing == False):
                    startIdx = i
                    startDepth = self.snowDepth[i-1]

            elif (itsSnowing == False):      # if it is not snowing but previously was, a snowfall has stopped
                if (itwasSnowing == True):
                    endIdx = i - 1
                    endDepth = self.snowDepth[i - 1]
                    # store values corresponding to the registered snowfall
                    snowFalls.append(sf.snowFall(self.dates[startIdx], self.dates[endIdx], startDepth, endDepth))
                    

            itwasSnowing = itsSnowing     # in next iteration it was snowing just as in current iteration was

        return snowFalls
    
    
    def computeTotalAccumulatedSnow(self):
        """
        function to compute the total accumulated snow by adding all snow falls within a season
        """
        
        accumulatedSnow = 0
        for snowfall in self.snowFalls:
            accumulatedSnow = accumulatedSnow + snowfall.newSnow
            
        return accumulatedSnow
    
    
    
    def startOfSeasonDate(self):
        """
        function to check when has the snow season started, considering the season to start
        when the snow depth is at least 20 cm
        """
        
        idx = 0
        # run backwards in order to retain the first day with 20cm
        for i in range(len(self.snowDepth) - 1, -1, -1):
            if self.snowDepth[i] >= 20:
                idx = i
        
        return self.dates[idx]
    
    
    def endOfSeasonDate(self):
        """
        function to check when has the snow season stopped, considering the season to end
        when the snow depth is less than 20 cm
        """
        
        idx = 0
        for i in range(len(self.snowDepth)):
            if self.snowDepth[i] >= 20:
                idx = i
            
        return self.dates[idx]
