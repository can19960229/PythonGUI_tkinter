# coding:UTF-8
import requests						# 模块导入
URL = "https://movie.douban.com/chart" 			# 要爬取的页面
def main():						# 主函数
    headers = {
        "User-Agent": "Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    }
    request = requests.get(url=URL, headers= headers)  				# 发送HTTP请求
    request.encoding = "UTF-8" 				# 设置页面编码
    print(request.status_code)  #状态代码
    print(request.text) 					# 获取页面信息
if __name__ == "__main__":     				# 判断执行名称
    main()						# 调用主函数
