import socket 


def main():
    #1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #2. 链接服务器
    tcp_socket.connect(("127.0.0.1", 10000))
    
    #3. 获取下载的文件名
    download_file_name = input("要下载的文件名：")

    #4. 将文件名发送到服务器
    tcp_socket.send(download_file_name.encode("utf=8"))

    #5. 接收文件中的数据
    recv_data = tcp_socket.recv(1024)

    if recv_data:
        #6. 保存接收到的数据到文件中
        with open(download_file_name, "wb") as f:
            f.write(recv_data) 

    #7. 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()   