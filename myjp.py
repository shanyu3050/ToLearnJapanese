import pandas as pd
import numpy as np
import random
data=pd.read_excel("jp.xlsx")
word=data['汉字']
anno=data['假名(读音)']
pfsp=data['词性']
mean=data['词义']
chwo=data['纯汉字']
len=data.__len__()
def hanxuanyin(xiangshu):
    global len
    li=[-1]*xiangshu
    for i in range(xiangshu):
        already=1
        while(already==1):
            li[i]=random.randint(0,len-1)
            already=0
            for k in range(i):
                if(li[k]==li[i]):
                    already=1
                    break
    inser=random.randint(0,xiangshu-1)
    print('“',chwo[li[xiangshu-1]],'”的读音是_____。')
    for i in range(xiangshu):
        ch=chr(ord('A')+i)
        print(ch,end='. ')
        if(i<inser):
            print(anno[li[i]])
        if(i==inser):
            print(anno[li[xiangshu-1]])
        if(i>inser):
            print(anno[li[i-1]])
    ans=input("请输入您的答案：")
    print('其汉字表达为：',word[li[xiangshu-1]])
    print('其释义为：',mean[li[xiangshu-1]])
    print('其读音是：',anno[li[xiangshu-1]])
    if(ans==chr(ord('A')+inser)):
        print("回答正确！")
        return 1
    else:
        chh=chr(ord('A')+inser)
        print("回答错误！正确答案是：",chh)
        return -1

def yinxuanyi(xiangshu):
    global len
    li=[-1]*xiangshu
    for i in range(xiangshu):
        already=1
        while(already==1):
            li[i]=random.randint(0,len-1)
            already=0
            for k in range(i):
                if(li[k]==li[i]):
                    already=1
                    break
    inser=random.randint(0,xiangshu-1)
    print('“',anno[li[xiangshu-1]],'”的含义是_____。')
    for i in range(xiangshu):
        ch=chr(ord('A')+i)
        print(ch,end='. ')
        if(i<inser):
            print(mean[li[i]])
        if(i==inser):
            print(mean[li[xiangshu-1]])
        if(i>inser):
            print(mean[li[i-1]])
    ans=input("请输入您的答案：")
    print(anno[li[xiangshu-1]],'的汉字表达为：',word[li[xiangshu-1]])
    print(anno[li[xiangshu-1]],'的释义为：',mean[li[xiangshu-1]])
    if(ans==chr(ord('A')+inser)):
        print("回答正确！")
        return 1
    else:
        chh=chr(ord('A')+inser)
        print("回答错误！正确答案是：",chh)
        return -1


def yixuanyin(xiangshu):
    global len
    li=[-1]*xiangshu
    for i in range(xiangshu):
        already=1
        while(already==1):
            li[i]=random.randint(0,len-1)
            already=0
            for k in range(i):
                if(li[k]==li[i]):
                    already=1
                    break
    inser=random.randint(0,xiangshu-1)
    print('如果你想表达“',mean[li[xiangshu-1]],'”？')
    for i in range(xiangshu):
        ch=chr(ord('A')+i)
        print(ch,end='. ')
        if(i<inser):
            print(anno[li[i]])
        if(i==inser):
            print(anno[li[xiangshu-1]])
        if(i>inser):
            print(anno[li[i-1]])
    ans=input("请输入您的答案：")
    print('“',mean[li[xiangshu-1]],'”的汉字表达为：',word[li[xiangshu-1]])
    print(anno[li[xiangshu-1]],'的读音为：',anno[li[xiangshu-1]])
    if(ans==chr(ord('A')+inser)):
        print("回答正确！")
        return 1
    else:
        chh=chr(ord('A')+inser)
        print("回答错误！正确答案是：",chh)
        return -1

def hanpeiyin(xiangshu):
    totpoint=0
    wds=[-1]*xiangshu
    for i in range(xiangshu):
        flag=1
        while(flag==1):
            wds[i]=random.randint(0,len-1)
            flag=0
            for j in range(i):
                if(wds[i]==wds[j]):
                    flag=1
    linpei=[-1]*xiangshu
    picked=[0]*xiangshu
    for i in range(xiangshu):
        flag=1
        while(flag==1):
            linpei[i]=random.randint(0,xiangshu-1)
            flag=0
            if(picked[linpei[i]]==1):
                flag=1
            else:
                picked[linpei[i]]=1
    yourans=[' ']*xiangshu
    print("需要匹配的汉字和读音是：")
    for i in range(xiangshu-1):
        print(i+1,".",chwo[wds[i]],end='   ',sep='')
    print("")
    for i in range(xiangshu):
        print(chr(65+i),'.',anno[wds[linpei[i]]],end='   ',sep='')
    print("\n请输入您的答案：")
    for i in range(xiangshu-1):
        print(i+1,'.',chwo[wds[i]],end=':',sep='')
        yourans[i]=input('')
        if(yourans[i].__len__()>0 and ((ord(yourans[i])>=65 and ord(yourans[i])<=64+xiangshu) and linpei[ord(yourans[i])-65]==i)):
            print("匹配正确！")
            totpoint=totpoint+1
        else:
            print("匹配错误！")
            totpoint=totpoint-1
        print('“',word[wds[i]],'”的读音是',anno[wds[i]],',含义是“',mean[wds[i]],'”。')
    return totpoint
    
              
while(True):
    rt=random.randint(1,4)
    print('\n')
    if(rt==1):
        hanxuanyin(4)
    if(rt==2):
        yinxuanyi(4)
    if(rt==3):
        yixuanyin(4)
    if(rt==4):
        hanpeiyin(5)

#this is restored2
#new branch added