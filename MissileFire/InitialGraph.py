# coding:utf-8

import xlrd
import math
import json
from Dijkstra import dijkstra
from NumToPlaceString import num2place


class Place(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connect = []
        self.length = []
        self.connect_type = []


class Edge(object):
    def __init__(self, length):
        self.length = length
        self.car = -1


class Car(object):
    def __init__(self, main_speed, normal_speed, type, start_place, target_place):
        self.main_speed = main_speed
        self.normal_speed = normal_speed
        self.type = type
        self.start_place = start_place
        self.target_place = target_place
        self.path = []
        self.next_arrive_time = 0
        self.next_arrive_place = start_place


carList = [Car(70, 45, 'A', 'D1', -1),
           Car(70, 45, 'A', 'D1', -1),
           Car(70, 45, 'A', 'D1', -1),
           Car(60, 35, 'B', 'D1', -1),
           Car(60, 35, 'B', 'D1', -1),
           Car(60, 35, 'B', 'D1', -1),
           Car(50, 30, 'C', 'D1', -1),
           Car(50, 30, 'C', 'D1', -1),
           Car(50, 30, 'C', 'D1', -1),
           Car(50, 30, 'C', 'D1', -1),
           Car(50, 30, 'C', 'D1', -1),
           Car(50, 30, 'C', 'D1', -1),
           Car(70, 45, 'A', 'D2', -1),
           Car(70, 45, 'A', 'D2', -1),
           Car(70, 45, 'A', 'D2', -1),
           Car(60, 35, 'B', 'D2', -1),
           Car(60, 35, 'B', 'D2', -1),
           Car(60, 35, 'B', 'D2', -1),
           Car(50, 30, 'C', 'D2', -1),
           Car(50, 30, 'C', 'D2', -1),
           Car(50, 30, 'C', 'D2', -1),
           Car(50, 30, 'C', 'D2', -1),
           Car(50, 30, 'C', 'D2', -1),
           Car(50, 30, 'C', 'D2', -1)]

filename = "positions.xls"
data = xlrd.open_workbook(filename)
sh = data.sheet_by_name("Sheet1")
nrows = sh.nrows

Road = {}
for x in range(1, nrows):
    Road[num2place(x - 1)] = Place(sh.cell_value(x, 1), sh.cell_value(x, 2))

INF = float('inf')
RoadMatrix = {}
for x in range(0, 130):
    RoadMatrix[num2place(x)] = {num2place(x): 0}
    for y in range(0, 130):
        if x != y:
            RoadMatrix[num2place(x)][num2place(y)] = INF


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


def initG():
    G('D1', 'J11')
    G('D1', 'J10')
    G('D1', 'J9')
    G('D1', 'Z3')
    G('J11', 'J10', 2)
    G('J11', 'J46')
    G('J46', 'F43')
    G('J46', 'J45')
    G('J46', 'J44')
    G('J10', 'J9', 2)
    G('J45', 'J10')
    G('J45', 'J9')
    G('J45', 'J44')
    G('J45', 'J42')
    G('J44', 'F42')
    G('J44', 'F41')
    G('J44', 'Z5')
    G('J44', 'J43')
    G('Z5', 'J41')
    G('J43', 'J19')
    G('J9', 'J8', 2)
    G('J9', 'Z3')
    G('Z3', 'J52')
    G('Z3', 'J57')
    G('Z3', 'J61')
    G('J61', 'F57')
    G('J61', 'F58')
    G('J61', 'J58')
    G('J58', 'J57')
    G('J58', 'J59')
    G('J58', 'J55')
    G('J59', 'J55')
    G('J59', 'J53')
    G('J59', 'F54')
    G('J59', 'J62')
    G('J62', 'F59')
    G('J62', 'F60')
    G('J62', 'J60')
    G('J60', 'F56')
    G('J60', 'F55')
    G('J60', 'J56')
    G('J56', 'F53')
    G('J56', 'F52')
    G('J56', 'J53')
    G('J53', 'J55')
    G('J53', 'F51')
    G('J53', 'J50')
    G('J50', 'F50')
    G('J50', 'Z1')
    G('J50', 'J4')
    G('J50', 'J49')
    G('J49', 'F49')
    G('J49', 'F48')
    G('J49', 'J5')
    G('J54', 'J55')
    G('J54', 'J57')
    G('J54', 'Z2')
    G('Z2', 'J52')
    G('Z2', 'J51')
    G('J51', 'J6')
    G('J52', 'J7')
    G('J52', 'J8')
    G('Z1', 'J4')
    G('Z1', 'J48')
    G('J48', 'F47')
    G('J48', 'F46')
    G('J48', 'J3')
    G('J48', 'J47')
    G('J47', 'F45')
    G('J47', 'F44')
    G('J47', 'J2')
    G('J2', 'J1', 2)
    G('J2', 'J3', 2)
    G('J3', 'J4', 2)
    G('J4', 'J5', 2)
    G('J5', 'J6', 2)
    G('J6', 'J7', 2)
    G('J7', 'J8', 2)
    G('J8', 'J42')
    G('J42', 'J38')
    G('J42', 'J40')
    G('J40', 'F39')
    G('J40', 'F38')
    G('J40', 'F37')
    G('J40', 'J39')
    G('J39', 'F36')
    G('J39', 'J16')
    G('J38', 'F35')
    G('J38', 'F34')
    G('J38', 'Z4')
    G('Z4', 'J7')
    G('Z4', 'J37')
    G('J37', 'F32')
    G('J37', 'F31')
    G('J37', 'F33')
    G('J37', 'J15')
    G('J41', 'F40')
    G('J41', 'J18')
    G('J36', 'J6')
    G('J36', 'F30')
    G('J36', 'F29')
    G('J36', 'J34')
    G('J34', 'J5')
    G('J34', 'F26')
    G('J34', 'J35')
    G('J34', 'J33')
    G('J35', 'F28')
    G('J35', 'F27')
    G('J35', 'J14')
    G('J33', 'F25')
    G('J33', 'J4')
    G('J33', 'J3')
    G('J33', 'J32')
    G('J32', 'F24')
    G('J32', 'J3')
    G('J32', 'D2')
    G('J32', 'J12')
    G('J32', 'J13')
    G('D2', 'J12')
    G('D2', 'J3')
    G('D2', 'J2')
    G('J12', 'J13', 2)
    G('J13', 'J14', 2)
    G('J14', 'J15', 2)
    G('J15', 'J16', 2)
    G('J16', 'J17', 2)
    G('J17', 'J18', 2)
    G('J18', 'J19', 2)
    G('J19', 'J20', 2)
    G('J20', 'J31')
    G('J31', 'J19')
    G('J31', 'F23')
    G('J31', 'J29')
    G('J31', 'J30')
    G('J30', 'F22')
    G('J30', 'F21')
    G('J30', 'J29')
    G('J29', 'J18')
    G('J29', 'F20')
    G('J29', 'J28')
    G('J28', 'J30')
    G('J28', 'F19')
    G('J28', 'F18')
    G('J28', 'J27')
    G('J27', 'F14')
    G('J27', 'F15')
    G('J27', 'F16')
    G('J27', 'F17')
    G('J27', 'J26')
    G('J26', 'F13')
    G('J26', 'F12')
    G('J26', 'Z6')
    G('Z6', 'J16')
    G('Z6', 'J25')
    G('Z6', 'J28')
    G('J25', 'J15')
    G('J25', 'F10')
    G('J25', 'F11')
    G('J25', 'J23')
    G('J25', 'J24')
    G('J24', 'J26')
    G('J24', 'F9')
    G('J24', 'F8')
    G('J24', 'J23')
    G('J23', 'F7')
    G('J23', 'J22')
    G('J22', 'F4')
    G('J22', 'F5')
    G('J22', 'F6')
    G('J22', 'J21')
    G('J21', 'F1')
    G('J21', 'F2')
    G('J21', 'F3')
    G('J21', 'J13')
    G('J21', 'J14')


initG()
# dijkstra(RoadMatrix)  # create path and distance json

with open('./Path.txt', 'r') as f:
    json_path = f.read()
with open('./Distance.txt', 'r') as f:
    json_distance = f.read()

path = json.loads(json_path)
print path['D1']['D2']
