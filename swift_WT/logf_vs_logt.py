import matplotlib.pyplot as plt
import numpy as np

text_file = open("wt_data.txt", "r")
data = text_file.readlines()

np_data = np.array(data)
col1, col4 = [], []

n = 2
while n < len(data):
	var = np_data[n].rstrip().split("\t")
	col1.append(float(var[0]))
	col4.append(float(var[3]))
	n += 1

x = np.log(col1)/np.log(10)
y = np.log(col4)/np.log(10)

bestfit = np.polyfit(x, y, 1)
bestfit_fn = np.poly1d(bestfit)
z = np.linspace(min(x), max(x), 2)

plt.plot(z, bestfit_fn(z), c="black")
plt.scatter(x, y, s=0.5, c="r")

plt.xlabel("log T")
plt.ylabel("log F")

plt.grid(alpha=0.5)
#plt.savefig("log_swift_WT.jpg", dpi=500)
plt.show()