import tkinter
from tkinter import messagebox
import douban
import re
import json
class Movetob():
    def __init__(self):
        # 生成主窗口
        self._root = tkinter.Tk()
        # 主窗口居中
        screenwidth = self._root.winfo_screenwidth()
        screenheight = self._root.winfo_screenheight()
        self._root.geometry(f"800x600+{int((screenwidth-800)/2)}+{int((screenheight-600)/2)}")
        #主窗口大小无法变化
        self._root.resizable(0,0)
        #获取豆瓣电影的分类
        self._classify_data = douban.get_classify()
        #电影数据
        self._movie = {}
        #按钮数据
        self._button = []

    def __get_move(self,url:str,index:str):
        if index not in self._movie.keys():
            url_id = re.findall(r'type=([1-9]{1,2})',url)
            self._movie[index] = douban.get_douban_json(id=url_id[0])
        self._text.config(state=tkinter.NORMAL)
        self._text.delete("1.0", "end")
        for i in self._movie[index]:
            #print(f"{'#' * 50}")
            self._text.insert("end",f"{'#' * 50}\n")
            #print(f"名称:{i['title']}", end='\n')
            self._text.insert("end",f"名称:{i['title']}\n")
            #print("类别:", end=" ")
            self._text.insert("end","类别:")
            for j in i['types']:
                #print(j, end="/")
                self._text.insert("end",f"{j}/")
            #print(f"\n豆瓣评分:{i['rating'][0]}\t排名:{i['rank']}\t制片国家/地区:", end=" ")
            self._text.insert("end",f"\n豆瓣评分:{i['rating'][0]}\t排名:{i['rank']}\t制片国家/地区:")
            for j in i['regions']:
                #print(j, end="/")
                self._text.insert("end", f"{j}/")
            #print("\n演员:", end="")
            self._text.insert("end","\n演员:")
            for j in i['actors']:
                #print(j, end=" ")
                self._text.insert("end", f"{j}/")
            #print(f"\n上映时间:{i['release_date']}")
            self._text.insert("end",f"\n上映时间:{i['release_date']}\n")
        self._text.config(state=tkinter.DISABLED)

    def __frame_left(self):
        # 生成右侧窗口
        self._fram_left = tkinter.Frame(self._root,height=600,width=200,bg='red',bd=2)
        self._fram_left.place(x=0,y=0)
        num = 0
        #生成分类的按钮
        for i in range(len(self._classify_data[1])):
            if num == 3 :
                num =0

            self._button.append(tkinter.Button(self._fram_left,text=self._classify_data[1][i],width=8,height=2,command=lambda id=self._classify_data[0][i],index=self._classify_data[1][i]: self.__get_move(id,index)))
            self._button[i].grid(row=int(i/3),column=num)
            num =num+1
    def __frame_right(self):
        # 生成右侧窗口
        self._frame_right = tkinter.Frame(self._root,height=600,width=600)
        self._frame_right.place(x=200,y=0)
        #生成文本窗口
        self._frame_text = tkinter.Frame(self._frame_right,height=550,width=600,bg='blue')
        self._frame_text.place(x=0,y=0)
        #文本框
        self._text = tkinter.Text(self._frame_text,height=33,width=72,font=("宋体",12))
        self._text.config(state=tkinter.DISABLED)
        self.text_scroll = tkinter.Scrollbar()
        self.text_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.text_scroll.config(command=self._text.yview)
        self._text.config(yscrollcommand=self.text_scroll.set)
        self._text.pack()
        # 翻页按钮
        #self._frame_button = tkinter.Frame(self._frame_right,height=50,width=600,bg='green')
        #self._frame_button.place(x=0,y=550)
        #tkinter.Button(self._frame_button,text="上一页",width=36,height=2,font=("宋体",12)).place(x=0,y=0)
        #tkinter.Button(self._frame_button,text="下一页",width=36,height=2,font=("宋体",12)).place(x=300,y=0)



    def start(self):
        self.__frame_left()
        self.__frame_right()
        self._root.mainloop()