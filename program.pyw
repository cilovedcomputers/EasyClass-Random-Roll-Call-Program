import tkinter as tk
import tkinter.messagebox as msgbox
import turtle as t
from time import sleep
import random as r
import os
import sys

result = ""
whitelist = []
itemlist = []

def readwhitelist():
    try:
        f = open(os.path.split(os.path.realpath(sys.argv[0]))[0] + "\\whitelist.conf", "r+")
        text = f.read()
        lst = text.split("\n")
        f.close()
        return lst
    except Exception as errinfo:
        print(errinfo)
        return []

def readtotalnum():
    num = 48
    try:
        f = open(os.path.split(os.path.realpath(sys.argv[0]))[0] + "\\totalnum.conf", "r+")
        text = f.read()
        num = int(text)
        return num
    except Exception as errinfo:
        print(errinfo)
        return 48

def get_lists_coincidence(list1, list2):
    items = []
    for i in list1:
        for j in list2:
            if (j == i):
                items.append(j)
    return items

def judge_if_list_include_item(item, lst):
    for i in lst:
        if (i == item):
            return True
    return False

def main():
    # t.screensize(1024, 1024, "white")
    t.ht()
    t.up()
    t.goto(-0, 110)
    t.write("请稍等，即将开始随机点名", align="center", font=("黑体", 39))
    sleep(1)
    t.goto(0, 0)
    t.write("抽取到的学号为：", align="center", font=("黑体", 39))
    whitelist = readwhitelist()
    # print(readtotalnum())
    for i in range(readtotalnum()):
        if (judge_if_list_include_item(str(i + 1), whitelist) == False):
            itemlist.append(str(i + 1))
    # print(itemlist)
    choice = r.choice(itemlist)
    sleep(1)
    t.color("red")
    t.goto(0, -120)
    t.write(choice + "号", align="center", font=("微软雅黑", 40))
    sleep(1.3)
    return choice

if (__name__ == "__main__"):
    # tk.BitmapImage("./appicon.ico")
    result = main()
    tk.Tk().withdraw()
    msgbox.showinfo("Complete", "点名完成。抽取到的学号为：" + result + "号")
else:
    tk.Tk().withdraw()
    msgbox.showwarning("Error", "该程序目前仅支持用户手动运行。")