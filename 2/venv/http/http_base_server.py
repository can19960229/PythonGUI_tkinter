# coding:UTF-8
import socket					# HTTP服务器基于socket组件开发
import multiprocessing				# 多进程管理
class HTTPServer: 					# 服务器类
    def __init__(self, port): 			# 构造方法
        #socket.AF_INET IPv4的协议进行处理，socket.SOCK_STREAM sokect流式进行处理
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建sokect实例
        # socket.SO_REUSEADDR可以方便的将应用绑定在系统核心端口上
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("0.0.0.0", port)) 	# 在当前主机的指定端口绑定服务
        self.server_socket.listen()			# 开启监听
    def start(self): 				# 服务器提供服务
        while True: 				# 持续提供服务
            client_socket, client_address = self.server_socket.accept() # 等待客户端连接
            print("【新的客户端连接】客户IP：%s、访问端口：%s" % client_address)
            # 为每一个客户请求开启一个新的子进程，同时设置不同的进程处理函数
            handle_client_process = multiprocessing.Process(target=self.handle_response,args=(client_socket,)) 		# 创建新进程
            handle_client_process.start()		# 进程启动
            client_socket.close()			# 进程执行完毕后，关闭当前的Socket连接
    def handle_response(self, client_socket): 		# 处理用户响应
        request_headers = client_socket.recv(1024) 	# 接收HTTP发送来的数据信息
        print(request_headers.decode())		# 获取客户端发送的头部信息
        response_start_line = "HTTP/1.1 200 OK\r\n"      # 响应状态码
        response_headers = "Server: Yootk Server\r\nContent-Type: text/html\r\n"  # 响应头信息
        response_body = "<html>" \
                        "<head>" \
                        "   <title>沐言优拓Python教程</title>" \
                        "   <meta charset='UTF-8'/>" \
                        "</head>" \
                        "<body>" \
                        "   <h1>沐言优拓：www.yootk.com</h1>" \
                        "   <h1>沐言优拓技术讲师：李兴华（江湖人称“小李老师”）</h1>" \
                        "</body>" \
                        "</html>" 			# 构造HTML数据
        response = response_start_line + response_headers + "\r\n" + response_body # 响应数据
        client_socket.send(bytes(response, "utf-8")) 	# 向客户端返回响应数据
        client_socket.close()			# 关闭客户端连接
def main():					# 主函数
    #如果使用80，则直接输入域名即可（https://www.baidu.com），如果不输入80则必须使用具体端口（https://www.baidu.com:90/）
    http_server = HTTPServer(80) 			# 创建HTTP服务器并设置监听端口
    http_server.start()				# 启动HTTP服务器
if __name__ == "__main__":     			# 判断执行名称
    main()
