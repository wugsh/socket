
'''
循环为多个客户端服务并且多次服务一个客户端
'''
import socket


def main():
    #1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #2. 绑定信息bind
    tcp_server_socket.bind(("127.0.0.1", 10000))

    #3. 默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128)

    # 循环目的：调用多次accept,从而为多个客户端服务
    while True:
        #4. 等待客户端链接accept
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("客户端地址: %s" %str(client_addr))

        # 循环目的: 为同一个客户端 服务多次
        while True:
            recv_data = new_client_socket.recv(1024)
            print("接收到的信息: %s" % recv_data.decode("utf-8"))

            # 如果recv解堵塞，那么有2种方式：
            # 1. 客户端发送过来数据
            # 2. 客户端调用close导致而了 这里 recv解堵塞
            if recv_data:
                pass
            else:
                break
        # 关闭套接字
        # 关闭accept返回的套接字 意味着 不会再为这个客户端服务
        new_client_socket.close()

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()

