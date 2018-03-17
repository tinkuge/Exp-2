import pandas as pan
import numpy as num
import matplotlib.pyplot as plot
import hashlib as hash
import math
import time
data = pan.read_csv('outputwireless-logs-20120409.DHCP_ANON.csv')

minTime = min(data["startTime"])

maxTime = max(data["startTime"])

d = dict()

interval = 900

n =  0 #number of bins

for i in range(minTime , maxTime + 1, interval): #initialize the dictionary
    d[i] = 0
    n +=1


for i in data["startTime"]: #For each entry, determine which bin it must be placed into
    diff = i - minTime
    bin = math.floor(diff/interval) #Find the bin number
    k = minTime+(bin*interval)      #get the time associated with bin number
    d[k] += 1

x = list(sorted(d.keys()))
y = [value for (key,value) in sorted(d.items())]

maxActivity = max(d, key = lambda k: d[k])  #Find the bin with max encounters
minActivity = min(d, key = lambda k: d[k])  #Find the bin with min encounters
print("Time of maximum activity is "+ str(maxActivity))
print("Time of minimum activity is "+ str(minActivity))


plot.plot(x,y)
plot.xlabel('Time in seconds')
plot.ylabel('Number of events')
plot.title('Time series plot at 15 min interval')
plot.show()
