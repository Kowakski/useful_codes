'''
AF端作为client端，实时的把数据发送到服务器端，然后画出来
'''
#服务器端:
import numpy as np
import socket
import pdb
from struct import *
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

Draw_data = []
def init_draw_dat_buf():
    global Draw_data
    pdb.set_trace()
    # Draw_data = []
    Draw_data.clear()
    for i in range(15):  #init
        tmp = []
        for j in range(17):
            tmp.append([])
        Draw_data.append(tmp)
    # print( np.size(Draw_data) )
    return

def socket_update_date(): #创建 socket 用于更新数据
    socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建服务端的socket对象socketserver
    host = '192.168.12.228'
    port = 6789
    print("创建socekt")
    global Draw_data
    socketserver.bind((host, port)) #绑定地址（包括ip地址会端口号）
    #设置监听
    socketserver.listen(5)
    #等待客户端的连接
    #注意：accept()函数会返回一个元组
    #元素1为客户端的socket对象，元素2为客户端的地址(ip地址，端口号)
    clientsocket,addr = socketserver.accept()

    #while循环是为了能让对话一直进行，直到客户端输入q
    while True:
        #接收客户端的请求
        recvmsg = clientsocket.recv(15*17*2)  #客户端是sizeof(alt_u16) *15*17 两边的bytes要一样，不然会出错
        # pdb.set_trace()
        if len(recvmsg) != 510:
            continue

        unpack_data = unpack( '255H', recvmsg )
        # Draw_data = [] #clear
        # print(unpack_data[0:15])
        # pdb.set_trace()
        # print("接收到AF端数据")
        if unpack_data[0] == 0x0 and unpack_data[60] == 0  and unpack_data[180] == 0:
            print("开始聚焦，清空数据")
            Draw_data.clear()
            for i in range(15):  #init
                tmp = []
                for j in range(17):
                    tmp.append([])
                Draw_data.append(tmp)
            # init_draw_dat_buf()
        else:
            # pdb.set_trace()
            index = 0
            for i in range(15):
                for j in range(17):
                    # print("存储数据", i, j, index)
                    Draw_data[i][j].append( unpack_data[index] )
                    index = index + 1
        # print(Draw_data)
        #把接收到的数据进行解码
        # strData = recvmsg.decode("utf-8")
        #判断客户端是否发送q，是就退出此次对话
        # if strData=='q':
        #     break
        # print("收到:"+strData)
        # msg = input("回复:")
        #对要发送的数据进行编码
        # clientsocket.send(msg.encode("utf-8"))

    socketserver.close()

threads = []
t1 = threading.Thread( target= socket_update_date, args=() )
threads.append( t1 )

fig = plt.figure( )
ax = fig.add_subplot( 111 )

def dy_draw(i):
    global Draw_data
    if len( Draw_data[0][0] ) == 0:
        return

    # x = range( len( Draw_data[0] ) )
    ax.clear()
    # pdb.set_trace()
    for j in range(3,12):
        for k in range(4,13):
            len_t = len( Draw_data[j][k] )
            x = np.linspace(0, len_t -1, len_t )
            if j == 0:
                plt.plot( x, Draw_data[j][k][0:len_t],'r' )
            else:
                plt.plot( x, Draw_data[j][k][0:len_t], 'b' )
    plt.xlabel('Focus Index')
    plt.ylabel('Focus Value')
    plt.title('Dynamic Focus Value')
    return

if __name__ == "__main__":
    init_draw_dat_buf()
    for t in threads:
        t.setDaemon(False)
        t.start()
    # ani = animation.FuncAnimation( fig, animate, interval = 10 )
    ani = animation.FuncAnimation( fig, dy_draw, interval = 10 )
    plt.show()
    print("exit main process")

#客户端建立连接和发送数据的代码 C语言实现
'''
/*
void socket_initial()
{
// #ifndef DEBUG_OSD
//  return;
// #endif
    int len;
    struct sockaddr_in remote_addr; //服务器端网络地址结构体
    memset(&remote_addr,0,sizeof(remote_addr)); //数据初始化--清零
    remote_addr.sin_family=AF_INET; //设置为IP通信
    remote_addr.sin_addr.s_addr=inet_addr("192.168.12.228");//服务器IP地址
    remote_addr.sin_port=htons(6789); //服务器端口号
    if((client_sockfd=socket(PF_INET,SOCK_STREAM,0))<0)
    {
        printf("socket error");
        return;
    }
    if(connect(client_sockfd,(struct sockaddr *)&remote_addr,sizeof(struct sockaddr))<0)
    {
        printf("connect error");
        close(client_sockfd);
        client_sockfd = -1;
        return;
    }
    printf("client_sockfd = %d \n", client_sockfd);
}

void send_raw_data( alt_u16 buf[15][17] ){
    if(-1 != client_sockfd){
        send( client_sockfd, buf, sizeof(alt_u16)*15*17, 0 );
    }
    return;
}

void send_firt_zeros_data( void ){
    alt_u16 buf[15][17];
    memset( buf, 0, sizeof(alt_u16)*17*15 );
    if(-1 != client_sockfd){
        send( client_sockfd, buf, sizeof(alt_u16)*15*17, 0 );
    }
    return;
}
 */
'''

'''
# 画柱状图，但是太卡了
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

def animate(i):
    print("In animate", len(Draw_data))
    if( len(Draw_data) == 0 ):
        return
    X = np.arange( 0, len(Draw_data[0]), 1 )
    Y = np.arange( 0, len(Draw_data), 1 )
    X,Y = np.meshgrid(X,Y)

    Xpos = X.flatten('F')
    Ypos = Y.flatten('F')
    Zpos = np.zeros_like( Xpos )

    dx = np.ones_like( Xpos )
    dy = dx.copy()
    dz = np.array(Draw_data).flatten()

    # ax1.plot_surface(X,Y,Z, cmap = plt.cm.winter )
    print("Draw")
    ax1.bar3d( Xpos, Ypos, Zpos, dx, dy, dz, color='b' )
    return

def draw_datas_in_time( i ):
    ani = animation.FuncAnimation( fig, animate, interval = 10 )

# t2 = threading.Thread( target = draw_datas_in_time, args=() )
# threads.append( t2 )
'''