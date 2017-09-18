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
    return distance, path


    def topk(t, k):  #top k algorithm
        rs = {}  
        ll = []  
        for w, c in t: #遍历trie树  
            if len(ll) == k:  
                ll.append(c)  
                rs.setdefault(c, [])  
                rs[c].append(w)  
                if len(ll) == k:  
                    heapq.heapify(ll) #收集前k项，并且进行堆排序  
            else:  
                if c in ll:  
                    rs[c].append(w)   
                    continue   
                pc = heapq.heappushpop(ll, c) #弹出频度最小的一项   
                if pc in rs.keys():   
                    rs.pop(pc) #从结果集中剔除被弹出的搜索项   
                    rs.setdefault(c, [])   
                    rs[c].append(w)   
                    return rs  

    with open('./Path.txt', 'w') as f:
        f.write(json.dumps(path))
    with open('./Distance.txt', 'w') as f:
        f.write(json.dumps(distance))

