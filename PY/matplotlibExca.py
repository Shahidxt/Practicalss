from matplotlib import pyplot as plt
import numpy as np



# a = np.array([14,1,8,18,87,11,9])
# le = len(a)
# max = a.max()
# min = a.min()
# rang = max - min
# widt = rang / le

# plt.style.use('ggplot')

# plt.hist(a,bins =int(widt))
# plt.show()


data = np.array([10,20,30,40,50,60,70,80,90,100])

bins= (data.max() - data.min()) //len(data)
# plt.style.use("ggplot")

plt.hist(x=data,bins=bins)

plt.show()
