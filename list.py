# list: written in square bracket 
# or list are used to store multiple value in 
#a single varaiable
 #-----------------------------------------------
# main uses of list: 
# 1. loist are ordered 
# 2. list nare changeable 
# 3. list are indexed 
# 4. list alowed duplicate values
# 5. list are written in square bracket 
# 6. here you can store  multiple data type 

#here you can store  multiple data type 
# x = [100,"friday",78.23,45j,"true","none",200,855]
# print("list : ",x)
# print("data type : ",type(x))
# print("length of list : ",len(x))
'''

x = ["sunday","monday","tuesday","wednesday","thurdsday","friday","saturday"]

 how to delete the value from the list
# 1. delete the sunday from the list 
x.pop(0) # write index number in bracket
x.pop()  # it will remove the last value


x.remove("sunday")
x.remove("monday")
# 2. delete the last value from the list 
# formulas 
# 1. pop : it is used to remove the
value from the list with the help of indexing 
and by defualt delete the last value
# 2. remove :
 it delete the value from list by values 
'''


#2. remove 
'''x = [12,45,78,12,55,45] '''
'''x.remove(12) # only first 12 is removed
print(x)
'''
#3. clear :- it deletes all values from the range
'''print(x)
x.clear()
print(x)
'''
 
 # 4. del: del is a keyboard that is used to delete 
 # the value according to index and according variable

 # x = [23,45,78,89,56,23,23]
 # del x[-1]   #indexing
 # del 








































































''' x = [45,78,89,56,253,23]
 a = x[-1::-1] # it will reverse the list
# print(a)
'''
'''
#1. 253 
a = x[-2]
print(a)
#2. [45,78]
a = x[0:2]
print(a)
#3. [23,253]
a = x[-1:-3:-1]
print(a)
#4. [89,78,45]
a = x[-4::-1]
print(a)
#5. [56,89]
a = x[-3:-5:-1]
print(a)
# or
a = x[3:1:-1]
print(a)'''
#-------------------------------------------------------------------

# x = [45,78,89,56,23,20,100]
# arrange in ascending order 
# 1. x.sort() :- it is used to arrange the data in ascending
# or descending order. 
# 2. sorted: it is used to arrange the data in ascending
# or descending order. 
'''
# Ascending order by sort()
x.sort()
print(x)
# Descending order by sort()
x.sort(reverse=True)
print(x)
'''
'''# Ascending order by sorted
y = sorted(x)
print(y)
# Descending order by sorted
y = sorted(x,reverse=True)
print(y)
'''
'''x = [45,89,56,25,41,10,96,35,78]
#1. arrnage the data in ascending order 
x.sort()
print(x)
#2. extract the maximum value from the list 
x.sort(reverse=True)
print(x[0])
#3. extract the minimum value from the list 
x.sort()
print(x[0])
#4. find the second highest value from the list 
x.sort(reverse=True)
print(x[1])
#5. show the second lowest value from the list
x.sort()
print(x[1])
#6. show the top three numbers from the list 
x.sort(reverse=True)
print(x[0:3])
#7. show the botoom three numbers from the list 
x.sort()
print(x[0:3]) '''

'''x = [45,89,56,25,41,10,96,35,78]
# Max :- it extract the maximum value from the list 
print (max(x))
# Min:- its extract the minimum value from the list 
print(min(x))'''
#---------------------------------------------------------------
'''x = ["sunday","monday","tuesday"]
x.sort(reverse=True)
print(x)
# reverse :- it is used to reverse the list 
x = [12,85,20,100]
x.reverse()
print(x)

# Count :- it is used to count the value from the list 
x = [12,45,78,89,56,12,45,12]
#Q1. count total number of 12 
a = x.count(12)
print(a)

# Index its shows the index of any value in list 
b = x.index(78)
print(b)

# Copy :- it isused to copy the list 
x = [12,45,78,89,23]
y = x.copy()
x.clear()
print(y)
print(x)'''
'''
x = [12,45,78,89,23,10]
#1. extract all the even numbers value from the list.
for i in x:
	if i%2==0:
		print(i)

#2. extract all the odd numbers from the list.
for i in x:
	if i%2!=0:
		print(i)
#3. create a blank list and add all even numbers from 
#the list. 
y = []
for i in x: 
	if i%2==0:
		y.append(i)

print(y)
#4. create a blank list and add all odd numbers from x.
y = []
for i in x:
	if i%2!=0:
		y.append(i)
print(y)'''



# x = [12,45,78,12,12,12]
#1. delete 12 from the list 
'''for i in x:
	if i==12:
		x.remove(i)
print(x)'''

# while 12 in x:
# 	x.remove(12)
# print(x)
#2. delete even numbers from the list

#3. delete odd numbers from the list


# nested list :- when one list used inside another list 
# it is called as nested list 

# x = [12,45,78,[1,2,3],100,200]
# print(x)
# print(len(x))
'''
x = [[1,2,3],[4,5,6],[7,8,9]]
# indexing 
# 2
print(x[0][1])
# 1
print(x[0][0])
# 5
print(x[1][1])
# 9
print(x[2][2])
# 7
print(x[2][0])
# 8
print(x[2][1])
'''
x = [[12,45,78,[100,200,300]]]

#Extract 
# 300
print(x[0][3][2])
# 78
print(x[0][2])
# 12
print(x[0][0])
# 45
print(x[0][1])
# 200
print(x[0][3][1])































