# coding:UTF-8
import tkinter, os							# 模块导入
LOGO_PATH = "f:\\resources" + os.sep + "p2585323764.ico"			# 图标
IMAGES_PATH = "f:\\resources" + os.sep + "p2585323764.png" 			# 图片
class MainForm: 							# 主窗体
    def __init__(self): 						# 构造方法
        root = tkinter.Tk()  					# 创建窗体
        root.title("www.candy.com")  				# 设置窗体标题
        root.iconbitmap(LOGO_PATH)  					# 设置窗体图标
        root.geometry("500x300")  					# 设置主窗体大小
        root.maxsize(1000, 600)  					# 设置窗体最大尺寸
        root["background"] = "LightSlateGray"  				# 设置背景颜色
        photo = tkinter.PhotoImage(file= IMAGES_PATH)  			# 定义图片
        button = tkinter.Button(root, text="点击搜索", image=photo,
		compound="bottom", fg="black", font=("微软雅黑", 20)) 	# 定义按钮
        button.pack()  						# 按钮显示
        root.mainloop()  						# 循环监听
def main():							# 主函数
   MainForm()							# 显示主窗体
   # canvas_test()                      # 窗体显示，画布绘制
#通过窗体创建画布，在画布上进行操作
def canvas_test():
    import tkinter
    window = tkinter.Tk()
    window.geometry('600x400')
    window.title('This is Canvas')
    # 创建550 * 300的画布
    canvas = tkinter.Canvas(window, bg='green', width=550, height=300)
    # 在画布上创建图像，放置导入图片
    image_file = tkinter.PhotoImage(file=IMAGES_PATH)
    image = canvas.create_image(300, 10, anchor='n', image=image_file)
    canvas.pack()
    window.mainloop()

if __name__ == "__main__":     					# 判断执行名称
    main()							# 调用主函数
