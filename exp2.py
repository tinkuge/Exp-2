import pandas as pan
import numpy as num
import matplotlib.pyplot as plot
import hashlib as hash
import math
data = pan.read_csv('outputwireless-logs-20120409.DHCP_ANON.csv')

minTime = min(data["startTime"])
print(minTime)

maxTime = max(data["startTime"])
print(maxTime)

d = dict()

n =  0 #number of bins
for i in range(minTime , maxTime + 1, 900):
    d[i] = 0
    n +=1

print(n)


for i in data["startTime"]:

    #print(i)
    diff = i - minTime
    #print(diff)
    bin = math.floor(diff/900)
    #print(bin)
    k = minTime+(bin*900)
    d[k] += 1

x = list(sorted(d.keys()))
y = [value for (key,value) in sorted(d.items())]

plot.plot(x,y)
plot.xlabel('Time in seconds')
plot.ylabel('Number of events')
plot.title('Time series plot at 15 min interval')
plot.show()
