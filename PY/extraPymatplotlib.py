from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
plt.title("Data Crushter")
plt.ylabel("Y label")
plt.xlabel("X label")
import statistics

# x = [1,5,4]
# y = [23,45,89]

# plt.style.use("ggplot")

# plt.plot([1,2,3],[12,15,50],label='1st')

# plt.plot(x,y,label='2nd data')
# plt.legend()




#histogram
ages=[18,16,24,5,7,16,49,9,49,47,64,18,18,18,18]
ages = np.array(ages)
bins = [10,20,30,40,50,60,70,80]
median= statistics.median(ages)
print(median)

plt.style.use('ggplot')
plt.axvline(median)
plt.hist(ages,bins=bins,edgecolor='black',color='green',label='ages')


plt.legend()
plt.show()


