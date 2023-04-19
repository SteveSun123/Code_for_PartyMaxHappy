import sys

# Party的最大快乐值
# 父亲节点来，孩子全部不能来；父亲节点不来，孩子可来，也可不来

class Employee():
    def __init__(self, happy):
        self.happy = happy
        self.nexts = []

def initCompany(arr):
    if arr == None or len(arr) == 0:
        return None
    head = Employee(arr[0])
    head.nexts.append(Employee(arr[1]))  # 列表从尾部添加元素使用list.append(elem)
    head.nexts.append(Employee(arr[2]))
    head.nexts.append(Employee(arr[3]))
    head.nexts[0].nexts.append(Employee(arr[4]))
    head.nexts[0].nexts.append(Employee(arr[5]))
    head.nexts[1].nexts.append(Employee(arr[6]))
    head.nexts[1].nexts[0].nexts.append(Employee(arr[7]))
    head.nexts[1].nexts[0].nexts.append(Employee(arr[8]))
    head.nexts[1].nexts[0].nexts.append(Employee(arr[9]))
    return head

def maxHappy(head):
    info = maxHappyProcess(head)
    return max(info.laiMax, info.buLaiMax)

class maxHappyInfo():
    def __init__(self, laiMax, buLaiMax):
        self.laiMax = laiMax
        self.buLaiMax = buLaiMax
def maxHappyProcess(head):
    if head == None:
        return 0
    if head.nexts == None or len(head.nexts) == 0:
        return maxHappyInfo(head.happy, 0)
    lai = head.happy  # 当前节点来的情况
    buLai = 0  # 当前节点不来的情况
    for each in head.nexts:  # 收集所有孩子的来和不来的信息
        eachInfo = maxHappyProcess(each)
        lai += eachInfo.buLaiMax  # 该孩子来时的信息
        buLai += max(eachInfo.laiMax, eachInfo.buLaiMax)  # 该孩子不来
    return maxHappyInfo(lai, buLai)

if __name__ == '__main__':
    a = [12, 34, 5, 64, 3, 2, 5, 7, 34, 8]
    head = initCompany(a)
    print(maxHappy(head))