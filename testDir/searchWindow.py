# -*- utf-8 -*-
import tkinter
import testDir.Mythread
searchWindowSize = "600x500"

searchTitle = "搜索结果"

#支持的网站个数
webNumber = 1

#显示搜索结果的标签高度
resultHeight = 50

commitBtnX = 475
commitBtnY = 400
commitBtnWeight = 50
commitBtnHeight = 50

exitBtnX = 525
exitBtnY = 400
exitBtnWidth = 50
exitBtnHeight = 50

borderwidthLabel = 5

nameLabelX = 25
nameLabelY = 25
nameLabelWidth = 100
nameLabelHeight = 50

webnameLabelX = 125
webnameLabelY = 25
webnameLabelWidth = 100
webnameLabelHeight = 50

authorLabelX = 225
authorLabelY = 25
authorLabelWidth = 75
authorLabelHeight = 50

lastestChapterLabelX = 300
lastestChapterLabelY = 25
lastestChapterLabelWidth = 100
lastestChapterLabelHeight = 50

updateTimeLabelX = 420
updateTimeLabelY = 25
updateTimeLabelWidth = 100
updateTimeLabelHeight = 50

moreInfoBtnX = 540
moreInfoBtnY = 25
moreInfoBtnWidth = 50
moreInfoBtnHeight = 50


class SearchWindow():

    def __init__(self,MWindow,novelName):
        self.SearchDialog = tkinter.Toplevel(takefocus=True)
        self.SearchDialog.resizable(0, 0)

        self.SearchDialog.title(searchTitle)
        self.SearchDialog.geometry(searchWindowSize)
        # 创建确认按钮
         
        # SearchDialog.attributes("-topmost",1)
        # 创建退出按钮
        self.exitBtn = tkinter.Button(self.SearchDialog, text="退出",
                                 command=self.SearchDialog.destroy)
        self.exitBtn.place(x=exitBtnX, y=exitBtnY, width=exitBtnWidth,
                      height=exitBtnHeight)

        # 创建名称标签
        self.nameLabel = tkinter.Label(self.SearchDialog, text="小说名称", borderwidth=borderwidthLabel)
        self.nameLabel.place(x=nameLabelX, y=nameLabelY,
                        width=nameLabelWidth, height=nameLabelHeight)

        # 创建网站标签
        self.webnameLabel = tkinter.Label(self.SearchDialog, text="网站名称", borderwidth=borderwidthLabel)
        self.webnameLabel.place(x=webnameLabelX, y=webnameLabelY,
                           width=webnameLabelWidth, height=webnameLabelHeight)
        # 创建作者标签
        self.authorLabel = tkinter.Label(self.SearchDialog, text="作者", )
        self.authorLabel.place(x=authorLabelX, y=authorLabelY,
                          width=authorLabelWidth, height=authorLabelHeight)
        # 创建最新章节标签
        self.lastestChapterLabel = tkinter.Label(self.SearchDialog, text="最新章节", )
        self.lastestChapterLabel.place(x=lastestChapterLabelX, y=lastestChapterLabelY,
                                  width=lastestChapterLabelWidth,
                                  height=lastestChapterLabelHeight)

        # 创建更新时间标签
        self.updateTimeLabel = tkinter.Label(self.SearchDialog, text="更新时间")
        self.updateTimeLabel.place(x=updateTimeLabelX, y=updateTimeLabelY,
                              width=updateTimeLabelWidth, height=updateTimeLabelHeight)
        # 创建更多内容按钮
        self.moreInfoBtn = tkinter.Label(self.SearchDialog, text="更多章节")
        self.moreInfoBtn.place(x=moreInfoBtnX, y=moreInfoBtnY,
                          width=moreInfoBtnWidth, height=moreInfoBtnHeight)
        self.MWindow = MWindow
        # 多线程实现小说的获取


        self.totalResultList = testDir.Mythread.Allweb(novelName).GetWeb()
        # 关键字搜索到的小说内容
        for i in range(0, len(self.totalResultList)):
            # print(i)

            Result = self.totalResultList[i].GetNovelMessage()
            # 创建小说名称标签
            realNameLabel = tkinter.Label(self.SearchDialog, text=Result['novelTitle'])
            realNameLabel.place(x=nameLabelX,
                                y=nameLabelY + (i + 1) * resultHeight,
                                width=nameLabelWidth,
                                height=nameLabelHeight)
            # 创建网站名称标签
            realWebnameLabel = tkinter.Label(self.SearchDialog, text=Result['webname'])
            realWebnameLabel.place(x=webnameLabelX,
                                   y=webnameLabelY + (i + 1) * resultHeight,
                                   width=webnameLabelWidth,
                                   height=webnameLabelHeight)
            # 创建作者名称标签
            realAuthorLabel = tkinter.Label(self.SearchDialog, text=Result['novelAuthor'])
            realAuthorLabel.place(x=authorLabelX,
                                  y=authorLabelY + (i + 1) * resultHeight,
                                  width=webnameLabelHeight,
                                  height=webnameLabelHeight)
            # 创建最新章节按钮
            realLastestChapter = tkinter.Button(self.SearchDialog,
                                                text=Result['novelLastestChapter'],
                                                wraplength=80,
                                                command=lambda :self.ReadLastestnovel(i))
            realLastestChapter.place(x=lastestChapterLabelX,
                                     y=lastestChapterLabelY + (i + 1) * resultHeight,
                                     width=lastestChapterLabelWidth,
                                     height=lastestChapterLabelHeight)

            # 创建更新时间标签
            realUpdatetime = tkinter.Label(self.SearchDialog,
                                           text=Result['novelUpdateTime'])
            realUpdatetime.place(x=updateTimeLabelX,
                                 y=updateTimeLabelY + (i + 1) * resultHeight,
                                 width=updateTimeLabelWidth,
                                 height=updateTimeLabelHeight)
            # 创建更多章节按钮
            realmoreInfo = tkinter.Button(self.SearchDialog, text="更多章节", )
            realmoreInfo.place(x=moreInfoBtnX,
                               y=moreInfoBtnY + (i + 1) * resultHeight,
                               width=moreInfoBtnWidth,
                               height=moreInfoBtnHeight)

        self.SearchDialog.grab_set()
        self.SearchDialog.focus_set()
        self.SearchDialog.mainloop()

    def ReadLastestnovel(self,number):
        self.MWindow.TextInsert(self.totalResultList[number].GetLastestTxt())
        self.SearchDialog.destroy()

        pass

