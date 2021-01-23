'''
循环为多个客户端服务器
'''
import socket


def main():
	#1. 创建套接字
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#2. 绑定本地信息bind
	tcp_server_socket.bind(("127.0.0.1", 10000))

	#3. 让默认套接字由主动改为被动listen
	tcp_server_socket.listen(128)

	while True:
		#4. 等待客户端的链接accept
		new_client_socket, client_addr = tcp_server_socket.accept()
		
		print("新客户端地址: %s" %str(client_addr))

		#5. 接收客户端发来的信息
		recv_data = new_client_socket.recv(1024)
		print("接受信息是: %s" %recv_data.decode("utf-8"))

		#6. 回送信息给客户端
		new_client_socket.send("服务端收到信息".encode("utf-8"))

		#7. 关闭套接字
		# 关闭accept返回的套接字，意味着不会为这个客户端服务
		new_client_socket.close()

	# 将监听套接字关闭
	tcp_server_socket.close()


if __name__ == "__main__":
	main()