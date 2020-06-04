# coding:UTF-8
import tkinter				# 模块导入
import os
IMAGES_PATH = "F:\\PYECourse\\2\\resoures\\11.png"		# 图标路径
class MainForm: 						# 定义主窗体类
    def __init__(self): 					# 构造方法
        root = tkinter.Tk()  				# 创建窗体
        root.title("www.candy.com")  # 设置窗体标题
     #  root.iconbitmap(IMAGES_PATH)  # 设置窗体图标
        root.geometry("500x100")  # 设置主窗体尺寸
        root.maxsize(1000, 1000)  # 设置窗体最大尺寸
        root["background"] = "pink"  # 设置背景颜色
        label_text = tkinter.Label(root, text="chencan:www.can829.com",
                                   width=200, height=200, bg="#006011",
                                   font=("微软雅黑", 20), fg="#ffffff", justify="right")  # 文字标签
        text = tkinter.Text(root, width=50, height=5, font=("微软雅黑", 10))
        text.insert("current", "程七七：")
        text.pack()
        label_text.pack()  # 显示文字
        root.mainloop()  					# 循环监听
def main():						# 主函数
    MainForm()					# 显示主窗体
if __name__ == "__main__":     	# 判断执行名称
    main()						# 调用主函数
