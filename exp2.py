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
for i in range(minTime , maxTime + 1, interval):
    d[i] = 0
    n +=1

print(n)


for i in data["startTime"]:

    #print(i)
    diff = i - minTime
    #print(diff)
    bin = math.floor(diff/interval)
    #print(bin)
    k = minTime+(bin*interval)
    d[k] += 1

x = list(sorted(d.keys()))
y = [value for (key,value) in sorted(d.items())]

maxActivity = max(d, key = lambda k: d[k])
minActivity = min(d, key = lambda k: d[k])
print("Time of maximum activity is "+ str(maxActivity))
print("Time of minimum activity is "+ str(minActivity))


plot.plot(x,y)
plot.xlabel('Time in seconds')
plot.ylabel('Number of events')
plot.title('Time series plot at 15 min interval')
plot.show()
