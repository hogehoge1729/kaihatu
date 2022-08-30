import socket
import random
import time
import os
'''
HOST = '127.0.0.1'
PORT = 50007

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    a = random.randrange(3)
    result = str(a)
    print(a)
    client.sendto(result.encode('utf-8'),(HOST,PORT))
    time.sleep(2.0)
'''

# 接続はIPアドレス= "127.0.0.1"、ポート=50007で行う
HOST = "172.21.23.64"
MAINPORT = 10001

def ConnectUnity(command):
    try :
        # TCP用のソケットを作成
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except :
        print("TCPerrpr")
    # テストのため自身のpidを表示
    result = str(command)
    print("Send:"+command)
   
    # クライアントに接続
    try :
       client.connect((HOST, MAINPORT))
    except :
        print("responce:no\n")
        return
    
    #接続したクライアントになんか送る
    try :
       # 接続できればpidをUTF-8でエンコードした文字列を送る(バイト列にする)
       client.send(result.encode('utf-8'))

       # 受け取るデータの大きさは200でデータ受け取り待ち
       data = client.recv(200)
   
        # 受け取ったデータを表示
       print(data.decode('utf-8') + "\n")
   
       # 以降はclientを通してsendメソッドでデータを送れる
       return client
       client.close()
    except :
       client.close()

#デバッグ用
if __name__ == '__main__' :
    for i in range(30):
        ConnectUnity("Hello")
