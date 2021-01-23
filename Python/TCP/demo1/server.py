import socket


def main():
    #1. 创建套接字 socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #2. 绑定本地信息 bind
    tcp_server_socket.bind(("127.0.0.1", 10000))

    #3. 让默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128)   # 128表示socket的”排队个数“, socket允许的最大连接数为128+1

    #4. 等待客户端的链接(accept)
    new_client_socket, client_addr = tcp_server_socket.accept()
    print("新客户地址: ",  client_addr)
   
    #5. 接收客户端发来的请求
    recv_data = new_client_socket.recv(1024)
    print("接受到的信息: %s" %recv_data.decode("utf-8"))

    #6. 回送一部分数据给客户端
    new_client_socket.send("server get message ok!".encode("utf-8"))

    #7.关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()