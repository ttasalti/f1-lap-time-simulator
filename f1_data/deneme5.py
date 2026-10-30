###butun pistler icin calisacak kod gelistirilecek
###pist pist lastik yipranmasi ve hiz farki eklenecek
##allRaces Degiskenin entegrasyonu saglanmali
from copy import deepcopy
mediumDs=   [610,343,507,82,340,377,486,610,374,277,291,263,58,217,294,196,596,48,352,302,309,352]
hardDs=     [1230,669,865,396,499,766,1010,1262,749,591,569,547,431,421,584,327,1302,415,830,804,362,521]
softDr=     [160,120,140,70,160,70,90,170,80,90,40,100,90,100,50,60,90,80,210,90,100,130]
mediumDr=   [120,80,70,40,100,50,70,130,60,60,30,70,60,60,40,40,70,60,140,60,70,100]
hardDr=     [100,50,50,30,70,40,40,90,40,50,20,50,40,50,30,20,30,50,90,40,50,60]
class race:
    fuelBonus=int
    pitTime=int
    raceLen=int
    lapTime=int
    tyreData=list()

class tyre:
    name=str
    ds=int
    dr=int
    dc=int
allRaces=list()
for i in range(0,len(mediumDs)):
    theRace=race()
    theRace.fuelBonus=60
    theRace.pitTime=17650
    theRace.raceLen=53
    theRace.lapTime=100000

    tyres=list()

    soft=tyre()
    soft.name='s'
    soft.ds=0
    soft.dr=softDr[i]
    soft.dc=100
    tyres.append(soft)

    medium=tyre()
    medium.name='m'
    medium.ds=mediumDs[i]
    medium.dr=mediumDr[i]
    medium.dc=80
    tyres.append(medium)

    hard=tyre()
    hard.name='h'
    hard.ds=hardDs[i] 
    hard.dr=hardDr[i]
    hard.dc=70
    tyres.append(hard)
    theRace.tyreData=deepcopy(tyres)
    allRaces.append(theRace)
class possibleResults:
    def __init__(self,pitNo,stints,tyreList):
        self.stints=list()
        self.pitNo=deepcopy(pitNo)
        self.stints=deepcopy(stints)
        self.tyreList=deepcopy(tyreList)
    pitNo=list()
    totalTime=int
    stints=list()
    tyreList=list()
class stint:
    def __init__(self):
        self.lapTimes=list()
        self.usedTyre=-1
        self.tyreCompound=tyre()
        self.stintTime=list()
    def addLapTimes(self,lapTimes):
        self.lapTimes=list()
        self.lapTimes=deepcopy(lapTimes)
    tyreCompound=tyre()
    usedTyre=-1
    stintTime=int
    lapTimes=list()
class raceStrategy:
    def __init__(self,tyresList):
        self.tyres=deepcopy(tyresList)
    tyres=list()
    def addAll(self,possibleStrategies,fastestStrategy,pitWindow):
        self.possibleStrategies=deepcopy(possibleStrategies)
        self.fastestStrategy=deepcopy(fastestStrategy)
        self.pitWindow=deepcopy(pitWindow)
    possibleStrategies=list()
    fastestStrategy=stint()
    pitWindow=list()




possibleStrategies=["sh","ms","mh","sm","sms","shs","mss","msm","mhs","smm","smh"]
strategies=list()
pitWindowStintsForAllStrategies=list()
for tyres in possibleStrategies:
    t=list()
    for theTyre in tyres:
        if theTyre=='s':
            t.append(soft)
        elif theTyre=='m':
            t.append(medium)
        elif theTyre=='h':
            t.append(hard)
        else:
            print("Unknown tyre error")
            exit()
    strategy=raceStrategy(t)
    strategies.append(strategy)
