import socket 						# 导入socket组件
SERVER_HOST = "localhost" 					# 或者为“127.0.0.1”
SERVER_PORT = 8080 					# 监听端口
def main():						# 主函数
    with socket.socket() as server_socket: 			# 创建Socket对象
        server_socket.bind((SERVER_HOST, SERVER_PORT)) 		# 绑定端口
        server_socket.listen()				# 端口监听
        print("服务器启动完毕，在“%s”端口上监听，等待客户端连接 ..." % SERVER_PORT)
        client_conn, address = server_socket.accept()		# 客户端连接，进入阻塞状态
        with client_conn: 					# 通过客户端连接操作
            print("客户端连接地址：%s、连接端口：%s" % address)  # 返回一个元祖
            while True:
                data = client_conn.recv(100).decode("UTF-8")   # 接收客户端发送的请求数据
                if data.upper() == "ByeBye":
                    client_conn.send("沐言优拓：www.yootk.com".encode("UTF-8")) # 向客户端发送字节数据
                    break
                else:   #正常响应
                    client_conn.send(("[ECHO]%s" % data).encode("UTF-8"))
if __name__ == "__main__":     				# 判断执行名称
    main()