import socket


def send_file(new_client_socket, client_addr):
    # 1. 接收客户端 需要下载的文件名
    # 接收客户端发送过来的 要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)需要下载文件是：%s" % (str(client_addr), file_name))

    file_content = None
    # 2. 打开这个文件，读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print(ret)
        print("没有要下载的文件(%s)" % file_name)

    # 3. 发送文件的数据给客户端
    if file_content:
        new_client_socket.send(file_content)


def main():
    # 1. 创建套接字socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定信息bind
    tcp_server_socket.bind(("127.0.0.1", 10002))

    # 3. 监听listen
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待客户端的链接accept
        new_cliet_scoket, client_addr = tcp_server_socket.accept()

        # 5. 调用发送文件函数，完成为客户端服务
        send_file(new_cliet_scoket, client_addr)

        # 6. 断开套接字
        new_cliet_scoket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()