possibleResultsForAllStrategies=list()
fastestPitStopForAllStrategies=list()
pitWindowForAllStrategies=list()
dd=list()
for strategy in strategies:
    stint1LapTimes=list()
    possibleResultsForTheStrategy=list()
    stint1=stint()
    stint1.tyreCompound=strategy.tyres[0]
    for stint1LapNo in range(1,theRace.raceLen-len(strategy.tyres)+2):        
        stint1.usedTyre+=1
        tl=theRace.lapTime+stint1.tyreCompound.ds
        deg=stint1.tyreCompound.dr*((1000+stint1.tyreCompound.dc)**(stint1.usedTyre))/(1000**(stint1.usedTyre))
        dl=tl+deg
        stint1LapTimes.append(dl-theRace.fuelBonus*(stint1LapNo-1))
        stint2LapTimes=list()
        stint2=stint()
        stint2.tyreCompound=strategy.tyres[1]
        for stint2LapNo in range(stint1LapNo+1,theRace.raceLen-len (strategy.tyres)+3):
            stint2.usedTyre+=1
            tl=theRace.lapTime+stint2.tyreCompound.ds
            deg=stint2.tyreCompound.dr*((1000+stint2.tyreCompound.dc)**(stint2.usedTyre))/(1000**(stint2.usedTyre))
            dl=tl+deg
            stint2LapTimes.append(dl-theRace.fuelBonus*(stint2LapNo-1))
            stint3LapTimes=list()
            if len(strategy.tyres)==3:
                stint3=stint()
                stint3.tyreCompound=strategy.tyres[2]
                for stint3LapNo in range(stint2LapNo+1,theRace.raceLen+1): 
                    stint3.usedTyre+=1
                    tl=theRace.lapTime+stint3.tyreCompound.ds
                    deg=stint3.tyreCompound.dr*((1000+stint3.tyreCompound.dc)**(stint3.usedTyre))/(1000**(stint3.usedTyre))
                    dl=tl+deg
                    stint3LapTimes.append(dl-theRace.fuelBonus*(stint3LapNo-1))
                stint1.addLapTimes(stint1LapTimes)
                stint2.addLapTimes(stint2LapTimes)
                stint3.addLapTimes(stint3LapTimes)
                stint1.stintTime=sum(stint1LapTimes)+theRace.pitTime
                stint2.stintTime=sum(stint2LapTimes)+theRace.pitTime
                stint3.stintTime=sum(stint3LapTimes)
                stints=list()
                stints.append(stint1)
                stints.append(stint2)
                stints.append(stint3)
                pitLapNo=list()
                pitLapNo.append(stint1LapNo)
                pitLapNo.append(stint2LapNo)
                pr=possibleResults(pitLapNo,stints,strategy.tyres)
                pr.totalTime=stint1.stintTime+stint2.stintTime+stint3.stintTime
                possibleResultsForTheStrategy.append(pr)
        if len(strategy.tyres)==2:
            stint1.addLapTimes(stint1LapTimes)
            stint2.addLapTimes(stint2LapTimes)
            stints=list()
            stints.append(stint1)
            stints.append(stint2)
            stint1.stintTime=sum(stint1LapTimes)+theRace.pitTime
            stint2.stintTime=sum(stint2LapTimes)
            pitLapNo=list()
            pitLapNo.append(stint1LapNo)
            pr=possibleResults(pitLapNo,stints,strategy.tyres)
            pr.totalTime=stint1.stintTime+stint2.stintTime
            possibleResultsForTheStrategy.append(pr)
    possibleResultsForTheStrategy.sort(key=lambda x:x.totalTime)
    fastestPitStopForAllStrategies.append(possibleResultsForTheStrategy[0])
    possibleResultsForAllStrategies.append(possibleResultsForTheStrategy)
    pitWindowForTheStrategy=list()
    pitWindowStintsForTheStrategy=list()
    for possibleResult in possibleResultsForTheStrategy:
        if possibleResult.totalTime-possibleResultsForTheStrategy[0].totalTime<3000:
            pitWindowForTheStrategy.append(deepcopy(possibleResult.pitNo))
            pitWindowStintsForTheStrategy.append(deepcopy(possibleResult))
        else:
            break
    pitWindowStintsForAllStrategies.append(pitWindowStintsForTheStrategy)
    d=list()
    if len(strategy.tyres)==3:
        minimumForFirstStop=200
        maximumForFirstStop=0
        minimumForSecondStop=200   
        maximumForSecondStop=0
        firstStop=list()
        secondStop=list()
        for pit in pitWindowForTheStrategy:
            if pit[0]<minimumForFirstStop:
                minimumForFirstStop=pit[0]
            if pit[0]>maximumForFirstStop:
                maximumForFirstStop=pit[0]
            if pit[1]<minimumForSecondStop:
                minimumForSecondStop=pit[1]
            if pit[1]>maximumForSecondStop:
                maximumForSecondStop=pit[1]
        firstStop.append(minimumForFirstStop)
        firstStop.append(maximumForFirstStop)
        secondStop.append(minimumForSecondStop)
        secondStop.append(maximumForSecondStop)
        d.append(firstStop)
        d.append(secondStop)
        dd.append(d)
    if len(strategy.tyres)==2:
        minimumForFirstStop=200
        maximumForFirstStop=0 
        for pit in pitWindowForTheStrategy:
            if pit[0]<minimumForFirstStop:
                minimumForFirstStop=pit[0]
            if pit[0]>maximumForFirstStop:
                maximumForFirstStop=pit[0]
        firstStop=list()
        firstStop.append(minimumForFirstStop)
        firstStop.append(maximumForFirstStop)
        d.append(firstStop)
        dd.append(d) 
    pitWindowForAllStrategies.append(pitWindowForTheStrategy)
fastestPitStopForAllStrategies.sort(key=lambda x:x.totalTime)
for i in range(0,len(strategies)):
    strategies[i].addAll(pitWindowStintsForAllStrategies[i],fastestPitStopForAllStrategies[i],dd[i])
for strategy in fastestPitStopForAllStrategies:
    for theTyre in strategy.tyreList:
        print(theTyre.name,end="")
    print(end="\t")
    print(" ",int(strategy.totalTime-fastestPitStopForAllStrategies[0].totalTime)//1000,end="\t")
    for pit in strategy.pitNo:
        print(pit,end=",")
    print(" ")
print('')