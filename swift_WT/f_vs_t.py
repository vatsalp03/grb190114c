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

plt.scatter(col1, col4, s=0.5, c="r")
plt.xlabel("Time (s)")
plt.ylabel("Flux density (erg cm$^{-2}$ s$^{-1}$)")

plt.grid(alpha=0.5)
#plt.savefig("log_swift_WT.jpg", dpi=500)
plt.show()