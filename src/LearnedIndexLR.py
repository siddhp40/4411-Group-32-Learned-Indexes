# LearnedIndexLR.py
# IMPLEMENTS LINEAR REGRESSION FOR A SINGLE COUNTRY
# https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/
# https://www.w3schools.com/python/python_ml_linear_regression.asp

class LearnedIndexLR:
    def __init__(self, countryCode: str, countryData: list):
        self.countryCode = countryCode
        self.data = countryData # CONSIDER SORTING IN ASC. ORDER

        # THESE WILL BE USE FOR OUR [mx + b] LINEAR REGRESSION
        self.m = 0
        self.b = 0

        self.maxError = 0.0
        self.minError = 9999999999.9 # ANY HIGH VALUE
        self.maxPositiveError = 0.0
        self.maxNegativeError = 0.0

    # LOAD THEN SORT INTO KEYS AND VALUES
    def trainModel(self):
        # SEPARATE THE YEARS AND VALUES
        dataYears, dataValues = zip(*self.data)

        # CALCULATE AVERAGES FOR LINEAR REGRESSION FORMULA
        numberOfPoints = len(dataYears)
        # x, y => years, values
        avgYears = sum(dataYears) / numberOfPoints
        avgValues = sum(dataValues) / numberOfPoints

        # CALCULATE THE SLOPE
        numeratorSum = 0
        denominatorSum = 0
        for year, value in self.data:
            xCalc = year - avgYears
            # FORMULA FOR SLOPE IN DOCUMENT
            numeratorSum += xCalc * (value - avgValues)
            denominatorSum += xCalc * xCalc
        self.m = numeratorSum / denominatorSum

        # CALCULATE THE INTERCEPT 
        self.b = avgValues - self.m * avgYears

    # OUTPUTS SLOPE AND INTERCEPT VALUES TO TERMINAL
    def printSlopeIntercept(self):
        print("\n" + self.countryCode)
        print("\tself.m:\t" + str(self.m))
        print("\tself.b:\t" + str(self.b))

    # USE [year] TO PREDICT POSITION BY [mx + b]
    def predict(self, year: int):
        returnValue = self.m * year + self.b
        return returnValue
    
    # GETS THE MAX POSSIBLE ERROR RANGES
    def calculateErrorRanges(self):
        for (year, actualValue) in self.data:
            predictedValue = self.predict(year)
            error = predictedValue - actualValue

            # GET THE MAX ERROR IN POSITIVE AND NEGATIVE
            self.maxError = max(self.maxError, abs(error))
            self.minError = min(self.minError, abs(error))


            # NOW THE MAX ERROR IN POSITIVE OR NEGATIVE
            if error > 0:
                self.maxPositiveError = max(self.maxPositiveError, error)
            else:
                self.maxNegativeError = min(self.maxNegativeError, error)

    # OUTPUT ALL CALCULATED ERROR RANGES TO COMMAND LINE
    def printErrorRanges(self):
        print("MAX ABSOLUTE ERROR: " + str(self.maxError))
        print("MIN ABSOLUTE ERROR: " + str(self.minError))
        print("MAX POSITIVE ERROR: " + str(self.maxPositiveError))
        print("MAX NEGATIVE ERROR: " + str(self.maxNegativeError))



