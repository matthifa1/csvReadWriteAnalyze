import os, signal, datetime
import json
import sys
import requests
import csv
#import matplotlib.pyplot as plt

class TestClass(object):

    __internalVar__ = "hallo, interneVar"

    def __init__(self, initVar= "Test"):
        self.testVar = initVar

    def printVariables(self):
        try:
            print(self.testVar)
        except:
            sys.exit(1)

class Request(object):
    def __init__(self):
        self.curStockValue = -1000.0

    def ShowRequest(self):
        try:
            response = requests.get(
              'https://api.github.com/search/repositories',
              params={'q': 'requests+language:python'},
            )
            print(response.json)
        except:
            sys.exit(1)

    def GetValue(self):
        #Todo Get a real value
        self.curStockValue = 2980.12

class CsvHandling(object):
    def __init__(self, initPathToCsv= "C:\\Users\\falger\\Downloads\\", initFileName = "data.csv"):
        self.pathToCsv = initPathToCsv
        self.fileName = initFileName

    def WriteNewValueToCsv(self, valueToWrite):
        with open(self.pathToCsv + self.fileName, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(now)
            spamwriter.writerow([valueToWrite, now])

    def ShowReadData(self):
        with open(self.pathToCsv + self.fileName, newline='') as csvfile:
            reader = csv.reader(csvfile)
            print("-------------------------------")
            print("-Show Csv-Content--------------")
            print("-------------------------------")
            for row in reader:
                print(', '.join(row))
            print("-------------------------------")
            print("-End of File ------------------")
            print("-------------------------------")

    def ReadCsvToList(self):
        with open(self.pathToCsv + self.fileName, newline='') as csvfile:
            reader = csv.reader(csvfile)
            readList = list()
            for row in reader:
                try:
                    value = float(row[0])
                    readList.append(value)
                except:
                    print("Error: couldn't read the float value from the following row:" + row[0])
            return readList
               
    def AddNewValueToCsv(self, valueToWrite):
       with open(self.pathToCsv + self.fileName, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(now)
            spamwriter.writerow([valueToWrite, now])

object1 = CsvHandling()

print("write new Value to csv")
object1.WriteNewValueToCsv("2812.0")
print("write new Value 1 to csv")
object1.AddNewValueToCsv("2932.0")
print("write new Value to csv")
object1.AddNewValueToCsv("2321.0")
print("write new Value 1 to csv")
object1.AddNewValueToCsv("2789.0")
print(object1.ReadCsvToList())
valueList = object1.ReadCsvToList()
#plt.plot(valueList)
#plt.show()

object1.ShowReadData()
print(object1.ReadCsvToList())
#object1 = Request()
#object1.ShowRequest()
#object1 = TestClass()
#object2 = TestClass("testdesanderenKonstruktors")

#print(object1.testVar)
#print(object2.testVar)
#print(object1.__internalVar__)
#print(os.__all__)
#help(os.kill)

#pid = os.getpid()
#print(pid)