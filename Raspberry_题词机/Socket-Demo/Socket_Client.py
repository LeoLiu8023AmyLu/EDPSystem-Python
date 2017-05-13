# -*- coding: utf-8 -*-
'''
Created on 2017年5月7日
@author: LeoLiu
'''
import socket
import threading
 
inString = '' # 输入的字符串
outString = '' # 输出的字符串
nick = '' # 用户聊天名称
 
def DealOut(s):
    global nick, outString # 建立全局字符
    while True:
        outString = raw_input() # 等待输入字符串
        outString = nick + ': ' + outString # 组成用户名+ 字符串
        s.send(outString) # Socket 输出
 
def DealIn(s):
    global inString
    while True:
        try:
            inString = s.recv(1024)
            if not inString:
                break
            if outString != inString:
                print(inString)
        except:
            break
         
 
nick = input("input your nickname: ")
ip = raw_input("input the server's ip adrress: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, 8888))
sock.send(nick)
 
thin = threading.Thread(target = DealIn, args = (sock,))
thin.start()
thout = threading.Thread(target = DealOut, args = (sock,))
thout.start()
 
#sock.close()