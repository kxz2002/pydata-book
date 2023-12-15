import socket
socket_client = socket.socket()
#链接到服务端
socket_client.connect(("localhost",8888))

while True:
    #发送消息
    msg = input("please enter the msg")
    if msg == 'exit':
        break
    socket_client.send(msg.encode("UTF-8"))

    #接收返回消息
    recv_data = socket_client.recv(1024)
    print(f"Reccevied data is {recv_data.decode('UTF-8')}")

#关闭连接
socket_client.close()
