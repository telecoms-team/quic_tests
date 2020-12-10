#!/usr/bin/python3

import matplotlib.pyplot as plt
import re
import numpy as np
time = []
data = []

with open('clientQUIC-rtt2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line_list = re.split("\t|\n", line)
        time.append(line_list[-4])
        data.append(line_list[-2])

print (time)
print (data)
graph_type = 'RTT'
ind = np.arange(len(time)) 
width = 0.1
plt.bar(ind, data, width, label=graph_type)
plt.ylabel(graph_type)
plt.title('Time VS ' + graph_type)
plt.savefig('plot_out.png')
