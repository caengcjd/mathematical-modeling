# coding:utf-8
from  Dijkstra   import   *
import threadpool
import  json
import sys

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


def  read_path():
	file_object = open('./Path.txt')
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
	#path_z2f.append({type:path[start][end]})
	#print start,end
	edge=read_edge()
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



'''def  cal_totaltime(d1a1_f,d1a2_f,d1a3_f,d1b1_f,d1b2_f,d1b3_f,d1c1_f,d1c2_f,d1c3_f,d1c4_f,d1c5_f,d1c6_f,
	 	    d2a1_f,d2a2_f,d2a3_f,d2b1_f,d2b2_f,d2b3_f,d2c1_f,d2c2_f,d2c3_f,d2c4_f,d2c5_f,d2c6_f,
	 	    d1a1_z,d1a2_z,d1a3_z,d1b1_z,d1b2_z,d1b3_z,d1c1_z,d1c2_z,d1c3_z,d1c4_z,d1c5_z,d1c6_z,
	 	    d2a1_z,d2a2_z,d2a3_z,d2b1_z,d2b2_z,d2b3_z,d2c1_z,d2c2_z,d2c3_z,d2c4_z,d2c5_z,d2c6_z,
	 	    d1a1_f2,d1a2_f2,d1a3_f2,d1b1_f2,d1b2_f2,d1b3_f2,d1c1_f2,d1c2_f2,d1c3_f2,d1c4_f2,d1c5_f2,d1c6_f2,
	 	    d2a1_f2,d2a2_f2,d2a3_f2,d2b1_f2,d2b2_f2,d2b3_f2,d2c1_f2,d2c2_f2,d2c3_f2,d2c4_f2,d2c5_f2,d2c6_f2):'''

	
'''{'C': 'D1F43'}, {'C': 'D1F58'}, {'C': 'D1F57'}, {'C': 'D1F42'}, {'C': 'D1F41'}, {'C': 'D1F34'}, {'B': 'D1F35'}, {'B': 'D1F31'}, {'B': 'D1F32'}, {'A': 'D1F29'}, {'A': 'D1F30'}, {'A': 'D1F33'}, {'C': 'D2F24'}, {'C': 'D2F25'}, {'C': 'D2F47'}, {'C': 'D2F46'}, {'C': 'D2F44'}, {'C': 'D2F45'},
 {'B': 'D2F3'}, {'B': 'D2F2'}, {'B': 'D2F1'}, {'A': 'D2F26'}, {'A': 'D2F49'}, {'A': 'D2F48'}
{'C': 'F43Z1'}, {'C': 'Z1F51'}, {'C': 'F58Z5'}, {'C': 'Z5F40'}, {'C': 'F57Z5'}, {'C': 'Z5F20'}, {'C': 'F42Z1'}, {'C': 'Z1F54'}, {'C': 'F41Z1'}, {'C': 'Z1F27'}, {'C': 'F34Z1'}, {'C': 'Z1F28'},
 {'B': 'F35Z1'}, {'B': 'Z1F52'}, {'B': 'F31Z1'}, {'B': 'Z1F53'}, {'B': 'F32Z1'}, {'B': 'Z1F55'}, {'A': 'F29Z5'}, {'A': 'Z5F23'}, {'A': 'F30Z5'}, {'A': 'Z5F19'}, {'A': 'F33Z1'}, {'A': 'Z1F56'}, 
 {'C': 'F24Z3'}, {'C': 'Z3F60'}, {'C': 'F25Z5'}, {'C': 'Z5F21'}, {'C': 'F47Z5'}, {'C': 'Z5F22'}, {'C': 'F46Z5'}, {'C': 'Z5F18'}, {'C': 'F44Z5'}, {'C': 'Z5F36'}, {'C': 'F45Z5'}, {'C': 'Z5F15'},
  {'B': 'F3Z3'}, {'B': 'Z3F59'}, {'B': 'F2Z3'}, {'B': 'Z3F37'}, {'B': 'F1Z3'}, {'B': 'Z3F39'}, {'A': 'F26Z5'}, {'A': 'Z5F17'}, {'A': 'F49Z5'}, {'A': 'Z5F16'}, {'A': 'F48Z5'}, {'A': 'Z5F14'}

['D1F29', 'D1F30', 'D1F33','D1F35', 'D1F31', 'D1F32',D1F43', 'D1F58', 'D1F57', 'D1F42', 'D1F41', 'D1F34',
 'D2F26', 'D2F49', 'D2F48','D2F3', 'D2F2', 'D2F1','D2F24', 'D2F25', 'D2F47', 'D2F46', 'D2F44', 'D2F45',
 'F29Z5', 'F30Z5','F33Z1',  'F35Z1', 'F31Z1',  'F32Z1', 'F43Z1', 'F58Z5', 'F57Z5', 'F42Z1','F41Z1','F34Z1',
 'F26Z5',  'F49Z5', 'F48Z5','F3Z3' , 'F2Z3' , 'F1Z3','F24Z3', 'F25Z5', 'F47Z5', 'F46Z5', 'F44Z5' ,'F45Z5',
 'Z5F23',  'Z5F19','Z1F56', 'Z1F52', 'Z1F53',  'Z1F55', 'Z1F51',  'Z5F40', 'Z5F20','Z1F54', 'Z1F27','Z1F28',
'Z5F17',   'Z5F16', 'Z5F14','Z3F59','Z3F37', 'Z3F39', 'Z3F60', 'Z5F21', 'Z5F22',  'Z5F18', 'Z5F36', 'Z5F15']
'''

