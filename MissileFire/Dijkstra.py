# coding:utf-8
import copy
import json
from NumToPlaceString import num2place


def dijkstra(Graph):
    path = {}
    distance = {}
    for src in Graph.keys():
        graph = copy.deepcopy(Graph)
        path[src] = {src: [src]}  # 记录源节点到每个节点的路径
        distance[src] = {src: 0}  # 记录源节点到各个节点的距离
        nodes = [i for i in graph.keys()]  # 获取图中所有节点
        visited = []  # 表示已经路由到最短路径的节点集合
        if src in nodes:
            visited.append(src)
            nodes.remove(src)
        else:
            return None
        for i in nodes:
            distance[src][i] = graph[src][i]  # 初始化
        # print(distance)
        k = pre = src
        while nodes:
            mid_distance = float('inf')
            for v in visited:
                for d in nodes:
                    new_distance = graph[src][v] + graph[v][d]
                    if new_distance < mid_distance:
                        mid_distance = new_distance
                        k = d
                        pre = v
            graph[src][k] = mid_distance  # 进行距离更新
            distance[src][k] = mid_distance  # 最短路径
            path[src][k] = [i for i in path[src][pre]]
            path[src][k].append(k)
            # 更新两个节点集合
            visited.append(k)
            nodes.remove(k)
            # print(visited, nodes)  # 输出节点的添加过程
    with open('./Path.txt', 'w') as f:
        f.write(json.dumps(path))
    with open('./Distance.txt', 'w') as f:
        f.write(json.dumps(distance))
