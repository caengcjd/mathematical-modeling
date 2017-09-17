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


def G(p1, p2, ctype):
    length = math.sqrt(abs(Road[p1].x - Road[p2].x) * abs(Road[p1].y - Road[p2].y))
    Road[p1].connect.append(p2)
    Road[p2].connect.append(p1)
    Road[p1].length.append(length)
    Road[p2].length.append(length)
    Road[p1].connect_type.append(ctype)
    Road[p2].connect_type.append(ctype)

G(D1, J11)
G(D1, J10)
G(D1, J09)
G(D1, Z03)