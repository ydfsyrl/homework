# -*- coding: utf-8 -*-

# student_dict={id:[名字，性别，专业，[课程号1、2、3]]}
# course_dict={id:[名字，时间，地点，老师，学分，[学生1、2、3]，人数]}

def addstudent(dict):
	list = []
	course_num = []
	
	addid = raw_input(u'\n输入学号: '.encode('gbk'))
	addname = raw_input(u'\n输入名字: '.encode('gbk'))
	addsex = raw_input(u'\n输入性别: '.encode('gbk'))
	addmajor = raw_input(u'\n输入专业: '.encode('gbk'))
	list.append(addname)
	list.append(addsex)
	list.append(addmajor)
	list.append(course_num)
	dict[addid] = list
	
def addcourse(dict):
	list = []
	student_num = []
	addid = raw_input(u'\n输入课程号: '.encode('gbk'))
	addname = raw_input(u'\n输入课程名: '.encode('gbk'))
	time = raw_input(u'\n输入上课时间: '.encode('gbk'))
	address = raw_input(u'\n输入上课地点: '.encode('gbk'))
	teacher = raw_input(u'\n输入老师名字: '.encode('gbk'))
	credit = raw_input(u'\n输入学分: '.encode('gbk'))
	limit = raw_input(u'\n输入限选人数: '.encode('gbk'))
	list.append(addname)
	list.append(time)
	list.append(address)
	list.append(teacher)
	list.append(credit)
	list.append(student_num)
	list.append(limit)
	dict[addid] = list
	
	
def savetofile(dic,filepath): #把dic保存在dump.txt
	try:
		import cPickle as pickle
	except ImportError:
		import pickle
	
	f = open(filepath, 'wb')
	pickle.dump(dic,f)	
	f.close()
	
	
def readfile(filepath): #读取dump.txt
	try:
		import cPickle as pickle
	except ImportError:
		import pickle
	
	f = open(filepath, 'rb')
	dic = pickle.load(f)
	f.close()
	return dic

def output_course(ckey,course_dict):
	print u'\n课程号: ',ckey 
	print u'课程名: ',course_dict[ckey][0]
	print  u'上课时间: ',course_dict[ckey][1]
	print  u'上课地点: ',course_dict[ckey][2]
	print  u'老师: ',course_dict[ckey][3]
	print  u'学分: ',course_dict[ckey][4] 
	print  u'限选人数： ',course_dict[ckey][6],'\n'
	
	'''
def passwd():
    chars = []
    sys.stdout.write(u'请输入密码: '.encode('gbk'))
    while True:       
        newChar = msvcrt.getch()
        if newChar in '\r\n': # 如果是换行，则输入结束
            print ''
            break
        else:
            chars.append(newChar)
            sys.stdout.write('*') # 显示为星号
    global mima
    mima = ''.join(chars)
'''


import  msvcrt
import sys
def mypasswd():
	chars = []
	print u'\n输入密码\n'.encode('gbk')
	while 1:
		newChar = msvcrt.getch()
		if newChar in '\r\n':
			break 
		else :
			chars.append(newChar)
			sys.stdout.write('*')		
	return ''.join(chars)

#************主函数************
import  msvcrt
import sys

student_filepath = 'D:\\student.txt'
course_filepath = 'D:\\course.txt'

student_dict = readfile(student_filepath)
course_dict = readfile(course_filepath)

#输入学生信息
'''
student_dict = {}

for x in [1,2,3,4,5]:
	addstudent(student_dict)
	
	
savetofile(student_dict,student_filepath)
'''

password = '12345'

print u'  ****************************\n        学生选课系统\n  ****************************'
inputpw = mypasswd()

if not inputpw == password:
	cs = 0
	print '\n'
	while(cs < 2):
		inputpw = mypasswd()
		print '\n'
		if inputpw ==password:
			print '\n'
			break
		cs = cs+1 
	if cs >= 2:
		exit()


i = '0'
while(not i == '4'):
	print u'''\n  ****************************\n        欢迎进入选课系统\n  ****************************\n
	1.课程管理
	2.学生信息管理
	3.学生选课
	4.退出系统  
	'''.encode('gbk')
