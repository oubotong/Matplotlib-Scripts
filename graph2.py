mport matplotlib.pyplot as plt
import numpy as np

veil = (5.71,   54.64,  7.07,   6.46,   4.54)

# Position of bars on x-axis
ind = np.arange(5)

# Figure size
plt.figure(figsize=(5,5))


width = 0.7      

plt.bar(ind + width / 2, veil, width, label='Veil',color = 'grey')

plt.xlabel('Syscalls')
plt.ylabel('Performance')
plt.title('Experiments')
ax = plt.gca()
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width / 2, ('open',    'getpid','read',    'write','mmap'))

# Finding the best position for legends and putting it
# plt.style.use('seaborn')
plt.legend(loc='best')
plt.show()
