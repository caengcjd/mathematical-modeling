# coding:utf-8

import xlrd
import math


class Place(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connect = []
        self.length = []
        self.connect_type = []


class Car(object):
    def __init__(self, main_speed, normal_speed, type, start, target):
        self.main_speed = main_speed
        self.normal_speed = normal_speed
        self.type = type
        self.start = start
        self.target = target


D1, D2 = range(0, 2)
Z01, Z02, Z03, Z04, Z05, Z06 = range(2, 8)
F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25, F26, F27, F28, F29, F30, F31, F32, F33, F34, F35, F36, F37, F38, F39, F40, F41, F42, F43, F44, F45, F46, F47, F48, F49, F50, F51, F52, F53, F54, F55, F56, F57, F58, F59, F60 = range(
    8, 68)
J01, J02, J03, J04, J05, J06, J07, J08, J09, J10, J11, J12, J13, J14, J15, J16, J17, J18, J19, J20, J21, J22, J23, J24, J25, J26, J27, J28, J29, J30, J31, J32, J33, J34, J35, J36, J37, J38, J39, J40, J41, J42, J43, J44, J45, J46, J47, J48, J49, J50, J51, J52, J53, J54, J55, J56, J57, J58, J59, J60, J61, J62 = range(
    68, 130)

carList = [Car(70, 45, 'A', D1, -1), Car(70, 45, 'A', D1, -1), Car(70, 45, 'A', D1, -1), Car(60, 35, 'B', D1, -1),
           Car(60, 35, 'B', D1, -1), Car(60, 35, 'B', D1, -1), Car(50, 30, 'C', D1, -1), Car(50, 30, 'C', D1, -1),
           Car(50, 30, 'C', D1, -1), Car(50, 30, 'C', D1, -1), Car(50, 30, 'C', D1, -1), Car(50, 30, 'C', D1, -1),
           Car(70, 45, 'A', D2, -1), Car(70, 45, 'A', D2, -1), Car(70, 45, 'A', D2, -1), Car(60, 35, 'B', D2, -1),
           Car(60, 35, 'B', D2, -1), Car(60, 35, 'B', D2, -1), Car(50, 30, 'C', D2, -1), Car(50, 30, 'C', D2, -1),
           Car(50, 30, 'C', D2, -1), Car(50, 30, 'C', D2, -1), Car(50, 30, 'C', D2, -1), Car(50, 30, 'C', D2, -1)]

filename = "positions.xls"
data = xlrd.open_workbook(filename)
sh = data.sheet_by_name("Sheet1")
nrows = sh.nrows

Road = []
for x in range(1, nrows):
    Road.append(Place(sh.cell_value(x, 1), sh.cell_value(x, 2)))

INF = float('inf')
RoadMatrix = [[INF for i in range(130)] for i in range(130)]
for x in range(0, 130):
    RoadMatrix[x][x] = 0


def G(p1, p2, ctype=1):
    length = math.sqrt(
        (Road[p1].x - Road[p2].x) * (Road[p1].x - Road[p2].x) + (Road[p1].y - Road[p2].y) * (Road[p1].y - Road[p2].y))
    Road[p1].connect.append(p2)
    Road[p2].connect.append(p1)
    Road[p1].length.append(length)
    Road[p2].length.append(length)

    Road[p1].connect_type.append(ctype)
    Road[p2].connect_type.append(ctype)
    RoadMatrix[p1][p2] = length
    RoadMatrix[p2][p1] = length


G(D1, J11)
G(D1, J10)
G(D1, J09)
G(D1, Z03)
G(J11, J10, 0)
G(J11, J46)
G(J46, F43)
G(J46, J45)
G(J46, J44)
G(J10, J09, 0)
G(J45, J10)
G(J45, J09)
G(J45, J44)
G(J45, J42)
G(J44, F42)
G(J44, F41)
G(J44, Z05)
G(J44, J43)
G(Z05, J41)
G(J43, J19)
G(J09, J08, 0)
G(J09, Z03)
G(Z03, J52)
G(Z03, J57)
G(Z03, J61)
G(J61, F57)
G(J61, F58)
G(J61, J58)
G(J58, J57)
G(J58, J59)
G(J58, J55)
G(J59, J55)
G(J59, J53)
G(J59, F54)
G(J59, J62)
G(J62, F59)
G(J62, F60)
G(J62, J60)
G(J60, F56)
G(J60, F55)
G(J60, J56)
G(J56, F53)
G(J56, F52)
G(J56, J53)
G(J53, J55)
G(J53, F51)
G(J53, J50)
G(J50, F50)
G(J50, Z01)
G(J50, J04)
G(J50, J49)
G(J49, F49)
G(J49, F48)
G(J49, J05)
G(J54, J55)
G(J54, J57)
G(J54, Z02)
G(Z02, J52)
G(Z02, J51)
G(J51, J06)
G(J52, J07)
G(J52, J08)
G(Z01, J04)
G(Z01, J48)
G(J48, F47)
G(J48, F46)
G(J48, J03)
G(J48, J47)
G(J47, F45)
G(J47, F44)
G(J47, J02)
G(J02, J01, 0)
G(J02, J03, 0)
G(J03, J04, 0)
G(J04, J05, 0)
G(J05, J06, 0)
G(J06, J07, 0)
G(J07, J08, 0)
G(J08, J42)
G(J42, J38)
G(J42, J40)
G(J40, F39)
G(J40, F38)
G(J40, F37)
G(J40, J39)
G(J39, F36)
G(J39, J16)
G(J38, F35)
G(J38, F34)
G(J38, Z04)
G(Z04, J07)
G(Z04, J37)
G(J37, F32)
G(J37, F31)
G(J37, F33)
G(J37, J15)
G(J41, F40)
G(J41, J18)
G(J36, J06)
G(J36, F30)
G(J36, F29)
G(J36, J34)
G(J34, J05)
G(J34, F26)
G(J34, J35)
G(J34, J33)
G(J35, F28)
G(J35, F27)
G(J35, J14)
G(J33, F25)
G(J33, J04)
G(J33, J03)
G(J33, J32)
G(J32, F24)
G(J32, J03)
G(J32, D2)
G(J32, J12)
G(J32, J13)
G(D2, J12)
G(D2, J03)
G(D2, J02)
G(J12, J13, 0)
G(J13, J14, 0)
G(J14, J15, 0)
G(J15, J16, 0)
G(J16, J17, 0)
G(J17, J18, 0)
G(J18, J19, 0)
G(J19, J20, 0)
G(J20, J31)
G(J31, J19)
G(J31, F23)
G(J31, J29)
G(J31, J30)
G(J30, F22)
G(J30, F21)
G(J30, J29)
G(J29, J18)
G(J29, F20)
G(J29, J28)
G(J28, J30)
G(J28, F19)
G(J28, F18)
G(J28, J27)
G(J27, F14)
G(J27, F15)
G(J27, F16)
G(J27, F17)
G(J27, J26)
G(J26, F13)
G(J26, F12)
G(J26, Z06)
G(Z06, J16)
G(Z06, J25)
G(Z06, J28)
G(J25, J15)
G(J25, F10)
G(J25, F11)
G(J25, J23)
G(J25, J24)
G(J24, J26)
G(J24, F09)
G(J24, F08)
G(J24, J23)
G(J23, F07)
G(J23, J22)
G(J22, F04)
G(J22, F05)
G(J22, F06)
G(J22, J21)
G(J21, F01)
G(J21, F02)
G(J21, F03)
G(J21, J13)
G(J21, J14)


def dijkstra(graph, src):
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]  # 获取图中所有节点
    visited = []  # 表示已经路由到最短路径的节点集合
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance = {src: 0}  # 记录源节点到各个节点的距离
    for i in nodes:
        distance[i] = graph[src][i]  # 初始化
    # print(distance)
    path = {src: {src: []}}  # 记录源节点到每个节点的路径
    k = pre = src
    while nodes:
        mid_distance = float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v] + graph[v][d]
                if new_distance < mid_distance:
                    mid_distance = new_distance
                    graph[src][d] = new_distance  # 进行距离更新
                    k = d
                    pre = v
        distance[k] = mid_distance  # 最短路径
        path[src][k] = [i for i in path[src][pre]]
        path[src][k].append(k)
        # 更新两个节点集合
        visited.append(k)
        nodes.remove(k)
        # print(visited, nodes)  # 输出节点的添加过程
    return distance, path


def num2place(places):
    l = []
    for p in places:
        if p == 0:
            l.append("D1")
        elif p == 1:
            l.append("D2")
        elif 2 <= p < 8:
            l.append("Z0%d" % (p - 1))
        elif 8 <= p < 68:
            l.append("F%d" % (p - 7))
        elif 68 <= p < 130:
            l.append("J%d" % (p - 67))
    return l


d, p = dijkstra(RoadMatrix, D1)
print num2place(p[D1][J53])
