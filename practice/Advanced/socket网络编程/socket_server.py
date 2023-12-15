import socket

# 创建socket对象
socket_server = socket.socket()

# 绑定ip地址和端口
socket_server.bind(("localhost", 8888))

# 监听端口
socket_server.listen(1)
# listen 方法内部接受一个整数值，表示接收的连接数

# 等待客户端连接
# result:tuple = socket_server.accept()
# conn = result[0]        #客户端和服务端的连接对象
# address = result[1]     #客户端的地址信息

conn, address = socket_server.accept()
# accept()方法是阻塞式的方法，如果没有连接，程序就会卡在这一行
print(f"接收到了信息，客户端地址式{address}")

while True:
    # 接收客户端信息，使用客户端和服务端的本质连接对象而非socket_server
    data: str = conn.recv(1024).decode("UTF-8")
    # recv返回值是一个字节数组，也就是bytes对象，不是字符串，需要decode解码为字符串
    print(f"客户端发来的消息是{data}")

    # 发送回复消息
    msg = input("Please enter the data you want to send.")
    if msg == "exit":
        break
    conn.send(msg.encode("UTF-8"))

# 关闭连接
conn.close()
socket_server.close()
