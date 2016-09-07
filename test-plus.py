class sort(object):
    def __init__(self,name):
        self.name = name
        self.iter = 0
        self.max_iter = 0
        self.score = 0
        self.total_score = 0
        self.avg_score = 0

    def add_items(self):
        if self.score > 0.5:
            self.iter += 1
        self.total_score += self.score
        return

    def print_items(self):
        print('姓名：', self.name, '       单字匹配度：', self.score, '      单字匹配成功次数：', self.iter, '      最大匹配度次数：', self.max_iter)
        return

    def print_result(self):
        self.avg_score = self.total_score/10
        print('姓名：', self.name, '      单字匹配成功次数：', self.iter, '      最大匹配度次数：', self.max_iter, '      平均匹配度', self.avg_score)


def add_max_iter(prop,k):
    for sort in sort_lists:
        if sort.score == prop:
            sort.max_iter += 1
            print('第', k+1, '次最高匹配度为：', sort.name, sort.score)

def result_writer():
    for sort in sort_lists:
        if sort.avg_score > 0.5:
            print('\n\t该句话为%s所写' % sort.name)

def get_sore(url,k):
    with open(url,'r') as fd:
        flists = fd.readlines()
        prop=0.0
        for i in range(len(flists)):
            sort_lists[i].score = float(flists[i][14:-1])
            sort_lists[i].add_items()
            if prop < float(flists[i][14:-1]):
                prop = float(flists[i][14:-1])
        add_max_iter(prop,k)
    return


if __name__=='__main__':
    GYC = sort('GYC')
    LJS1 = sort('LJS1')
    LJS2 = sort('LJS2')
    WTK = sort('WTK')
    YZQ = sort('YZQ')
    NYK = sort('NYK')
    sort_lists = [GYC, LJS1, LJS2, WTK, YZQ, NYK]

    name=['白', '日', '依', '山', '尽', '黄', '河', '入', '海', '流']
    for i in range(10):
        url='E:\\笔迹识别\\' + name[i] + '.txt'
        print('=======================================================================================')
        get_sore(url,i)
        for sort in sort_lists:
            sort.print_items()

    print('=======================================================================================')
    print('最终结果：')
    for sort in sort_lists:
        sort.print_result()
    result_writer()


