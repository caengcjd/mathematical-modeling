# coding:utf-8
from  Dijkstra   import   *
import threadpool
import  json

pool = threadpool.ThreadPool(24)

main_road_list = []

graph = None
edge  = None 
to_f_1=[]
to_z=[]
to_f_2=[]
used_f= [] 
left_f=[]
path_z2f=[]
path_f2z=[]

#cal   cost ,  type, 
def   cal_cost (graph,start ,end,speed):
	distance =  graph(start,end)
	time = distance /speed;


def  path_time(point,type,prefix='D1'):
	global graph
	global edge
	global path
	time = 0
	speed_fast=0
	speed_slow=0
	if(type == 'A'):
		speed_fast=70
		speed_slow=45
	elif(type=='B'):
		speed_fast=60
		speed_slow=35
	elif(type=='C'):
		speed_fast=50
		speed_slow=30
	
	#prefix =  'D1'
	#print  path[point]
	i = 0 
	to_f_1.append({	type:path[point]})
	for   points  in  path[point]:
		i+=1
		if(i==1):
			continue 
		try :
			if   edge[prefix][points]["lanes"] == 2:
				time+= edge[prefix][points]["length"]/speed_fast
			else :
				time+= edge[prefix][points]["length"]/speed_slow
			prefix = points	
		except Exception as err:
			print prefix,points,point
	return time 

def  new_path_time(start,end,type):
	#global graph
	#global edge
	path =read_path()
	time = 1.0/6 # 
	speed_fast=0
	speed_slow=0
	if(type == 'A'):
		speed_fast=70
		speed_slow=45
	elif(type=='B'):
		speed_fast=60
		speed_slow=35
	elif(type=='C'):
		speed_fast=50
		speed_slow=30
	i = 0 
	#to_f_1.append({	type:path[point]})
	prefix = start 
	path_z2f.append({type:path[start][end]})
	#print start,end
	for   points  in  path[start][end]:
		i+=1
		if(i==1):
			continue 
		try :
			if   edge[prefix][points]["lanes"] == 2:
				time+= edge[prefix][points]["length"]/speed_fast
			else :
				time+= edge[prefix][points]["length"]/speed_slow
			prefix = points	
		except Exception as err:
			print prefix,points,point
	return time 


def   flood_all_cars(dict,prefix='D1'): # first time
	#tanxin algorithm
	rs=dict 
	global graph
	global used_f
	time = 0
	count = 0
	max_time=0
	for  k  in  dict:
		path= k[0] #point
		#print path
		if(path[:1] != "F" ) : # to itself
			continue
		count+=1
		used_f.append(path)
		#print count 
		if(0<count<=6):
			time = path_time(path,'C',prefix)
			if (time > max_time ) :
				max_time = time 
		elif(6<count<=9):
			time =0 
			time= path_time(path,'B',prefix)
			if(time > max_time):
				max_time = time 
		elif(9<count<=12):
			time = path_time(path,'A',prefix)
			if(time > max_time):
				max_time = time 
		elif(count>12):
			break
	return  max_time


def    flood_from_z(start,type):
	result={}
	time =0
	edge=read_edge()
	distance =  read_distance()
	#print  edge[start]
	#print start 
	global  used_f
	for  point in distance[start]:
		#print point
		if(point[:1]=='F' and point  not in used_f) :
			result[point]=distance[start][point]
		else:
			continue
	result= sorted(result.iteritems(), key=lambda d:d[1], reverse = False)
	#print  result[0][1]
	point = result[0][0]
	used_f.append(point)
	time = new_path_time(start,point,type)
	return  time 



def    flood_to_z_to_f(start,type):
	result={}
	time =0 
	distance =  read_distance()
	min_point=0
	min_path=0
	edge=read_edge()
	for  i  in   range(1,6):
		#print start,"Z"+str(i)
		length=distance[start]["Z"+str(i)]
		if(length>min_path):
			min_path=length
			min_point="Z"+str(i)
	#paths= path[start][min_point]
	time = new_path_time(start,min_point,type)
	time += flood_from_z(min_point,type)
	return time 




def  read_path():
	file_object = open('./Path.txt')
	try:
	     all_the_text = file_object.read( )
	     return  json.loads(all_the_text,encoding='utf-8')
	finally:
	     file_object.close( )

def  read_distance():
	file_object = open('./Distance.txt')
	try:
	     all_the_text = file_object.read( )
	     return  json.loads(all_the_text,encoding='utf-8')
	finally:
	     file_object.close( )

def  read_edge():
	file_object = open('./Edges.txt')
	try:
	     all_the_text = file_object.read( )
	     return  json.loads(all_the_text,encoding='utf-8')
	finally:
	     file_object.close( )


if __name__ == '__main__':
	#print  read_path()
	#start_time = time.time()
	global path
	path=read_path()["D1"]
	'''for  path  in paths["D1"]:
		print path'''
	distance =  read_distance()
	global edge
	edge = read_edge()
	global graph
	graph = distance["D1"]
	dict= sorted(graph.iteritems(), key=lambda d:d[1], reverse = False)
	max_time= flood_all_cars(dict)
	print max_time

	#D2 type 
	path=read_path()["D2"]
	graph = distance["D2"]
	dict= sorted(graph.iteritems(), key=lambda d:d[1], reverse = False)
	#print dict
	d2_max_time= flood_all_cars(dict,"D2")
	#print d2_max_time
	last_endpoint =[]
	print to_f_1,len(to_f_1) 
	for   car_path    in   to_f_1:
		for car,path  in car_path.items():
			last_endpoint.append({car:path})
			alltime = flood_to_z_to_f(path[-1],car)
			print car,path[-1],alltime




	#calculate the time of all delay




