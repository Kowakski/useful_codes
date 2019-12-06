/*
 *@client
 */

int client_sockfd = -1;
void socket_initial( void ){
    int len;
    struct sockaddr_in remote_addr; //服务器端网络地址结构体
    memset(&remote_addr,0,sizeof(remote_addr)); //数据初始化--清零
    remote_addr.sin_family=AF_INET; //设置为IP通信
    remote_addr.sin_addr.s_addr=inet_addr("127.0.0.1");//服务器IP地址
    remote_addr.sin_port=htons(1206); //服务器端口号
    if((client_sockfd=socket(PF_INET,SOCK_STREAM,0))<0){
        printf("socket error");
        return;
    }
    if(connect(client_sockfd,(struct sockaddr *)&remote_addr,sizeof(struct sockaddr))<0){
        printf("connect error");
        close(client_sockfd);
        client_sockfd = -1;
        return;
    }
    printf("client_sockfd = %d \n", client_sockfd);
}

/*
 *@send fv to server,发送FV值
 */
void send_focus_value_to_server( unsigned short *buf, int length ){
    unsigned short temp_buf[255];
    if(-1 != client_sockfd){
        memcpy(temp_buf, buf, sizeof( unsigned short )*length);
        send(client_sockfd, temp_buf, sizeof( unsigned short )*length, 0);
    }
    return;
}

void send_weight_to_main(unsigned char *buf, int length){

    unsigned char temp_buf[255];
    int i;
    static unsigned char test = 0;
    if(-1 != client_sockfd){
        send(client_sockfd, &length, 1, 0);
        if(length == 25 || length == 255) {
            for(i = 0; i < length; i++){
                temp_buf[i] = buf[length - 1 - i];
            }
        } else {
            memcpy(temp_buf, buf, length);
        }
        send(client_sockfd, temp_buf, length, 0);
    }
}

void send_clear_weight_to_main(){
    if(-1 != client_sockfd){
        int length = 225;
        unsigned char buf[225] = { 0 };
        memset(buf, 0, 225);
        send(client_sockfd, &length, 1, 0);
        send(client_sockfd, buf, length, 0);
    }
}



/*
 *@server C
 */
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>

#define MYPORT  8887
#define QUEUE   20
#define BUFFER_SIZE 1024

//add by zys
static int fb_fd = -1;
int g_fdClient = 0;
int g_fdSever = 0;


void print_u16_array( const unsigned short buf[][17], unsigned short line ){
    printf("print array line %d\n", line);
    for( int i = 0; i < 15; i++ ){
        for( int j = 0; j < 17; j++ ){
            printf("%d,\t", buf[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int main(int argc, char *argv[])//跟相邻帧对比
{
    unsigned int u32FrmCnt = 0;
    int i, j, k;
    float ratio = 0.0;
    unsigned char plusState = 0;

    int server_sockfd = socket(AF_INET,SOCK_STREAM, 0);
    g_fdSever = server_sockfd;
    int mw_optval = 1;
    setsockopt(server_sockfd, SOL_SOCKET, SO_REUSEADDR, (char *)&mw_optval,sizeof(mw_optval));
    ///定义sockaddr_in
    struct sockaddr_in server_sockaddr;
    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_port = htons(MYPORT);
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_ANY);

    ///bind，成功返回0，出错返回-1
    if(bind(server_sockfd,(struct sockaddr *)&server_sockaddr,sizeof(server_sockaddr))==-1){
        perror("bind");
        exit(1);
    }

    printf("监听%d端口\n",MYPORT);
    ///listen，成功返回0，出错返回-1
    if(listen(server_sockfd,QUEUE) == -1){
        perror("listen");
        exit(1);
    }

    ///客户端套接字
    // char buffer[BUFFER_SIZE];
    unsigned short buffer[15][17];
    struct sockaddr_in client_addr;
    socklen_t length = sizeof(client_addr);

    printf("等待客户端连接\n");
    ///成功返回非负描述字，出错返回-1
    while(1){
    int conn = accept(server_sockfd, (struct sockaddr*)&client_addr, &length);
    if(conn<0){
        perror("connect");
        exit(1);
    }
    int i=0;

    g_fdClient = conn;

    printf("客户端成功连接\n");
    while(1)
    {
        memset(buffer,0,sizeof(buffer));
        int len = recv(conn, buffer, sizeof(buffer),0);
        if (len <= 0){
            break;
        }
        print_u16_array( buffer, __LINE__ );
    }
    close(fb_fd);
    close(conn);
}
    close(server_sockfd);
    return 0;
}


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