def  cal_totaltime(sys):

	sys_argv=sys
	first_max_time=0
	for i in range(1, 3):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'A')
		if time > first_max_time:
			first_max_time= time
	for i in range(13, 15):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'A')
		if time > first_max_time:
			first_max_time= time		    	

	for i in range(4, 6):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'B')
		if time > first_max_time:
			first_max_time= time
	for i in range(16, 18):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'B')
		if time > first_max_time:
			first_max_time= time
	for i in range(7, 12):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'C')
		if time > first_max_time:
			first_max_time= time
	for i in range(19, 24):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'C')
		if time > first_max_time:
			first_max_time= time
	#print first_max_time



	second_max_time =0
	for i in range(25, 27):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'A')+new_path_time(split_str(sys_argv[i+12])[0],split_str(sys_argv[i+12])[1],'A')
		if time >second_max_time:
			second_max_time= time

	for i in range(37, 39):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'A')+new_path_time(split_str(sys_argv[i+12])[0],split_str(sys_argv[i+12])[1],'A')
		if time >second_max_time:
			second_max_time= time
	for i in range(28, 30):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'B')+new_path_time(split_str(sys_argv[i+12])[0],split_str(sys_argv[i+12])[1],'B')
		if time >second_max_time:
			second_max_time= time
	for i in range(40, 42):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'B')+new_path_time(split_str(sys_argv[i+12])[0],split_str(sys_argv[i+12])[1],'B')
		if time >second_max_time:
			second_max_time= time

	for i in range(31, 37):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'C')+new_path_time(split_str(sys_argv[i+12])[0],split_str(sys_argv[i+12])[1],'C')
		if time >second_max_time:
			second_max_time= time
	for i in range(43, 49):
		time =new_path_time(split_str(sys_argv[i])[0],split_str(sys_argv[i])[1],'C')+new_path_time(split_str(sys_argv[i+12])[0],split_str(sys_argv[i+12])[1],'C')
		if time >second_max_time:
			second_max_time= time
	return  first_max_time+second_max_time


def   split_str(strs):
	first=[]
	first.append(strs[0])
	second=[]
	ite=first
	for i  in  range(1,len(strs)):
		if  strs[i].isdigit():
			ite.append(str(strs[i]))
		elif  strs[i].isalpha():
			ite=second
			ite.append(strs[i])
 	return   ''.join(first), ''.join(second)




if __name__ == '__main__':
	sys=['D1F29', 'D1F30', 'D1F33','D1F35', 'D1F31', 'D1F32','D1F43', 'D1F58', 'D1F57', 'D1F42', 'D1F41', 'D1F34',
 'D2F26', 'D2F49', 'D2F48','D2F3', 'D2F2', 'D2F1','D2F24', 'D2F25', 'D2F47', 'D2F46', 'D2F44', 'D2F45',
 'F29Z5', 'F30Z5','F33Z1',  'F35Z1', 'F31Z1',  'F32Z1', 'F43Z1', 'F58Z5', 'F57Z5', 'F42Z1','F41Z1','F34Z1',
 'F26Z5',  'F49Z5', 'F48Z5','F3Z3' , 'F2Z3' , 'F1Z3','F24Z3', 'F25Z5', 'F47Z5', 'F46Z5', 'F44Z5' ,'F45Z5',
 'Z5F23',  'Z5F19','Z1F56', 'Z1F52', 'Z1F53',  'Z1F55', 'Z1F51',  'Z5F40', 'Z5F20','Z1F54', 'Z1F27','Z1F28',
'Z5F17',   'Z5F16', 'Z5F14','Z3F59','Z3F37', 'Z3F39', 'Z3F60', 'Z5F21', 'Z5F22',  'Z5F18', 'Z5F36', 'Z5F15']
	print cal_totaltime(sys)
	#print  split_str('D1234F4533')[0]