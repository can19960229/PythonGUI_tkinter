# coding:UTF-8
import requests,bs4, os, csv, threading  # 路径匹配符  多线程下载  下载的文件保存在csv文件中
import selenium
import selenium.webdriver
import time,re  #进行延时爬取，爬太快容易被封  匹配评论人数数字
CHROME_DRIVER = "F:\\PYECourse\\2\\chromedriver_win32\\chromedriver.exe"
BASE_URL = "https://movie.douban.com" 			# 定义基础路径
CHART_URL = BASE_URL + "/chart" 				# 要爬取的页面
driver = selenium.webdriver.Chrome(executable_path=CHROME_DRIVER)
SAVE_DIR = "f:" + os.sep + "resoures"  #下载的数据目录 F:\PYECourse\2\resoures
IMAGE_PATH =SAVE_DIR + os.sep + "images"  #图片保存的路径 F:\PYECourse\2\resoures\images
#URL = "https://movie.douban.com/typerank?" \
   #   "type_name=剧情&type=11&interval_id=100:90&action=" 	# 爬取路径
HTTP_HEADERS = {
        "User-Agent": "Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    }
CSV_HEADERS = ["type", "rank", "name", "rating", "comment", "img", "crew", "url"] # csv标题
if not os.path.exists(IMAGE_PATH): 				# 图片目录不存在
    os.makedirs(IMAGE_PATH)
class Movie:
    def __init__(self,type):
        self.img = None  # 图片名称
        self.name = None  # 电影名称
        self.type = type  # 电影分类,上一级解析来的
        self.rank = None  # 电影评分
        self.crew = None  # 演员列表
        self.rating = None  # 平均分
        self.comment = None  # 评论人数
        self.url = None  #影片路径
    def __repr__(self) -> str:
        return "【电影信息】分类：%s、名次：%d、名称：%s、评分：%f、评论人数：%d、图片：%s、演员列表：%s、影片路径：%s" % \
               (self.type, self.rank, self.name, self.rating, self.comment, self.img, self.crew, self.url)
    def get(self):  #该数据需要保存在csv文件里面
        return [self.type, self.rank, self.name, self.rating,
                self.comment, self.img, self.crew, self.url]  # 返回数据


def main():
    request = requests.get(url=CHART_URL, headers=HTTP_HEADERS)  # 发送HTTP请求
    request.encoding = "UTF-8"  # 设置页面编码
    soup = bs4.BeautifulSoup(markup=request.text, features="lxml")  # 使用lxml库解析
    # 找到指定的超链接（“<a>”）标签，当发现href属性可以匹配正则则返回此标签的数据数据
    typerank_list = soup.find_all("a", href=re.compile("^/typerank"))  # 获取所有分类信息
    for type in typerank_list:  # 迭代uri地址
        type_title = type.contents[0]  # 获取类型标题
        download_type(type_title, BASE_URL + type["href"])  #开始进行数据爬取


def download_movie_image(url, image_name):  #url:下载路径，image_name:保存名称

    image_path = IMAGE_PATH + os.sep + image_name  # 图片保存路径
    response = requests.get(url)
    with open(file=image_path, mode="bw") as file:  # 文件写入
        file.write(response.content)  # 图片写入文件，获取二进制数据
        #response.text 获取文本数据

def download_type(type, url):						# 主函数
    driver.get(url=url)
    for item in range(5):
        target = driver.find_element_by_id("footer")
        driver.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2)  #2秒进行一次数据处理
    time.sleep(2)  #因为考虑到异步加载需要时间，所以等待2秒
    count = 0 #抓取的计数
    save_path = SAVE_DIR + os.sep + type + ".csv"
    with open(file=save_path, mode="w", newline="", encoding="UTF-8") as file:
        csv_file = csv.writer(file)  # 创建csv输出
        csv_file.writerow(CSV_HEADERS)  # 写入标题
        try:
            for content in driver.find_elements_by_xpath("//div[@class='movie-content']"):
                time.sleep(0.2)
                movie = Movie(type) #实例化电影信息
                movie.url = content.find_element_by_tag_name("a").get_property("href")  #获取影片路径
                image_url = content.find_element_by_class_name("movie-img").get_property("src")  # 图片
                if image_url:  # 可以加载到图片再获取后续元素
                    movie.img = image_url[image_url.rfind("/") + 1 :]  #获取图片名称
                    movie.name = content.find_element_by_class_name("movie-name-text").text  # 名称
                    threading.Thread(target=download_movie_image,args=(image_url, movie.img,)).start()  #启动下载线程
                    movie.rank = int(content.find_element_by_class_name("rank-num").text)  # 名次
                    movie.crew = content.find_element_by_class_name("movie-crew").text.split("/")  # 演员列表
                    movie.rating = float(content.find_element_by_class_name("rating_num").text)  # 评分
                # 评分内容里面包含有中文，可以通过正则匹配的方式加载到里面的数字信息
                    movie.comment = int(re.sub("\D", "", content.find_element_by_class_name("comment-num").text))  # 评论人数
                    csv_file.writerow(movie.get())  # 获取列表数据写入

                    count += 1  # 统计计数
                    if count >= 50:  # 设置采集上限
                        raise Exception("爬够了，休息了！")  # 结束采集
        except Exception as exp:
            print(exp)
            pass

if __name__ == "__main__":     				# 判断执行名称
    main()						# 调用主函数
