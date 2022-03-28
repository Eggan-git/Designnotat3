import csv
import numpy as np
import matplotlib.pyplot as plt

header = []
data = []


filename = "yscope.csv"
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

    for datapoint in csvreader:

        values = [float(value) for value in datapoint]
        data.append(values)

print(header)
print(data[0])
print(data[1])

frekvens = [p[0] for p in data]
ch1 = [p[1] for p in data]
ch2 = [p[2] for p in data]

xmax = frekvens[np.argmax(ch2)]
ymax = max(ch2)
print(ymax, xmax)
plt.plot(frekvens,ch1, frekvens, ch2)
plt.xlabel("Tid(s)")
plt.ylabel("Spenning(V)")
plt.legend(["CH1", "CH2"])
plt.grid(True)
plt.savefig("yscope")
plt.show()

    
