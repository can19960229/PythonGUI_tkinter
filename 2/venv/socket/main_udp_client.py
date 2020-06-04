import socket 						# 导入socket组件
SERVER_HOST = "localhost" 					# 或者为“127.0.0.1”
SERVER_PORT = 8080 					# 监听端口
def main():						# 主函数
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket: # UDP客户端
        while True: 					# 持续交互
            input_data = input("请输入要发送的数据：") 		# 键盘输入
            if input_data: 					# 有数据输入
                client_socket.sendto(input_data.encode("UTF-8"),(SERVER_HOST, SERVER_PORT)) 		# 发送数据
                print("服务器端响应数据：%s" %client_socket.recv(30).decode("UTF-8")) 	# 接收返回数据
            else: 						# 没有数据输入
                break 					# 结束交互操作
if __name__ == "__main__":     				# 判断执行名称
    main()
