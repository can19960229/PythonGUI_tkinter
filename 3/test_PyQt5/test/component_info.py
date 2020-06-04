import tkinter

class ComponentInfo:
    def __init__(self):
        pass
        # self.No = ''
        # self.x = 0
        # self.y = 0
        # self.type = ''
        # self.value = 0
        # self.encapsulation = ''
        #

    def showComponent_info():           #self,No,type,value
        showInfomationForm = tkinter.Tk()
        showInfomationForm.title('元器件信息')
        showInfomationForm.geometry('200x80')
        showInfomationForm.maxsize(width=500, height=500)
        showInfomationForm['background'] = 'white'

        Label_No   = tkinter.Label(showInfomationForm,width=10,height=10,text='序号').place(x=20,y=20)
        Label_type = tkinter.Label(showInfomationForm,width=10,height=10,text='类型').place(x=20,y=50)