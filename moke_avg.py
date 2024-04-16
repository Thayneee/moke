import numpy as np
import csv
import matplotlib.pyplot as plt 

#open data.txt
f = open('data.txt', 'r')

magneticFieldValues = []
voltageValues = []

#reads each line of data.txt and assigns to lists
for line in f:
    lineList = line.split()
    magneticFieldValues.append(float(lineList[0]))
    voltageValues.append(float(lineList[1]))

#close data.txt
f.close()

found = []

for index in range(len(magneticFieldValues) - 1):
    #search for when changes from negative to positive (signals end of cycle)
    if magneticFieldValues[index] < 0 and magneticFieldValues[index + 1] >= 0:
        #add the index of the change (current index) into found list
        found.append(index + 1)

#create a list of sublists split on the indexes in found
magneticFieldValuesSplit = [magneticFieldValues[found[i]:found[i+1]] for i in range(len(found)-1)]
voltageValuesSplit = [voltageValues[found[i]:found[i+1]] for i in range(len(found)-1)]

#converts seperated sublists into a numpy array then averages them together (numpy array is faster than base python arrays)
array_mag = np.array(magneticFieldValuesSplit)
avg_mag = np.mean(array_mag, axis=0)

array_volt = np.array(voltageValuesSplit)
avg_volt = np.mean(array_volt, axis=0)

#choose 2nd cycle to plot so can be compared to averaged data
raw_mag = magneticFieldValuesSplit[1]
raw_volt = voltageValuesSplit[1]
    
#write average data to file "avgdata.txt", file needs to exist first
with open('avgdata.txt', 'w+') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(avg_mag, avg_volt))

#plot averaged data
plt.figure(1)
plt.plot(avg_mag, avg_volt)
plt.xlabel('Magnetic Field')
plt.ylabel('Voltage')
plt.title('Average Magnetic Field vs Voltage')
plt.grid(True)

#plot one cycle of raw data
plt.figure(2)
plt.plot(raw_mag, raw_volt)
plt.xlabel('Magnetic Field')
plt.ylabel('Voltage')
plt.title('One Cycle of Raw Magnetic Field vs Voltage')
plt.grid(True)

#show the plots
plt.show()