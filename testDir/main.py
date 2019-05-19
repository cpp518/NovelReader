import tkinter
import tkinter.messagebox
from testDir import mainWindow
from testDir import searchWindow
import tkinter.scrolledtext
import testDir.Mythread

componentList = []
totalResultList = []



def ReadLastestnovel(Obj,novelName,windows,number):

    global totalResultList

    Obj.insert("insert",totalResultList[number].GetLastestTxt())
    windows.destory()
    pass

def ReadLastest():
    pass


#显示搜索结果

def SearchDialog(novelName,MWindow):
    if len(novelName) < 1:
        tkinter.messagebox.showinfo("提示","请输入小说名称")
    else:
        searchWindow.SearchWindow(MWindow,novelName)

class MainWindow():

    def __init__(self):
        self.top = tkinter.Tk()
        self.top.geometry(mainWindow.mainWindow)
        self.top.resizable(0, 0)
        self.top.title(mainWindow.mainTitle)
        self.text = tkinter.scrolledtext.Text(self.top, font=("宋体", 12, "normal"))
        self.text.place(x=mainWindow.textX, y=mainWindow.textY, width=mainWindow.textWidth, height=mainWindow.textHeight)

        # 生成滚动条
        self.scroll = tkinter.Scrollbar()
        self.scroll.place(x=mainWindow.scrollX, y=mainWindow.scrollY, width=mainWindow.scrollWidth,
                     height=mainWindow.scrollHeight)

        # 设置滚动条和文本框关联
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)

        # 退出按钮
        self.exit = tkinter.Button(self.top, text="退出", command=self.top.destroy)
        self.exit.place(x=mainWindow.exitBtnX, y=mainWindow.exitBtnY, width=mainWindow.exitBtnWidth,
                   height=mainWindow.exitBtnHeight)

        # 测试用于是否能正常显示滚动条
        s = "1234567890\n" * 1000
        self.Open = tkinter.Button(self.top, text="打开", command=lambda: TextInsert(self.text, s))
        self.Open.place(x=475, y=400, width=50, height=50)

        # 输入框，用来输入小说名称
        self.Input = tkinter.Entry(self.top)
        self.Input.place(x=mainWindow.InputTxtX, y=mainWindow.InputTxtY, width=mainWindow.InputTxtWidth,
                    height=mainWindow.InputTxtHeight)

        # 搜索按钮
        self.SearchBtn = tkinter.Button(self.top, text="搜索", command=lambda: SearchDialog(self.Input.get(),self))
        self.SearchBtn.place(x=mainWindow.SearchBtnX, y=mainWindow.SearchBtnY, width=mainWindow.SearchBtnWidth,
                        height=mainWindow.SearchBtnHeight)

        # 设置按钮
        self.SettingBtn = tkinter.Button(self.top, text="设置")
        self.SettingBtn.place(x=mainWindow.SettingBtnX, y=mainWindow.SettingBtnY, width=mainWindow.SettingBtnWidth,
                         height=mainWindow.SettingBtnHeight)
        self.top.mainloop()

    def TextInsert(self, novel):
        self.text.insert("insert", novel)


if __name__ == '__main__':
    MainWindow()