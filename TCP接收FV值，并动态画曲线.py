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

#matplotlib inline
def do_on_press(key):
    global keyvalue
    try:
        keyvalue = key.char
        # print('alphanumeric key {0} {1} {2} pressed'.format(key.char, type(keyvalue), keyvalue ))
    except AttributeError:
        # print('special key {0} pressed'.format(key), type(key) )
        keyvalue = "f12"
        exit()

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def key_event_listen():
    print("Start key event listern")
    with keyboard.Listener(
        on_press=do_on_press,
        on_release=on_release) as listener:
        listener.join()

# set up matplotlib
is_ipython = 'inline' in matplotlib.get_backend()
if is_ipython:
    from IPython import display

plt.ion()

def plot_durations(y):
    plt.figure(2)
    plt.clf()
    plt.subplot(211)
    plt.plot(y[:,0])
    plt.subplot(212)
    plt.plot(y[:,1])

    plt.pause(0.001)  # pause a bit so that plots are updated
    if is_ipython:
        display.clear_output(wait=True)
        display.display(plt.gcf())

y = []
t_now      = 0
recv_count = 0

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

def plot_draw_curves( ):
    # print("y is ", y)
    draw_y = np.array(y)
    plt.figure(2)
    plt.clf()
    plt.subplot(211)
    plt.title("FV value", loc='left')
    plt.plot(draw_y[:,0],'r')    #FV value
    plt.subplot(212)
    plt.title("lens position", loc='left')
    plt.plot(draw_y[:,1],'g')    #lens value
    plt.draw()
    plt.pause(0.01)

def draw_curves():
    global keyvalue, recv_count
    # plt.figure(1)

    #建立TCP 链接
    client = socket.socket()
    client.connect((IP_addr, Port))

    while True:
        # print("in draw_curves process {0}".format(keyvalue))
        if keyvalue == "f12":
            msg = "0"
            if len(msg) == 0:continue
            client.send(msg.encode('utf-8'))    #把编译成utf-8的数据发送出去
            client.close()
            exit()

        elif keyvalue == "p":   #暂停
            msg = "2"
            if len(msg) == 0:continue
            client.send(msg.encode('utf-8'))
            plot_draw_curves( )
            # continue

        elif keyvalue == "r":
            # print("send value {0}".format(keyvalue))
            msg = "1"
            if len(msg) == 0: continue
            client.send(msg.encode('utf-8'))
            # print("send value 2")
            recv_count = recv_count+1
            t_now = recv_count*0.1
            data = client.recv(512)    #接收数据
            # print(type(data),len(data))
            parse_and_get_draw_data( data )
            plot_draw_curves( )
        elif keyvalue == "c":
            keyvalue = 'r'
            global y
            y = []
            # y = [[0,0]]
            # plot_draw_curves( )
        else:
            plot_draw_curves( )
            pass
    client.close()


'''
监听按键消息
'''
threads=[]
t1 = threading.Thread(target= key_event_listen, args=( ))
threads.append(t1)

'''
跟服务器端交互消息并且绘图
'''
t2 = threading.Thread(target= draw_curves, args=())
threads.append(t2)

if __name__ == "__main__":
    for t in threads:
        t.setDaemon(False)
        t.start()
    # t.join()
    print("exit main process")