#课程管理：查看，添加课程，删除课程，修改课程 返回
#学生信息管理：增加、删除学生，修改信息 返回
#选课：查看已选课程 选 退 返回

	i = raw_input(u"请输入菜单选项(1~4): ".encode('gbk'))
	print '\n'
	
	while ( not i in ['1','2','3','4']):
		i = raw_input(u"输入错误,请重输: ".encode('gbk'))
   
	if i == '1': #课程管理
		j1 = '0'
		
		while(not j1 == '6'):
			print u'\n          一、课程管理\n'
			print u'	1.查看所有课程'
			print u'	2.添加课程'
			print u'	3.删除课程'
			print u'	4.修改课程信息'
			print u'	5.查找课程'
			print u'	6.返回选课系统\n'
			
			j1 = raw_input(u"请输入菜单选项(1~6): ".encode('gbk'))
			while( not j1 in ['1','2','3','4','5','6']):
				j1 = raw_input(u"输入错误,请重输: ".encode('gbk'))
			print '\n'
			if j1 == '1':#查看课程
				keys = course_dict.keys()
				keys.sort()
		
				for key in keys:
					output_course(key,course_dict )
					
			if j1 == '2':#添加课程	
				addcourse(course_dict)
				
			if j1 == '3':#删除课程
				key = raw_input(u'\n输入课程号: '.encode('gbk'))
				if not key in course_dict.keys():
					print u'\n该课程不存在'
				else :
					output_course(key,course_dict )
				
					d = raw_input(u'\n是否删除该课程（Y or N）: '.encode('gbk'))
					if not d in ['Y','N']:
						d = raw_input(u'\n输入有误，请重新输入（Y or N）: '.encode('gbk'))
					if d =='Y':
						del course_dict[key]
			
			if j1 == '4':  #修改课程信息
				key = raw_input(u'\n输入要修改的课程号: '.encode('gbk'))
				if not key in course_dict.keys():
					print u'\n该课程不存在'
				else :
					output_course(key,course_dict )
					d = raw_input(u'\n是否修改该课程信息（Y or N）: '.encode('gbk'))
					while (not d in ['Y','N']):
						d = raw_input(u'\n输入有误，请重新输入（Y or N）: '.encode('gbk'))
					if d =='Y':
						l = '0'
						while(not l == '8'):
							print u'\n1.修改课程号'
							print u'2.修改课程名'
							print u'3.修改上课时间'
							print u'4.修改上课地点'
							print u'5.修改授课老师姓名'
							print u'6.修改学分'
							print u'7.修改限选人数'
							print u'8.完成修改\n'
							l = raw_input(u"请输入菜单选项(1~8): ".encode('gbk'))
							while (not l in ['1','2','3','4','5','6','7','8']):
								l = raw_input(u"输入错误,请重输: ".encode('gbk'))
							print '\n'
							if l == '1':
								num = raw_input(u'输入新课程号： '.encode('gbk'))
								while ( num in course_dict.keys()):
									num = raw_input(u'\n该课程号已存在，请重新输入: '.encode('gbk'))
								course_dict[num] = course_dict[key]
								del course_dict[key]
								for stu_id in student_dict:
									student_dict[stu_id][3] = [num if x == key else x for x in student_dict[stu_id][3]]
								
								
								
								key = num 
							if l =='2':
								course_dict[key][0] = raw_input(u'输入新课程名： '.encode('gbk'))
							if l == '3':
								course_dict[key][1] = raw_input(u'输入新上课时间： '.encode('gbk'))
							if l == '4':
								course_dict[key][2] = raw_input(u'输入新上课地点： '.encode('gbk'))
							if l == '5':
								course_dict[key][3] = raw_input(u'输入新授课老师姓名： '.encode('gbk'))
							if l == '6':
								course_dict[key][4] = raw_input(u'输入新学分： '.encode('gbk'))
							if l == '7':
								course_dict[key][6] = raw_input(u'输入新限选人数： '.encode('gbk'))
			
			
			if  j1 == '5':  #查找课程
				key = raw_input(u'\n输入课程号: '.encode('gbk'))
				if not key in course_dict.keys():
					print u'\n该课程不存在'
				else :
					output_course(key,course_dict )
				
			
	if i == '2': #学生信息管理
		j2 = '0'
		while(not j2 == '5'):
			print u'\n         二、学生信息管理\n'
			print u'	1.添加学生信息'
			print u'	2.删除学生信息'
			print u'	3.查询学生信息'
			print u'	4.修改学生信息'
			print u'	5.返回选课系统\n'
			
			j2 = raw_input(u"请输入菜单选项(1~5): ".encode('gbk'))
			while( not j2 in ['1','2','3','4','5']):
				j2 = raw_input(u"输入错误,请重输: ".encode('gbk'))
			print '\n'
			if j2 == '1':#添加学生信息
				addstudent(student_dict)
				
			if j2 == '2':#删除学生信息
				key = raw_input(u'\n输入学生学号: '.encode('gbk'))
				if not key in student_dict.keys():
					print u'\n该学生信息不存在'
				else :
					print u'\n学号: ',key 
					print u'姓名: ',student_dict[key][0]
					print  u'性别: ',student_dict[key][1]
					print  u'专业: ',student_dict[key][2],'\n'

				
					d = raw_input(u'\n是否删除该学生信息（Y or N）: '.encode('gbk'))
					if not d in ['Y','N']:
						d = raw_input(u'\n输入有误，请重新输入（Y or N）: '.encode('gbk'))
					if d =='Y':
						del student_dict[key]
			
			if j2 == '3':#查询学生信息
				key = raw_input(u'\n输入学生学号: '.encode('gbk'))
				if not key in student_dict.keys():
					print u'\n该学生信息不存在'
				else :
					print u'\n学号: ',key 
					print u'姓名: ',student_dict[key][0]
					print  u'性别: ',student_dict[key][1]
					print  u'专业: ',student_dict[key][2],'\n'
			
			if j2 == '4': #修改学生信息
				key = raw_input(u'\n输入要修改的学生学号: '.encode('gbk'))
				if not key in student_dict.keys():
					print u'\n该学生信息不存在'
				else :
					print u'\n学号: ',key 
					print u'姓名: ',student_dict[key][0]
					print  u'性别: ',student_dict[key][1]
					print  u'专业: ',student_dict[key][2],'\n'
					d = raw_input(u'\n是否修改该学生信息（Y or N）: '.encode('gbk'))
					while (not d in ['Y','N']):
						d = raw_input(u'\n输入有误，请重新输入（Y or N）: '.encode('gbk'))
					if d =='Y':
						l = '0'
						while(not l == '5'):
							print u'\n1.修改学生学号'
							print u'2.修改学生姓名'
							print u'3.修改学生性别'
							print u'4.修改学生专业'
							print u'5.完成修改\n'
							l = raw_input(u"请输入菜单选项(1~5): ".encode('gbk'))
							while (not l in ['1','2','3','4','5']):
								l = raw_input(u"输入错误,请重输: ".encode('gbk'))
							print '\n'
							if l == '1':
								num = raw_input(u'输入新学生学号： '.encode('gbk'))
								while ( num in student_dict.keys()):
									num = raw_input(u'\n该课程号已存在，请重新输入: '.encode('gbk'))
								student_dict[num] = student_dict[key]
								del student_dict[key]
								for cour_id in course_dict:
									course_dict[cour_id][5] = [num if x == key else x for x in course_dict[cour_id][5]]
								
								key = num 
							if l =='2':
								student_dict[key][0] = raw_input(u'输入新学生姓名： '.encode('gbk'))
							if l == '3':
								student_dict[key][1] = raw_input(u'输入新学生性别： '.encode('gbk'))
							if l == '4':
								student_dict[key][2] = raw_input(u'输入新学生专业： '.encode('gbk'))
			
					
					
	if i == '3': #学生选课
		j3 = '0'
		while(not j3 == '5'):
			print u'\n         三、学生选课\n'
			print u'	1.选课'
			print u'	2.退课'
			print u'	3.查询学生已选课程'
			print u'	4.查询已选课程学生名单'
			print u'	5.返回选课系统\n'
			
			j3 = raw_input(u"请输入菜单选项(1~5): ".encode('gbk'))
			while( not j3 in ['1','2','3','4','5']):
				j3 = raw_input(u"输入错误,请重输: ".encode('gbk'))
			print '\n'
			
			if j3 == '1': #选课	
				ckey = raw_input(u'\n输入课程号: '.encode('gbk'))
				if not ckey in course_dict.keys():
					print u'\n该课程不存在'
				else :
					output_course(ckey,course_dict)
					
				skey = raw_input(u'\n输入学生学号: '.encode('gbk'))  

				
				if not skey in student_dict.keys():
					print u'\n该学生信息不存在'
				elif int(course_dict[ckey][6]) == len(course_dict[ckey][5]): #选课人数已满
					print u'\n选课人数已满'
				
				else :
					selected_time = {}                          #已经有课的时间
					for num in student_dict[skey][3]:
						selected_time[num] = course_dict[num][1]
					g = 0
					for k in selected_time:                      
						if course_dict[ckey][1] == selected_time[k]:
							g = k 						#已选的时间冲突的课程号
			
					if ckey in student_dict[skey][3]:
						print u'\n已选本课程'
					elif  g :
						print u'\n该课程时间与 ',course_dict[k][0],u' 课冲突'
					else : 
						student_dict[skey][3].append(ckey)
						course_dict[ckey][5].append(skey)
						print u'选课成功'
			
			if j3 == '2':  #退课
				skey = raw_input(u'\n输入学生学号: '.encode('gbk')) 
				if not skey in student_dict.keys():
					print u'\n该学生信息不存在'
				else :
					print u'\n已选课程如下： '
					for x in student_dict[skey][3]:
						output_course(x,course_dict)
					ckey = raw_input(u'\n输入退课的课程号: '.encode('gbk'))
					d = raw_input( u'\n是否确认退课(Y or N)')
					while ( not d in ['Y','N']):
						d = raw_input( u'\n输入错误，请重新输入(Y or N)')
					if d == 'Y':
						student_dict[skey][3].remove(ckey)
					
			if j3 == '3':  #查询已选课程
				skey = raw_input(u'\n输入学生学号: '.encode('gbk'))  

				if not skey in student_dict.keys():
					print u'\n该学生信息不存在'
				else :
					print u'\n已选课程如下： '
					for x in student_dict[skey][3]:
						output_course(x,course_dict)
			
			if j3 == '4':
				key = raw_input(u'\n输入课程号: '.encode('gbk'))
				if not key in course_dict.keys():
					print u'\n该课程不存在'
				else :
					print u'\n该课学生名单如下: \n'
					for x in course_dict[key][5]:
						print u'\n学号: ',x 
						print u'姓名: ',student_dict[x][0]
						print  u'性别: ',student_dict[x][1]
						print  u'专业: ',student_dict[x][2],'\n'
		
savetofile(student_dict,student_filepath)
savetofile(course_dict,course_filepath)
			
			
				
