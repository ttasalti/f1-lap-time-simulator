import pandas as pd
class classdataFrame:
    race=list()
    def __init__(self,lap):
        self.lap=lap
        lap_d= list()
        for driver in self.lap:
            data={
            'driverNo':                     driver.driverNo,
            'DNF':                          driver.DNF,
            'DRSRule':                      driver.DRSRule,
            'DRSSituation':                 driver.DRSSituation,
            'FP2':                          driver.FP2,
            'allTime':                      driver.allTime,
            'boolCheckDNF':                 driver.boolCheckDNF,
            'deltaFP2':                     driver.deltaFP2,
            'deltaQualify':                 driver.deltaQualify,
            'forecastedPrimeTime':          driver.forecastedPrimeTime,
            'gridPosition' :                driver.gridPosition,
            'lapCount' :                    driver.lapCount,
            'lapTimeVariability' :          driver.lapTimeVariability,
            'newLap' :                      driver.newLap,
            'position' :                    driver.position,
            'qualify' :                     driver.qualify,
            'spin' :                        driver.spin,
            'spinCounter' :                 driver.spinCounter,
            'timeDifferencePreviousCar' :   driver.timeDifferencePreviousCar
            }
            lap_d.append(data)
        self.race.append(lap_d)
        race_pd=pd.DataFrame(self.race)
        print()