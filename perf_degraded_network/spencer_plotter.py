#!/usr/bin/python3

import matplotlib.pyplot as plt
import re
import numpy as np

# options: 'rtt', 'cwnd-change', 'rwnd-change', 'rx-data'
metric = 'rtt'

# QUIC
time = []
rtt = []
# sp1 = plt.subplot(2, 2, 1)
with open('quic-'+metric+'.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line_list = re.split("\t|\n", line)
        time.append(line_list[-4])
        rtt.append(float(line_list[-2]))
min_rtt = min(rtt)
max_rtt = max(rtt)
plt.yticks(np.arange(min_rtt, max_rtt, step=(max_rtt-min_rtt)/10))
ind = np.arange(len(time)) 
width = 0.1
plt.bar(ind, rtt, width, label=metric)
plt.ylabel(metric)
plt.title('quic: '+metric+' VS time')
plt.savefig('plots/quic-'+metric+'.png')

# VEGAS
time = []
rtt = []
plt.clf()
# sp2 = plt.subplot(2, 2, 2)
with open('vegas-'+metric+'.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line_list = re.split("\t|\n", line)
        time.append(line_list[-4])
        rtt.append(float(line_list[-2]))
min_rtt = min(rtt)
max_rtt = max(rtt)
plt.yticks(np.arange(min_rtt, max_rtt, step=(max_rtt-min_rtt)/10))
ind = np.arange(len(time)) 
width = 0.1
plt.bar(ind, rtt, width, label=metric)
plt.ylabel(metric)
plt.title('vegas: '+metric+' VS Time')
plt.savefig('plots/vegas-'+metric+'.png')

# RENO
time = []
rtt = []
plt.clf()
# sp3 = plt.subplot(2, 2, 3)
with open('reno-'+metric+'.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line_list = re.split("\t|\n", line)
        time.append(line_list[-4])
        rtt.append(float(line_list[-2]))
min_rtt = min(rtt)
max_rtt = max(rtt)
plt.yticks(np.arange(min_rtt, max_rtt, step=(max_rtt-min_rtt)/10))
ind = np.arange(len(time)) 
width = 0.1
plt.bar(ind, rtt, width, label=metric)
plt.ylabel(metric)
plt.title('reno: '+metric+' VS Time')
plt.savefig('plots/reno-'+metric+'.png')

# plt.tight_layout()
# plt.savefig('plots/'+metric+'.png')