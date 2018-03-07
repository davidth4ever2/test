Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 40%22
18
>>> 70%22
4
>>> 180/22
8
>>> 180%22
4
>>> 180/22
8
>>> a = [ [0,0,0] [0,0,0] [0,0,0] ]

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a = [ [0,0,0] [0,0,0] [0,0,0] ]
TypeError: list indices must be integers, not tuple
>>> a = [ [0,0,0], [0,0,0], [0,0,0] ]
>>> for i in a:
	for j in a:
		print j

		
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
>>> for i in a:
	for j in i:
		print j

		
0
0
0
0
0
0
0
0
0
>>> for i in a:
	for j in i:
		print j.index

		

Traceback (most recent call last):
  File "<pyshell#14>", line 3, in <module>
    print j.index
AttributeError: 'int' object has no attribute 'index'
>>> a[0][0] = 1
>>> a
[[1, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> a[0][0] = 1
