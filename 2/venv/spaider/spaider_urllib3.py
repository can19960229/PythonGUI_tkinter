# coding:UTF-8
import urllib3				# 模块导入
URL = "https://movie.douban.com/chart" 	# 要爬取的页面
def main():				# 主函数
    http = urllib3.PoolManager()		# 实例化请求对象
    request = http.request("GET", URL) 	# 发送请求
    print(request.data.decode())		# 获取数据并解码
if __name__ == "__main__":     		# 判断执行名称
    main()				# 调用主函数
