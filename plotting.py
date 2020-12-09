#!/usr/bin/python3
#import matplotlib.pyplot as plt
import re
time_rtt = []

with open('clientQUIC-rtt2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line_list = re.split("\t|\n", line)
        time_rtt.append((line_list[-4], line_list[-2]))

# time_rtt (current_time, rtt)
