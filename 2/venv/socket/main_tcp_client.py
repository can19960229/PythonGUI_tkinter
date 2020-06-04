import socket 						# 导入socket组件
SERVER_HOST = "localhost" 	# 连接主机名
SERVER_PORT = 8080 			# 服务器连接端口
def main():						# 主函数
    with socket.socket() as client_socket: 		# 创建客户端socket对象
        client_socket.connect((SERVER_HOST, SERVER_PORT)) 	# 连接服务端
        print("服务器端响应数据：%s" % client_socket.recv(30).decode("UTF-8")) # 接收返回数据
if __name__ == "__main__":     				# 判断执行名称
    main()
