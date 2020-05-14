
/*
 *@server python
 */
def parse_and_get_draw_data( data ):
    unpack_data    = unpack('25HH26?',data)
    zoom_value     = np.array(unpack_data[0:25])

    # print(zoom_value)
    focus_position = unpack_data[25]
    zoom_weight    = np.array(unpack_data[26:-1])

    # zoom_weight[2] = True
    # zoom_weight[5] = True

    print(zoom_weight, focus_position)
    valued_weight_num = np.sum(zoom_weight)
    if valued_weight_num == 0:
        zoom_avg_value = 0
    else:
        zoom_avg_value = np.sum(np.multiply(zoom_value, zoom_weight))/valued_weight_num
    y.append([zoom_avg_value, focus_position])

import math
import socket
from struct import *
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pynput import keyboard
import threading

IP_addr = '192.168.12.74'
Port = 6789
keyvalue = "r"

#建立TCP 链接
client = socket.socket()
client.connect((IP_addr, Port))

while True:
    msg = "1"
    if len(msg) == 0: continue
    client.send(msg.encode('utf-8'))
    # print("send value 2")
    recv_count = recv_count+1
    t_now = recv_count*0.1
    data = client.recv(512)    #接收数据
    # print(type(data),len(data))
    parse_and_get_draw_data( data )