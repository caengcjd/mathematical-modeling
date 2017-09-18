from  Dijkstra   import   *
import threadpool
import  json

pool = threadpool.ThreadPool(24)




#cal   cost ,  type, 
def   cal_cost (graph,start ,end,speed):
	distance =  graph(start,end)
	time = distance /speed;





def   flood_all_cars(): # first time
	#tanxin suannfa
	rs={}
	rs=topk(D1,12)
	time = 0
	for  path  in  rs[0:6]:
		time = 0 
		for  p  in  path:
			if(p is single):
				time += distance(p)/30
			else :
				time += distance(p)/50
		if (time > max_time ) max_time = time 
	for distance in rs[7:9]:
		time 
	for distance in rs[10:12]:
		time 




	

def  read_path():
	file_object = open('./Path.txt')
	try:
	     all_the_text = file_object.read( )
	     return  json.loads(all_the_text)
	finally:
	     file_object.close( )

def  read_distance():
	file_object = open('./Distance.txt')
	try:
	     all_the_text = file_object.read( )
	     return  json.loads(all_the_text)
	finally:
	     file_object.close( )



if __name__ == '__main__':
	#print  read_path()
	start_time = time.time()
	pool = threadpool.ThreadPool(10) 
	requests = threadpool.makeRequests(sayhello, name_list) 
	[pool.putRequest(req) for req in requests] 
	pool.wait() 
	print '%d second'% (time.time()-start_time)
	#复制代码
