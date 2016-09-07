class sort(object):
    def __init__(self,name):
        self.name=name
        self.iter=0
        self.max_iter=0
        self.score=0
        self.total_score=0
        self.avg_score=0

GYC=sort('GYC')
LJS1=sort('LJS1')
LJS2=sort('LJS2')
WTK=sort('WTK')
YZQ=sort('YZQ')
NYK=sort('NYK')
lists=[GYC,LJS1,LJS2,WTK,YZQ,NYK]

def add_items(sort):
    if sort.score>0.5:
        sort.iter+=1
    sort.total_score+=sort.score
    return

def add_max_iter(prop,k):
    for list in lists:
        if list.score==prop:
            list.max_iter+=1
            print('第',k+1,'次最高匹配度为：',list.name,list.score)

def result_writer():
    for list in lists:
        if list.avg_score>0.5:
            print('\n\t该句话为%s所写' %list.name)

def return_items(sort):
    print('姓名：',sort.name,'       单字匹配度：',sort.score,'      单字匹配成功次数：',sort.iter,'      最大匹配度次数：',sort.max_iter)
    return

def return_result(sort):
    sort.avg_score=sort.total_score/10
    print('姓名：',sort.name,'      单字匹配成功次数：',sort.iter,'      最大匹配度次数：',sort.max_iter,'      平均匹配度',sort.avg_score)

def get_sore(url,k):
    with open(url,'r') as fd:
        flists=fd.readlines()
        prop=0.0
        i=0
        for flist in flists:
            i+=1
            if i==1:
               GYC.score=float(flist[14:-1])
               add_items(GYC)
            elif i==2:
                LJS1.score=float(flist[14:-1])
                add_items(LJS1)
            elif i==3:
                LJS2.score=float(flist[14:-1])
                add_items(LJS2)
            elif i==4:
                WTK.score=float(flist[14:-1])
                add_items(WTK)
            elif i==5:
                YZQ.score=float(flist[14:-1])
                add_items(YZQ)
            elif i==6:
                NYK.score=float(flist[14:-1])
                add_items(NYK)
            if prop<float(flist[14:-1]):
                prop=float(flist[14:-1])
        add_max_iter(prop,k)
    return

name=['白','日','依','山','尽','黄','河','入','海','流']
for i in range(10):
    url='E:\\笔迹识别\\'+ name[i]+'.txt'
    print('=======================================================================================')
    get_sore(url,i)
    for list in lists:
        return_items(list)

print('=======================================================================================')
print('最终结果：')
for list in lists:
    return_result(list)
result_writer()


