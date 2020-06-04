# coding:UTF-8
import os, selenium.webdriver, time, re   			# pip install selenium
CHROME_DRIVER = "F:\\PYECourse\\2\\chromedriver_win32\\chromedriver.exe"
URL = "https://ff14.huijiwiki.com/wiki/" \
      "%E9%94%BB%E9%93%81%E5%8C%A0%E9%85%8D%E6%96%B9%E5%88%97%E8%A1%A8" 	# 爬取路径
class Game: 						# 保存游戏信息
    def __init__(self, type):
        self.name = None 					# 成品名称
        self.img = None                     #获取成品图片
        self.type = type 					# 所属分类
        self.rank = None 					# 成品等级
        self.material = None 				# 制作材料
    def __repr__(self) -> str : 				# 信息输出
        return "【信息】分类：%s、名称：%s、等级：%s、制作材料：%s、成品图片:%s" % \
               (self.name, self.type,self.rank, self.material,self.img)
def main():						# 主函数
    driver = selenium.webdriver.Chrome(executable_path=CHROME_DRIVER) # 配置浏览器驱动
    driver.get(url=URL) 					# 加载页面
    count = 0
    try: 							# 捕获可能产生的异常
        for content in driver.find_elements_by_xpath("//div[@class='tabber-content']"):# 找到类型成品信息
            print(content)
            game = Game("铁匠76-80") 				# 实例化游戏等级
            game.name = content.find_element_by_class_name("item-name rarity-common").text # 名称
            print(game.name)
            game.rank = content.find_element_by_class_name("item-category").text # 名次
            print(game.rank)
        #for item in driver.find_elements_by_xpath(
#                    "//div[@class='tabber-content']"):  # 找到类型成品信息
       #     game.material = content.find_element_by_class_name("movie-crew").text.split("/")			# 演员列表
            print(game) 					# 输出电影信息

    except Exception: 					# 异常捕获
        pass						# 未定义异常处理
if __name__ == "__main__":     				# 判断执行名称
    main()						# 调用主函数
