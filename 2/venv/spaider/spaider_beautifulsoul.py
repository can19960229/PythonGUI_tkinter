# coding:UTF-8
import requests, bs4, re  					# pip install bs4
BASE_URL = "https://movie.douban.com" 			# 定义基础路径
CHART_URL = BASE_URL + "/chart" 				# 要爬取的页面
def main():						# 主函数
    headers = {
        "User-Agent": "Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    }
    request = requests.get(url=CHART_URL, headers=headers)  # 发送HTTP请求
    request.encoding = "UTF-8"  # 设置页面编码
    soup = bs4.BeautifulSoup(markup=request.text, features="lxml") # 使用lxml库解析
    # 找到指定的超链接（“<a>”）标签，当发现href属性可以匹配正则则返回此标签的数据数据
    typerank_list = soup.find_all("a", href=re.compile("^/typerank")) # 获取所有分类信息
    for type in typerank_list: 				# 迭代uri地址
        type_title = type.contents[0] 			# 获取类型标题
        print("【%s】访问路径: %s" % (type_title, BASE_URL + type["href"])) 			# 处理连接
if __name__ == "__main__":     				# 判断执行名称
    main()						# 调用主函数
