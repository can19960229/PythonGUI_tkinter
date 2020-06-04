python GUI界面编程
	https://www.cnblogs.com/pywjh/p/9527828.html#ckcjybj
tkinter
	1. 事件处理
		鼠标事件
			Button-1>  鼠标左键
			<Button-2>   鼠标中间键（滚轮）
			<Button-3>  鼠标右键
			<Double-Button-1>   双击鼠标左键
			<Double-Button-3>   双击鼠标右键
			<Triple-Button-1>   三击鼠标左键
			<Triple-Button-3>   三击鼠标右键
			鼠标移动事件
			<B1-Motion>   鼠标左键滑动
			<B2-Motion>   鼠标滚轮移动
			<B3-Motion>   鼠标右键滑动
		事件绑定：
			command
				1. command是控件中的一个参数，如果使得command=函数，那么点击控件的时候将会触发函数
				2. 能够定义command的常见控件有: Button、Menu…
				3. 调用函数时，默认是没有参数传入的，如果要强制传入参数，可以考虑使用lambda
								
			bind
				bind的用法：控件.bind(event, handler),其中event是tkinter已经定义好的的事件，handler是处理器，可以是一个处理函数，如果相关事件发生, handler 函数会被触发, 事件对象 event 会传递给 handler 函数
				基本所有控件都能bind
			protocol
				protocol的使用：控件.protocol(protocol，handler)，其中控件为窗口对象(Tk,Toplevel)
				常见protocol有：
				WM_DELETE_WINDOW：最常用的协议称为WM_DELETE_WINDOW，用于定义用户使用窗口管理器明确关闭窗口时发生的情况。如果使用自己的handler来处理事件的话，这时候窗口将不会自动执行关闭
							
	2. 几何布局管理
		pack：垂直水平排列
			参考链接：https://blog.csdn.net/superfanstoprogram/article/details/83713196
		grid：网格排列
			Grid(网格)布局管理器会将控件放置到一个二维的表格里。主控件被分割成一系列的行和列，表格中的每个单元(cell)都可以放置一个控件。
		place：位置管理器
	3. 组件
		参考链接：https://www.runoob.com/python/python-gui-tkinter.html
		Button: 显示按钮
			master:指定按钮的父容器
			options:可选项，设置按钮属性
				常用属性值：
		Canvas：画布控件，显示图形元素
		Entry：输入控件
		Frame: 框架控件
		Label：标签控件,显示文本和位图
		Listbox	列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
		Menubutton	菜单按钮控件，用于显示菜单项。
		Menu	菜单控件；显示菜单栏,下拉菜单和弹出菜单
		Message	消息控件；用来显示多行文本，与label比较类似
		Radiobutton	单选按钮控件；显示一个单选的按钮状态
		Scale	范围控件；显示一个数值刻度，为输出限定范围的数字区间
		Scrollbar	滚动条控件，当内容超过可视化区域时使用，如列表框。.
		Text	文本控件；用于显示多行文本
		Toplevel	容器控件；用来提供一个单独的对话框，和Frame比较类似
		Spinbox	输入控件；与Entry类似，但是可以指定输入范围值
		PanedWindow	PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
		LabelFrame	labelframe 是一个简单的容器控件。常用与复杂的窗口布局。
		tkMessageBox	用于显示你应用程序的消息框。	
		
	4. 绘图
		自己绘制一个界面可以用于绘制电路图
	