# USED TO TIME HOW LONG SPECIFIC METHODS TAKE TO EXECUTE

import time 
from LRManager import LRManager

def main():
    # WILL BE CHANGED TO GET FROM COMMAND LINE
    filepath = "../data/globalYouthUnemployment.csv"
    indexColumn = 2

    print("TIMING MODULE START")

    # CREATE MANAGER (NO NEED TO BE TIMED)
    manager = LRManager(filepath, indexColumn)

    # GETS ALL KEYS FROM FILE, THEN SORTS IN ASC. ORDER
    # WILL BE TIMED SINCE OTHER INDEXING IMPLEMENTATION NEEDS TO READ IN DATA
    timeStart = time.time()
    manager.processInputFile()
    timeEnd = time.time()
    resultingTime = timeEnd - timeStart
    print("PROCESS INPUT TIME: " + str(resultingTime) + " SECONDS.")

if __name__ == "__main__":
    main()
