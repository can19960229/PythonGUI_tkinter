import socket 						# 导入socket组件
SERVER_HOST = "localhost" 					# 服务器主机名称
SERVER_PORT = 8080 					# 监听端口
def main():						# 主函数
    with socket.socket() as client_socket: 			# 创建socket实例
        client_socket.connect((SERVER_HOST, SERVER_PORT)) 	# 连接服务端
        while True: 					# 客户端持续操作
            input_data = input("请输入要发送的数据：") 		# 键盘数据输入
            client_socket.send(input_data.encode("UTF-8")) 	# 向服务器端发送数据
            echo_data = client_socket.recv(100).decode("UTF-8") 	# 接收回应数据
            if echo_data.upper() == "EXIT": 			# 操作结束
                break 					# 结束循环
            print(echo_data)  				# 输出返回数据
if __name__ == "__main__":     				# 判断执行名称
    main()
