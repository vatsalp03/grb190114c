import numpy as np
import matplotlib.pyplot as plt

text_file = open("mag_vs_time.txt", "r")
data = text_file.readlines()
np_data = np.array(data)

col3, col5 = [], []

n = 2
while n < len(data):
	var = np_data[n].split("\t")
	col3.append(float(var[2]))
	col5.append(float(var[4]))
	n += 1

plt.scatter(col3[0:334], col5[0:334], s=2, c="red" )
plt.scatter(col3[380:770], col5[380:770], s=2, c="blue")
plt.scatter(col3[771:len(data)], col5[771:len(data)], s=2, c="green")

plt.xlabel("Time (s)")
plt.ylabel("Magnitude")
plt.ylim(19,10)

plt.legend(["BV_RING03 (4269Å - 6501Å)", "R_RINGO3 (6465Å - 7595Å)", "I_RINGO3 (7827Å - 8662Å)"], loc ="upper right")
plt.grid(alpha=0.5)

#plt.savefig("mag_time.jpg", dpi=500)
plt.show()