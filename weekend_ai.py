Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> board = 0,1,2,3,4,5,6,7,8
>>> board
(0, 1, 2, 3, 4, 5, 6, 7, 8)
>>> type(board)
<type 'tuple'>
>>> board =[1,2,3,4,5,6,7,8]
>>> type(board)
<type 'list'>
>>> board
[1, 2, 3, 4, 5, 6, 7, 8]
>>> new_board = [ [1,2,3],[4,5,6],[7,8,0]
	      ]
>>> new_board
[[1, 2, 3], [4, 5, 6], [7, 8, 0]]
>>> for i in board:
	println i
	
SyntaxError: invalid syntax
>>> for i in board:
	print i

	
1
2
3
4
5
6
7
8
>>> for i in board:
	print board[i]

	
2
3
4
5
6
7
8

Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    print board[i]
IndexError: list index out of range
>>> board = ['0','1','2','3','4','5','6','7','8']
>>> board
['0', '1', '2', '3', '4', '5', '6', '7', '8']
>>> for i in board:
	print board[i]

	

Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    print board[i]
TypeError: list indices must be integers, not str
>>> for i in board:
	print i

	
0
1
2
3
4
5
6
7
8
>>> new_board = [ ['0'.'0'.'0'],['0','0','0'],['0','0','0']]
SyntaxError: invalid syntax
>>> new_board = [ ['0','0','0'],['0','0','0'],['0','0','0']]
>>> new_board
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
>>> for i in new_board:
	print(max(i))

	
0
0
0
>>> for i in new_board:
	print(len(i))

	
3
3
3
>>> for i in new_board:
	print(len(i)-1)

	
2
2
2
>>> for i in new_board:
	for j in new_board[i]:
		for k in board:
			new_board[i] = board[k]

			

Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    for j in new_board[i]:
TypeError: list indices must be integers, not list
>>> for i,j in new_board:
	print i

	

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for i,j in new_board:
ValueError: too many values to unpack
>>> for i in new_board:
	print i

	
['0', '0', '0']
['0', '0', '0']
['0', '0', '0']
>>> for i in new_board[0]:
	print i

	
0
0
0
>>> for i in new_board:
	for x in i:
		print i

		
['0', '0', '0']
['0', '0', '0']
['0', '0', '0']
['0', '0', '0']
['0', '0', '0']
['0', '0', '0']
['0', '0', '0']
['0', '0', '0']
['0', '0', '0']
>>> for i in new_board:
	for x in new_board[i.index]:
		print x

		

Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    for x in new_board[i.index]:
TypeError: list indices must be integers, not builtin_function_or_method
>>> for i in new_board:
	for x in i:
		print x

		
0
0
0
0
0
0
0
0
0
>>> for board_piece in board:
	for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		     new_board_horizational_index = board_piece

		     
>>> print new_board
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
>>> for board_piece in board:
	for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		    print new_board++
		    
SyntaxError: invalid syntax
>>> for board_piece in board:
	for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:new_board
	    temporary_memory = board_piece
	    print temporary_memory

	    
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
0
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
0
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
0
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
1
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
1
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
1
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
2
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
2
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
2
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
3
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
3
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
3
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
4
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
4
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
4
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
5
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
5
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
5
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
6
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
6
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
6
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
7
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
7
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
7
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
8
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
8
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
8
>>> for board_piece in board:
	for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:new_board
	        temporary_memory = board_piece
	        print temporary_memory
	        
  File "<pyshell#59>", line 4
    temporary_memory = board_piece
    ^
IndentationError: unexpected indent
>>> for board_piece in board:
	for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		    temporary_memory = board_piece
	            print temporary_memory

	            
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
3
4
4
4
4
4
4
4
4
4
5
5
5
5
5
5
5
5
5
6
6
6
6
6
6
6
6
6
7
7
7
7
7
7
7
7
7
8
8
8
8
8
8
8
8
8
>>> 
>>> 


for board_piece in board:

/
  File "<pyshell#63>", line 6
    /
    ^
IndentationError: expected an indented block
>>> for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		    temporary_memory = board[2]
	            print temporary_memory

	            
2
2
2
2
2
2
2
2
2
>>> i =0
>>> for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		    temporary_memory = board[i]
	            print temporary_memory
	            i = i + 1

	            
0
1
2
3
4
5
6
7
8
>>> print new_board
[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
>>> for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		    temporary_memory = board[i]
	            print temporary_memory
	            i = i + 1
	            new_board_horizational_index = temporary_memory

	            

Traceback (most recent call last):
  File "<pyshell#74>", line 3, in <module>
    temporary_memory = board[i]
IndexError: list index out of range
>>> for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		    temporary_memory_address = new_boaod_horizational_index
		    print temporary_memory_address

		    

Traceback (most recent call last):
  File "<pyshell#77>", line 3, in <module>
    temporary_memory_address = new_boaod_horizational_index
NameError: name 'new_boaod_horizational_index' is not defined
>>> for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		    temporary_memory_address = new_baord_horizational_index
		    print temporary_memory_address

		    

Traceback (most recent call last):
  File "<pyshell#79>", line 3, in <module>
    temporary_memory_address = new_baord_horizational_index
NameError: name 'new_baord_horizational_index' is not defined
>>> for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		    temporary_memory_address = new_baord_horizational_index
		    print temporary_memory_addressfor new_board_vertical_index in new_board:
		    	    for new_board_horizational_index  in new_board_vertical_index:
		    		    temporary_memory = board[i]
		    	            print temporary_memory
		    	            i = i + 1
		    	            
SyntaxError: invalid syntax
>>> for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		    temporary_memory_address = new_baord_horizational_index
		    print temporary_memory_address

		    

Traceback (most recent call last):
  File "<pyshell#82>", line 3, in <module>
    temporary_memory_address = new_baord_horizational_index
NameError: name 'new_baord_horizational_index' is not defined
>>> for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board_vertical_index:
		    temporary_memory_address = new_board_horizational_index
		    print temporary_memory_address

		    
0
0
0
0
0
0
0
0
0
>>> for new_board_vertical_index in new_board:
	    for new_board_horizational_index  in new_board[new_board_vertical_index]:
		    temporary_memory_address = new_board_horizational_index
		    print temporary_memory_address

		    

Traceback (most recent call last):
  File "<pyshell#86>", line 2, in <module>
    for new_board_horizational_index  in new_board[new_board_vertical_index]:
TypeError: list indices must be integers, not list
>>> for new_board_vertical_axis in new_board:
	    for new_board_horizational_index  in new_board[new_board_vertical_axis.index]:
		    temporary_memory_address = new_board_horizational_index
		    print temporary_memory_address

		    

Traceback (most recent call last):
  File "<pyshell#88>", line 2, in <module>
    for new_board_horizational_index  in new_board[new_board_vertical_axis.index]:
TypeError: list indices must be integers, not builtin_function_or_method
>>> for new_board_vertical_axis in new_board:
	    for new_board_horizational_index  in new_board[int(new_board_vertical_axis.index)]:
		    temporary_memory_address = new_board_horizational_index
		    print temporary_memory_address

		    

Traceback (most recent call last):
  File "<pyshell#90>", line 2, in <module>
    for new_board_horizational_index  in new_board[int(new_board_vertical_axis.index)]:
TypeError: int() argument must be a string or a number, not 'builtin_function_or_method'
>>> for new_board_vertical_axis in new_board:
	    print new_board_vertical_axis

	    
['0', '0', '0']
['0', '0', '0']
['0', '0', '0']
>>> for new_board_vertical_axis in new_board:
	    for  new_board_horizontal_item in new_board_vertical_axis
	    
SyntaxError: invalid syntax
>>> for new_board_vertical_axis in new_board:
	    for  new_board_horizontal_item in new_board_vertical_axis
	    
SyntaxError: invalid syntax
>>> 
>>> for new_board_vertical_axis in new_board:
	    for  new_board_horizontal_item in new_board_vertical_axis:
		    print new_board_horizontal_item

		    
0
0
0
0
0
0
0
0
0
>>> import random
>>> for i in range(1,100):
	print i

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> for i in range(0,9):
	if(i%2==0):
		print i

		
0
2
4
6
8
>>> for i in range(0,9):
	if(i%2<>0):
		print i

		
1
3
5
7
>>> for i in range(0,9):
	for x in range(0,9)
	
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9)
		
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
			if(x * y < 0):
				print x*y

				
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    for x in range(0,9):
			    result = x*y
			    print '{0:4d}*{1:4d}={2:4d}'.format(x,y,results)

			    

Traceback (most recent call last):
  File "<pyshell#119>", line 6, in <module>
    print '{0:4d}*{1:4d}={2:4d}'.format(x,y,results)
NameError: name 'results' is not defined
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    for x in range(0,9):
			    result = x*y
			    print '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)

			    
   0*   0=   0
   1*   0=   0
   2*   0=   0
   3*   0=   0
   4*   0=   0
   5*   0=   0
   6*   0=   0
   7*   0=   0
   8*   0=   0
   0*   1=   0
   1*   1=   1
   2*   1=   2
   3*   1=   3
   4*   1=   4
   5*   1=   5
   6*   1=   6
   7*   1=   7
   8*   1=   8
   0*   2=   0
   1*   2=   2
   2*   2=   4
   3*   2=   6
   4*   2=   8
   5*   2=  10
   6*   2=  12
   7*   2=  14
   8*   2=  16
   0*   3=   0
   1*   3=   3
   2*   3=   6
   3*   3=   9
   4*   3=  12
   5*   3=  15
   6*   3=  18
   7*   3=  21
   8*   3=  24
   0*   4=   0
   1*   4=   4
   2*   4=   8
   3*   4=  12
   4*   4=  16
   5*   4=  20
   6*   4=  24
   7*   4=  28
   8*   4=  32
   0*   5=   0
   1*   5=   5
   2*   5=  10
   3*   5=  15
   4*   5=  20
   5*   5=  25
   6*   5=  30
   7*   5=  35
   8*   5=  40
   0*   6=   0
   1*   6=   6
   2*   6=  12
   3*   6=  18
   4*   6=  24
   5*   6=  30
   6*   6=  36
   7*   6=  42
   8*   6=  48
   0*   7=   0
   1*   7=   7
   2*   7=  14
   3*   7=  21
   4*   7=  28
   5*   7=  35
   6*   7=  42
   7*   7=  49
   8*   7=  56
   0*   8=   0
   1*   8=   8
   2*   8=  16
   3*   8=  24
   4*   8=  32
   5*   8=  40
   6*   8=  48
   7*   8=  56
   8*   8=  64
   0*   0=   0
   1*   0=   0
   2*   0=   0
   3*   0=   0
   4*   0=   0
   5*   0=   0
   6*   0=   0
   7*   0=   0
   8*   0=   0
   0*   1=   0
   1*   1=   1
   2*   1=   2
   3*   1=   3
   4*   1=   4
   5*   1=   5
   6*   1=   6
   7*   1=   7
   8*   1=   8
   0*   2=   0
   1*   2=   2
   2*   2=   4
   3*   2=   6
   4*   2=   8
   5*   2=  10
   6*   2=  12
   7*   2=  14
   8*   2=  16
   0*   3=   0
   1*   3=   3
   2*   3=   6
   3*   3=   9
   4*   3=  12
   5*   3=  15
   6*   3=  18
   7*   3=  21
   8*   3=  24
   0*   4=   0
   1*   4=   4
   2*   4=   8
   3*   4=  12
   4*   4=  16
   5*   4=  20
   6*   4=  24
   7*   4=  28
   8*   4=  32
   0*   5=   0
   1*   5=   5
   2*   5=  10
   3*   5=  15
   4*   5=  20
   5*   5=  25
   6*   5=  30
   7*   5=  35
   8*   5=  40
   0*   6=   0
   1*   6=   6
   2*   6=  12
   3*   6=  18
   4*   6=  24
   5*   6=  30
   6*   6=  36
   7*   6=  42
   8*   6=  48
   0*   7=   0
   1*   7=   7
   2*   7=  14
   3*   7=  21
   4*   7=  28
   5*   7=  35
   6*   7=  42
   7*   7=  49
   8*   7=  56
   0*   8=   0
   1*   8=   8
   2*   8=  16
   3*   8=  24
   4*   8=  32
   5*   8=  40
   6*   8=  48
   7*   8=  56
   8*   8=  64
   0*   0=   0
   1*   0=   0
   2*   0=   0
   3*   0=   0
   4*   0=   0
   5*   0=   0
   6*   0=   0
   7*   0=   0
   8*   0=   0
   0*   1=   0
   1*   1=   1
   2*   1=   2
   3*   1=   3
   4*   1=   4
   5*   1=   5
   6*   1=   6
   7*   1=   7
   8*   1=   8
   0*   2=   0
   1*   2=   2
   2*   2=   4
   3*   2=   6
   4*   2=   8
   5*   2=  10
   6*   2=  12
   7*   2=  14
   8*   2=  16
   0*   3=   0
   1*   3=   3
   2*   3=   6
   3*   3=   9
   4*   3=  12
   5*   3=  15
   6*   3=  18
   7*   3=  21
   8*   3=  24
   0*   4=   0
   1*   4=   4
   2*   4=   8
   3*   4=  12
   4*   4=  16
   5*   4=  20
   6*   4=  24
   7*   4=  28
   8*   4=  32
   0*   5=   0
   1*   5=   5
   2*   5=  10
   3*   5=  15
   4*   5=  20
   5*   5=  25
   6*   5=  30
   7*   5=  35
   8*   5=  40
   0*   6=   0
   1*   6=   6
   2*   6=  12
   3*   6=  18
   4*   6=  24
   5*   6=  30
   6*   6=  36
   7*   6=  42
   8*   6=  48
   0*   7=   0
   1*   7=   7
   2*   7=  14
   3*   7=  21
   4*   7=  28
   5*   7=  35
   6*   7=  42
   7*   7=  49
   8*   7=  56
   0*   8=   0
   1*   8=   8
   2*   8=  16
   3*   8=  24
   4*   8=  32
   5*   8=  40
   6*   8=  48
   7*   8=  56
   8*   8=  64
   0*   0=   0
   1*   0=   0
   2*   0=   0
   3*   0=   0
   4*   0=   0
   5*   0=   0
   6*   0=   0
   7*   0=   0
   8*   0=   0
   0*   1=   0
   1*   1=   1
   2*   1=   2
   3*   1=   3
   4*   1=   4
   5*   1=   5
   6*   1=   6
   7*   1=   7
   8*   1=   8
   0*   2=   0
   1*   2=   2
   2*   2=   4
   3*   2=   6
   4*   2=   8
   5*   2=  10
   6*   2=  12
   7*   2=  14
   8*   2=  16
   0*   3=   0
   1*   3=   3
   2*   3=   6
   3*   3=   9
   4*   3=  12
   5*   3=  15
   6*   3=  18
   7*   3=  21
   8*   3=  24
   0*   4=   0
   1*   4=   4
   2*   4=   8
   3*   4=  12
   4*   4=  16
   5*   4=  20
   6*   4=  24
   7*   4=  28
   8*   4=  32
   0*   5=   0
   1*   5=   5
   2*   5=  10
   3*   5=  15
   4*   5=  20
   5*   5=  25
   6*   5=  30
   7*   5=  35
   8*   5=  40
   0*   6=   0
   1*   6=   6
   2*   6=  12
   3*   6=  18
   4*   6=  24
   5*   6=  30
   6*   6=  36
   7*   6=  42
   8*   6=  48
   0*   7=   0
   1*   7=   7
   2*   7=  14
   3*   7=  21
   4*   7=  28
   5*   7=  35
   6*   7=  42
   7*   7=  49
   8*   7=  56
   0*   8=   0
   1*   8=   8
   2*   8=  16
   3*   8=  24
   4*   8=  32
   5*   8=  40
   6*   8=  48
   7*   8=  56
   8*   8=  64
   0*   0=   0
   1*   0=   0
   2*   0=   0
   3*   0=   0
   4*   0=   0
   5*   0=   0
   6*   0=   0
   7*   0=   0
   8*   0=   0
   0*   1=   0
   1*   1=   1
   2*   1=   2
   3*   1=   3
   4*   1=   4
   5*   1=   5
   6*   1=   6
   7*   1=   7
   8*   1=   8
   0*   2=   0
   1*   2=   2
   2*   2=   4
   3*   2=   6
   4*   2=   8
   5*   2=  10
   6*   2=  12
   7*   2=  14
   8*   2=  16
   0*   3=   0
   1*   3=   3
   2*   3=   6
   3*   3=   9
   4*   3=  12
   5*   3=  15
   6*   3=  18
   7*   3=  21
   8*   3=  24
   0*   4=   0
   1*   4=   4
   2*   4=   8
   3*   4=  12
   4*   4=  16
   5*   4=  20
   6*   4=  24
   7*   4=  28
   8*   4=  32
   0*   5=   0
   1*   5=   5
   2*   5=  10
   3*   5=  15
   4*   5=  20
   5*   5=  25
   6*   5=  30
   7*   5=  35
   8*   5=  40
   0*   6=   0
   1*   6=   6
   2*   6=  12
   3*   6=  18
   4*   6=  24
   5*   6=  30
   6*   6=  36
   7*   6=  42
   8*   6=  48
   0*   7=   0
   1*   7=   7
   2*   7=  14
   3*   7=  21
   4*   7=  28
   5*   7=  35
   6*   7=  42
   7*   7=  49
   8*   7=  56
   0*   8=   0
   1*   8=   8
   2*   8=  16
   3*   8=  24
   4*   8=  32
   5*   8=  40
   6*   8=  48
   7*   8=  56


Traceback (most recent call last):
  File "<pyshell#121>", line 6, in <module>
    print '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    while(result < 0):
			  result = x*y
			  print '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)

			  
>>> results = 0
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    while(result < 0):
			  result = x*y
			  print '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)

			  
>>> result = 0
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    while(result < 0):
			  result = x*y
			  print '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)

			  
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
			int s = 0
			if(s < 9 ):
				result = x*y
			  print '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)
			  
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    int s = 0
		    	if(s < 9):
				result = x*yprint '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)
				
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if(s < 9):
		result = x*yprint '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)
		
  File "<pyshell#132>", line 6
    result = x*yprint '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)
    ^
IndentationError: expected an indented block
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if(s < 9):
		result = x*y print '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)
		
  File "<pyshell#133>", line 6
    result = x*y print '{0:4d}*{1:4d}={2:4d}'.format(x,y,result)
    ^
IndentationError: expected an indented block
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if(s < 9):
		        result = x*y
		    s++
		    
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if(s < 9):
		        result = x*y
		        s++
		        
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if(s < 9):
		        result = x*y
		        s = s + 1

		        
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if(s < 9):
		        result = x*y
		        s = s + 1
		        print result

		        
0
0
0
0
0
0
0
0
0
0
1
2
3
4
5
6
7
8
0
2
4
6
8
10
12
14
16
0
3
6
9
12
15
18
21
24
0
4
8
12
16
20
24
28
32
0
5
10
15
20
25
30
35
40
0
6
12
18
24
30
36
42
48
0
7
14
21
28
35
42
49
56
0
8
16
24
32
40
48
56
64
0
0
0
0
0
0
0
0
0
0
1
2
3
4
5
6
7
8
0
2
4
6
8
10
12
14
16
0
3
6
9
12
15
18
21
24
0
4
8
12
16
20
24
28
32
0
5
10
15
20
25
30
35
40
0
6
12
18
24
30
36
42
48
0
7
14
21
28
35
42
49
56
0
8
16
24
32
40
48
56
64
0
0
0
0
0
0
0
0
0
0
1
2
3
4
5
6
7
8
0
2
4
6
8
10
12
14
16
0
3
6
9
12
15
18
21
24
0
4
8
12
16
20
24
28
32
0
5
10
15
20
25
30
35
40
0
6
12
18
24
30
36
42
48
0
7
14
21
28
35
42
49
56
0
8
16
24
32
40
48
56
64
0
0
0
0
0
0
0
0
0
0
1
2
3
4
5
6
7
8
0
2
4
6
8
10
12
14
16
0
3
6
9
12
15
18
21
24
0
4
8
12
16
20
24
28
32
0
5
10
15
20
25
30
35
40
0
6
12
18
24
30
36
42
48
0
7
14
21
28
35
42
49
56
0
8
16
24
32
40
48
56
64
0
0
0
Traceback (most recent call last):
  File "<pyshell#142>", line 8, in <module>
    print result
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if(s <> 0 & x%y <> 0):
		        result = x*y
		        s = s + 1
		        print result

		        

Traceback (most recent call last):
  File "<pyshell#144>", line 5, in <module>
    if(s <> 0 & x%y <> 0):
ZeroDivisionError: integer division or modulo by zero
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			result = x*y
		        s = s + 1
		        print result

		       
1
2
3
4
5
6
7
8
2
4
6
8
10
12
14
16
3
6
9
12
15
18
21
24
4
8
12
16
20
24
28
32
5
10
15
20
25
30
35
40
6
12
18
24
30
36
42
48
7
14
21
28
35
42
49
56
8
16
24
32
40
48
56
64
1
2
3
4
5
6
7
8
2
4
6
8
10
12
14
16
3
6
9
12
15
18
21
24
4
8
12
16
20
24
28
32
5
10
15
20
25
30
35
40
6
12
18
24
30
36
42
48
7
14
21
28
35
42
49
56
8
16
24
32
40
48
56
64
1
2
3
4
5
6
7
8
2
4
6
8
10
12
14
16
3
6
9
12
15
18
21
24
4
8
12
16
20
24
28
32
5
10
15
20
25
30
35
40
6
12
18
24
30
36
42
48
7
14
21
28
35
42
49
56
8
16
24
32
40
48
56
64
1
2
3
4
5
6
7
8
2
4
6
8
10
12
14
16
3
6
9
12
15
18
21
24
4
8
12
16
20
24
28
32
5
10
15
20
25
30
35
40
6
12
18
24
30
36
42
48
7
14
21
28
35
42
49
56
8
16
24
32
40
48
56
64
1
2
3
4
5
6
7
8
2
4
6
8
10
12
14
16
3
6
9
12
15
18
21
24
4
8
12
16
20
24
28
32
5
10
15
20
25
30
35
40
6
12
18
24
30
36
42
48
7
14
21
28
35
42
49
56
8
16
24
32
40
48
56
64
1
2
3
4
5
6
7
8
2
4
6
8
10
12
14
16
3
6
9
12
15
18
21
24
4
8
12
16
20
24
28
32
5
10
15
20
25
30
35
40
6
12
18
24
30
36
42
48
7
14
21
28
35
42
49
56
8
16
24
32
40
48
56
64
1
2
3
4
5
6
7
8
2
4
6
8
10
12
14
16
3
6
9
12
15
18
21
24
4
8
12
16
20
24
28
32
5
10
15
20
25
30
35
40
6
12
18
24
30
36
42
48
7
14
21
28
35
42
49
56
8
16
24
32
40
48
56
64
1
2
3
4
5
6
7
8
2
4
6


Traceback (most recent call last):
  File "<pyshell#146>", line 8, in <module>
    print result
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			result = x*y
		        s = s + 1print result."{},{},{}"
		        
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			result = x*y
		        s = s + 1 print result."{},{},{}"
		        
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0 and result < 9):
			result = x*y
		        s = s + 1
		    print result

		    
6
6
6
6
6
6
6
6
6
6
1
2
3
4
5
6
7
8
8
2
4
6
8
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
Traceback (most recent call last):
  File "<pyshell#151>", line 8, in <module>
    print result
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0 and result < 9):
			result = x*y
		        s = s + 1
     print result
     
  File "<pyshell#152>", line 8
    print result
               ^
IndentationError: unindent does not match any outer indentation level
>>> result = 0
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0 and result < 9):
			result = x*y
		        s = s + 1
     print result
     
  File "<pyshell#154>", line 8
    print result
               ^
IndentationError: unindent does not match any outer indentation level
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0 and result < 9):
			result = x*y
		        s = s + 1
         print result
         
  File "<pyshell#155>", line 8
    print result
               ^
IndentationError: unindent does not match any outer indentation level
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0 and result < 9):
			result = x*y
		s = s + 1
                print result

                
0
8
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
>>> 
KeyboardInterrupt
>>> 
>>> 
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0 and result < 9):
			result = x*y
		s = s + 1
                print result

                
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    if(results > (9-1)):
				    result = x*y
print result
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    if(results > (9-1)):
				    result = x*y
print result
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    if(results > (9-1)):
				    result = x*y
     print result
     
  File "<pyshell#164>", line 8
    print result
               ^
IndentationError: unindent does not match any outer indentation level
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    if(results > (9-1)):
				    result = x*y
         print result
         
  File "<pyshell#165>", line 8
    print result
               ^
IndentationError: unindent does not match any outer indentation level
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    if(results > (9-1)):
				    result = x*y
         print result
         
  File "<pyshell#166>", line 8
    print result
               ^
IndentationError: unindent does not match any outer indentation level
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    if(results > (9-1)):
				    result = x*y

				    
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    if(result > (9-1)):
				    result = x*y

				    
>>> results
0
>>> result
1
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    if(result > (9-1)):
				    result = x*y
				    print result

				    
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    if(result < (9-1)):
				    result = x*y
				    print result

				    
1
2
3
4
5
6
7
8
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    if(result < (9)):
				    result = x*y
				    print result

				    
1
2
3
4
5
6
7
8
2
4
6
8
10
>>> result = 0
    for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    while(result < (9)):
				    result = x*y
				    print result
				    
>>> result
0
>>> result = 0
    for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    while(result < (9)):
				    result = x*y
				    print result
				    
>>> result = 0
    for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    s = 0
		    if( x <> 0 and y <> 0):
			    while(result < (9)):
				    result = x*y
				    print result
				    
>>> 
>>> result = 0
    for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    for s in range(0,9):
			    
>>> 
for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    for s in range(0,9):


			   /
			   
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    while(x*y < 9 (:print x
				   
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for x in range(0,9):
		for y in range(0,9):
		    while( (x*y) < 9 ): print x

		    
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
Traceback (most recent call last):
  File "<pyshell#194>", line 4, in <module>
    while( (x*y) < 9 ): print x
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> x = 0
    y = 0
    for i in range(0,9):
	for x in range(0,9):
		if((x*y) < 9):
			
>>> for i in range(0,9):
	for x in range(0,9):
		if((x*y) < 9):
			print(x*y)

			
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
>>> 

>>> for i in range(0,9):
	print i

	
0
1
2
3
4
5
6
7
8
>>> for i in range(0,9):
	print "{0:d4}".format(i)

	

Traceback (most recent call last):
  File "<pyshell#205>", line 2, in <module>
    print "{0:d4}".format(i)
ValueError: Invalid conversion specification
>>> for i in range(0,9):
	print '{0:d4}'.format(i)

	

Traceback (most recent call last):
  File "<pyshell#207>", line 2, in <module>
    print '{0:d4}'.format(i)
ValueError: Invalid conversion specification
>>> for i in range(0,9):
	print '{0:d1}'.format(i)

	

Traceback (most recent call last):
  File "<pyshell#209>", line 2, in <module>
    print '{0:d1}'.format(i)
ValueError: Invalid conversion specification
>>> for i in range(0,9):
	print '{0:d4}'.format(str(i))

	

Traceback (most recent call last):
  File "<pyshell#211>", line 2, in <module>
    print '{0:d4}'.format(str(i))
ValueError: Invalid conversion specification
>>> for i in range(0,9):
	print '{0:4d}'.format(i)

	
   0
   1
   2
   3
   4
   5
   6
   7
   8
>>> for i in range(0,9):
	print '{0:4d} * '.format(i)

	
   0 * 
   1 * 
   2 * 
   3 * 
   4 * 
   5 * 
   6 * 
   7 * 
   8 * 
>>> for i in range(0,9):
	for j in range(0,9):
		print '{0:4d} * {1:4d} '.format(i,j)

		
   0 *    0 
   0 *    1 
   0 *    2 
   0 *    3 
   0 *    4 
   0 *    5 
   0 *    6 
   0 *    7 
   0 *    8 
   1 *    0 
   1 *    1 
   1 *    2 
   1 *    3 
   1 *    4 
   1 *    5 
   1 *    6 
   1 *    7 
   1 *    8 
   2 *    0 
   2 *    1 
   2 *    2 
   2 *    3 
   2 *    4 
   2 *    5 
   2 *    6 
   2 *    7 
   2 *    8 
   3 *    0 
   3 *    1 
   3 *    2 
   3 *    3 
   3 *    4 
   3 *    5 
   3 *    6 
   3 *    7 
   3 *    8 
   4 *    0 
   4 *    1 
   4 *    2 
   4 *    3 
   4 *    4 
   4 *    5 
   4 *    6 
   4 *    7 
   4 *    8 
   5 *    0 
   5 *    1 
   5 *    2 
   5 *    3 
   5 *    4 
   5 *    5 
   5 *    6 
   5 *    7 
   5 *    8 
   6 *    0 
   6 *    1 
   6 *    2 
   6 *    3 
   6 *    4 
   6 *    5 
   6 *    6 
   6 *    7 
   6 *    8 
   7 *    0 
   7 *    1 
   7 *    2 
   7 *    3 
   7 *    4 
   7 *    5 
   7 *    6 
   7 *    7 
   7 *    8 
   8 *    0 
   8 *    1 
   8 *    2 
   8 *    3 
   8 *    4 
   8 *    5 
   8 *    6 
   8 *    7 
   8 *    8 
>>> for i in range(0,9):
	for j in range(0,9):
		print '{0:1d} * {1:1d} '.format(i,j)

		
0 * 0 
0 * 1 
0 * 2 
0 * 3 
0 * 4 
0 * 5 
0 * 6 
0 * 7 
0 * 8 
1 * 0 
1 * 1 
1 * 2 
1 * 3 
1 * 4 
1 * 5 
1 * 6 
1 * 7 
1 * 8 
2 * 0 
2 * 1 
2 * 2 
2 * 3 
2 * 4 
2 * 5 
2 * 6 
2 * 7 
2 * 8 
3 * 0 
3 * 1 
3 * 2 
3 * 3 
3 * 4 
3 * 5 
3 * 6 
3 * 7 
3 * 8 
4 * 0 
4 * 1 
4 * 2 
4 * 3 
4 * 4 
4 * 5 
4 * 6 
4 * 7 
4 * 8 
5 * 0 
5 * 1 
5 * 2 
5 * 3 
5 * 4 
5 * 5 
5 * 6 
5 * 7 
5 * 8 
6 * 0 
6 * 1 
6 * 2 
6 * 3 
6 * 4 
6 * 5 
6 * 6 
6 * 7 
6 * 8 
7 * 0 
7 * 1 
7 * 2 
7 * 3 
7 * 4 
7 * 5 
7 * 6 
7 * 7 
7 * 8 
8 * 0 
8 * 1 
8 * 2 
8 * 3 
8 * 4 
8 * 5 
8 * 6 
8 * 7 
8 * 8 
>>> for i in range(0,9):
	for j in range(0,9):
		print '{0:1d} * {1:1d} = {2:4d}'.format(i,j, (i * j))

		
0 * 0 =    0
0 * 1 =    0
0 * 2 =    0
0 * 3 =    0
0 * 4 =    0
0 * 5 =    0
0 * 6 =    0
0 * 7 =    0
0 * 8 =    0
1 * 0 =    0
1 * 1 =    1
1 * 2 =    2
1 * 3 =    3
1 * 4 =    4
1 * 5 =    5
1 * 6 =    6
1 * 7 =    7
1 * 8 =    8
2 * 0 =    0
2 * 1 =    2
2 * 2 =    4
2 * 3 =    6
2 * 4 =    8
2 * 5 =   10
2 * 6 =   12
2 * 7 =   14
2 * 8 =   16
3 * 0 =    0
3 * 1 =    3
3 * 2 =    6
3 * 3 =    9
3 * 4 =   12
3 * 5 =   15
3 * 6 =   18
3 * 7 =   21
3 * 8 =   24
4 * 0 =    0
4 * 1 =    4
4 * 2 =    8
4 * 3 =   12
4 * 4 =   16
4 * 5 =   20
4 * 6 =   24
4 * 7 =   28
4 * 8 =   32
5 * 0 =    0
5 * 1 =    5
5 * 2 =   10
5 * 3 =   15
5 * 4 =   20
5 * 5 =   25
5 * 6 =   30
5 * 7 =   35
5 * 8 =   40
6 * 0 =    0
6 * 1 =    6
6 * 2 =   12
6 * 3 =   18
6 * 4 =   24
6 * 5 =   30
6 * 6 =   36
6 * 7 =   42
6 * 8 =   48
7 * 0 =    0
7 * 1 =    7
7 * 2 =   14
7 * 3 =   21
7 * 4 =   28
7 * 5 =   35
7 * 6 =   42
7 * 7 =   49
7 * 8 =   56
8 * 0 =    0
8 * 1 =    8
8 * 2 =   16
8 * 3 =   24
8 * 4 =   32
8 * 5 =   40
8 * 6 =   48
8 * 7 =   56
8 * 8 =   64
>>> for i in range(0,9):
	for j in range(0,9):
		if((i * j) <= 9):
			print '{0:1d} * {1:1d} = {2:4d}'.format(i,j, (i * j))

			
0 * 0 =    0
0 * 1 =    0
0 * 2 =    0
0 * 3 =    0
0 * 4 =    0
0 * 5 =    0
0 * 6 =    0
0 * 7 =    0
0 * 8 =    0
1 * 0 =    0
1 * 1 =    1
1 * 2 =    2
1 * 3 =    3
1 * 4 =    4
1 * 5 =    5
1 * 6 =    6
1 * 7 =    7
1 * 8 =    8
2 * 0 =    0
2 * 1 =    2
2 * 2 =    4
2 * 3 =    6
2 * 4 =    8
3 * 0 =    0
3 * 1 =    3
3 * 2 =    6
3 * 3 =    9
4 * 0 =    0
4 * 1 =    4
4 * 2 =    8
5 * 0 =    0
5 * 1 =    5
6 * 0 =    0
6 * 1 =    6
7 * 0 =    0
7 * 1 =    7
8 * 0 =    0
8 * 1 =    8
>>> for i in range(0,9):
	for j in range(0,9):
		if((i * j) <= 9):
	print '{0:1d} * {1:1d} = {2:4d}'.format(i,j, (i * j))
	
  File "<pyshell#224>", line 4
    print '{0:1d} * {1:1d} = {2:4d}'.format(i,j, (i * j))
    ^
IndentationError: expected an indented block
>>> for i in range(0,9):
	for j in range(0,9):
		if((i * j) <= 9 print '{0:1d} * {1:1d} = {2:4d}'.format(i,j, (i * j))
		   
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for j in range(0,9):
		if((i * j) <= 9
		   print '{0:1d} * {1:1d} = {2:4d}'.format(i,j, (i * j))
		   
SyntaxError: invalid syntax
>>> for i in range(0,9):
	for j in range(0,9):
		if((i * j) <= 9 ):
		   print '{0:1d} * {1:1d} = {2:4d}'.format(i,j, (i * j))

		   
0 * 0 =    0
0 * 1 =    0
0 * 2 =    0
0 * 3 =    0
0 * 4 =    0
0 * 5 =    0
0 * 6 =    0
0 * 7 =    0
0 * 8 =    0
1 * 0 =    0
1 * 1 =    1
1 * 2 =    2
1 * 3 =    3
1 * 4 =    4
1 * 5 =    5
1 * 6 =    6
1 * 7 =    7
1 * 8 =    8
2 * 0 =    0
2 * 1 =    2
2 * 2 =    4
2 * 3 =    6
2 * 4 =    8
3 * 0 =    0
3 * 1 =    3
3 * 2 =    6
3 * 3 =    9
4 * 0 =    0
4 * 1 =    4
4 * 2 =    8
5 * 0 =    0
5 * 1 =    5
6 * 0 =    0
6 * 1 =    6
7 * 0 =    0
7 * 1 =    7
8 * 0 =    0
8 * 1 =    8
>>> for i in range(1,9):
	for j in range(1,9):
		print '{0:d2} {1:d2}'.format (i,j)

		

Traceback (most recent call last):
  File "<pyshell#232>", line 3, in <module>
    print '{0:d2} {1:d2}'.format (i,j)
ValueError: Invalid conversion specification
>>> for i in range(1,9):
	for j in range(1,9):
		print '{0:2d} {1:2d}'.format (i,j)

		
 1  1
 1  2
 1  3
 1  4
 1  5
 1  6
 1  7
 1  8
 2  1
 2  2
 2  3
 2  4
 2  5
 2  6
 2  7
 2  8
 3  1
 3  2
 3  3
 3  4
 3  5
 3  6
 3  7
 3  8
 4  1
 4  2
 4  3
 4  4
 4  5
 4  6
 4  7
 4  8
 5  1
 5  2
 5  3
 5  4
 5  5
 5  6
 5  7
 5  8
 6  1
 6  2
 6  3
 6  4
 6  5
 6  6
 6  7
 6  8
 7  1
 7  2
 7  3
 7  4
 7  5
 7  6
 7  7
 7  8
 8  1
 8  2
 8  3
 8  4
 8  5
 8  6
 8  7
 8  8
>>> for i in range(1,9):
		print '{0:2d} {1:2d}'.format (i)

		

Traceback (most recent call last):
  File "<pyshell#236>", line 2, in <module>
    print '{0:2d} {1:2d}'.format (i)
IndexError: tuple index out of range
>>> for i in range(1,9):
		print '{0:2d}'.format (i)

		
 1
 2
 3
 4
 5
 6
 7
 8
>>> for i in range(1,9):
		print '{0:2d}'.format (range[i])

		

Traceback (most recent call last):
  File "<pyshell#240>", line 2, in <module>
    print '{0:2d}'.format (range[i])
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> for i in range(1,9):
		print '{0:2d}'.format (i.getitem)

		

Traceback (most recent call last):
  File "<pyshell#242>", line 2, in <module>
    print '{0:2d}'.format (i.getitem)
AttributeError: 'int' object has no attribute 'getitem'
>>> for i in range(1,9):
		print '{0:2d}'.format (i)for i in range(1,9):
				print '{0:2d}'.format (range[i])for i in range(1,9):
						print '{0:2d}'.format (i.getitem)
						
SyntaxError: invalid syntax
>>> for i in range(1,10):
		print '{0:2d}'.format (range[i])

		

Traceback (most recent call last):
  File "<pyshell#245>", line 2, in <module>
    print '{0:2d}'.format (range[i])
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> for i in range(1,10):print '{0:2d}'.format (range[i])


Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    for i in range(1,10):print '{0:2d}'.format (range[i])
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> for i in range(1,10):
	print '{0:2d}'.format(i)

	
 1
 2
 3
 4
 5
 6
 7
 8
 9
>>> for i in range(0,10):
	print '{0:2d}'.format(i)

	
 0
 1
 2
 3
 4
 5
 6
 7
 8
 9
>>> for i in range(0,10):
	for j in range(0,10):
		print '{0:2d} * {1:2d} = {2:2d)'.format(i,j,(i*j))

		

Traceback (most recent call last):
  File "<pyshell#254>", line 3, in <module>
    print '{0:2d} * {1:2d} = {2:2d)'.format(i,j,(i*j))
ValueError: unmatched '{' in format
>>> for i in range(0,10):
	for j in range(0,10):
		print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))

		
 0 *  0 =  0
 0 *  1 =  0
 0 *  2 =  0
 0 *  3 =  0
 0 *  4 =  0
 0 *  5 =  0
 0 *  6 =  0
 0 *  7 =  0
 0 *  8 =  0
 0 *  9 =  0
 1 *  0 =  0
 1 *  1 =  1
 1 *  2 =  2
 1 *  3 =  3
 1 *  4 =  4
 1 *  5 =  5
 1 *  6 =  6
 1 *  7 =  7
 1 *  8 =  8
 1 *  9 =  9
 2 *  0 =  0
 2 *  1 =  2
 2 *  2 =  4
 2 *  3 =  6
 2 *  4 =  8
 2 *  5 = 10
 2 *  6 = 12
 2 *  7 = 14
 2 *  8 = 16
 2 *  9 = 18
 3 *  0 =  0
 3 *  1 =  3
 3 *  2 =  6
 3 *  3 =  9
 3 *  4 = 12
 3 *  5 = 15
 3 *  6 = 18
 3 *  7 = 21
 3 *  8 = 24
 3 *  9 = 27
 4 *  0 =  0
 4 *  1 =  4
 4 *  2 =  8
 4 *  3 = 12
 4 *  4 = 16
 4 *  5 = 20
 4 *  6 = 24
 4 *  7 = 28
 4 *  8 = 32
 4 *  9 = 36
 5 *  0 =  0
 5 *  1 =  5
 5 *  2 = 10
 5 *  3 = 15
 5 *  4 = 20
 5 *  5 = 25
 5 *  6 = 30
 5 *  7 = 35
 5 *  8 = 40
 5 *  9 = 45
 6 *  0 =  0
 6 *  1 =  6
 6 *  2 = 12
 6 *  3 = 18
 6 *  4 = 24
 6 *  5 = 30
 6 *  6 = 36
 6 *  7 = 42
 6 *  8 = 48
 6 *  9 = 54
 7 *  0 =  0
 7 *  1 =  7
 7 *  2 = 14
 7 *  3 = 21
 7 *  4 = 28
 7 *  5 = 35
 7 *  6 = 42
 7 *  7 = 49
 7 *  8 = 56
 7 *  9 = 63
 8 *  0 =  0
 8 *  1 =  8
 8 *  2 = 16
 8 *  3 = 24
 8 *  4 = 32
 8 *  5 = 40
 8 *  6 = 48
 8 *  7 = 56
 8 *  8 = 64
 8 *  9 = 72
 9 *  0 =  0
 9 *  1 =  9
 9 *  2 = 18
 9 *  3 = 27
 9 *  4 = 36
 9 *  5 = 45
 9 *  6 = 54
 9 *  7 = 63
 9 *  8 = 72
 9 *  9 = 81
>>> for i in range(0,10):
	for j in range(0,10):
		if(
		print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
		
SyntaxError: invalid syntax
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10):
			print '{0:2d}*{1:2d} = {2:2d}'.format(i,j,(i*j))

			
 0* 0 =  0
 0* 1 =  0
 0* 2 =  0
 0* 3 =  0
 0* 4 =  0
 0* 5 =  0
 0* 6 =  0
 0* 7 =  0
 0* 8 =  0
 0* 9 =  0
 1* 0 =  0
 1* 1 =  1
 1* 2 =  2
 1* 3 =  3
 1* 4 =  4
 1* 5 =  5
 1* 6 =  6
 1* 7 =  7
 1* 8 =  8
 1* 9 =  9
 2* 0 =  0
 2* 1 =  2
 2* 2 =  4
 2* 3 =  6
 2* 4 =  8
 3* 0 =  0
 3* 1 =  3
 3* 2 =  6
 3* 3 =  9
 4* 0 =  0
 4* 1 =  4
 4* 2 =  8
 5* 0 =  0
 5* 1 =  5
 6* 0 =  0
 6* 1 =  6
 7* 0 =  0
 7* 1 =  7
 8* 0 =  0
 8* 1 =  8
 9* 0 =  0
 9* 1 =  9
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10):
			if(i> 1):
				print '{0:2d}*{1:2d} = {2:2d}'.format(i,j,(i*j))

				
 2* 0 =  0
 2* 1 =  2
 2* 2 =  4
 2* 3 =  6
 2* 4 =  8
 3* 0 =  0
 3* 1 =  3
 3* 2 =  6
 3* 3 =  9
 4* 0 =  0
 4* 1 =  4
 4* 2 =  8
 5* 0 =  0
 5* 1 =  5
 6* 0 =  0
 6* 1 =  6
 7* 0 =  0
 7* 1 =  7
 8* 0 =  0
 8* 1 =  8
 9* 0 =  0
 9* 1 =  9
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10):
			if( (i> 1) and (i * j)
				for i in range(0,10):
					for j in range(0,10):
						if((i*j) < 10):
							if(i> 1):
								print '{0:2d}*{1:2d} = {2:2d}'.format(i,j,(i*j))
			    
SyntaxError: invalid syntax
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10):
			if( (i> 1) and (i * j)
				for i in range(0,10):
					for j in range(0,10):
						if((i*j) < 10):
						     print '{0:2d}*{1:2d} = {2:2d}'.format(i,j,(i*j))
			    
SyntaxError: invalid syntax
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10):
			if( (i> 1) and (i * j)
				for i in range(0,10):print '{0:2d}*{1:2d} = {2:2d}'.format(i,j,(i*j))
			    
SyntaxError: invalid syntax
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10):
			if( (i> 1) and (i * j)
				for i in range(0,10):print '{0:2d}*{1:2d} = {2:2d}'.format(i,j,(i*j))
			    
SyntaxError: invalid syntax
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10 and (i> 1)):for i in range(0,10):
			
SyntaxError: invalid syntax
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10 and (i> 1)):for i in range(0,10):
			
SyntaxError: invalid syntax
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10 and (i> 1)):
			print i * j

			
0
2
4
6
8
0
3
6
9
0
4
8
0
5
0
6
0
7
0
8
0
9
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10 and (i> 1)):
			print '{i:d2} * {j:d2}'.format(i,j)

			

Traceback (most recent call last):
  File "<pyshell#272>", line 4, in <module>
    print '{i:d2} * {j:d2}'.format(i,j)
KeyError: 'i'
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10 and (i> 1)):
			print '{0:d2} * {1:d2}'.format(i,j)

			

Traceback (most recent call last):
  File "<pyshell#274>", line 4, in <module>
    print '{0:d2} * {1:d2}'.format(i,j)
ValueError: Invalid conversion specification
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10 and (i> 1)):
			print '{0:d2} * {1:d2}'.format(i,j)

			

Traceback (most recent call last):
  File "<pyshell#276>", line 4, in <module>
    print '{0:d2} * {1:d2}'.format(i,j)
ValueError: Invalid conversion specification
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10 and (i> 1)):
			print i

			
2
2
2
2
2
3
3
3
3
4
4
4
5
5
6
6
7
7
8
8
9
9
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10 and (i> 1)):
			print '{0:2d}'.format(i)

			
 2
 2
 2
 2
 2
 3
 3
 3
 3
 4
 4
 4
 5
 5
 6
 6
 7
 7
 8
 8
 9
 9
>>> for i in range(0,10):
	for j in range(0,10):
		if((i*j) < 10 and (i> 1)):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))

			
 2 *  0 =  0
 2 *  1 =  2
 2 *  2 =  4
 2 *  3 =  6
 2 *  4 =  8
 3 *  0 =  0
 3 *  1 =  3
 3 *  2 =  6
 3 *  3 =  9
 4 *  0 =  0
 4 *  1 =  4
 4 *  2 =  8
 5 *  0 =  0
 5 *  1 =  5
 6 *  0 =  0
 6 *  1 =  6
 7 *  0 =  0
 7 *  1 =  7
 8 *  0 =  0
 8 *  1 =  8
 9 *  0 =  0
 9 *  1 =  9
>>> test_number = 9

for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1)):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			
>>> 
>>> 

for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1)):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))

			
 2 *  0 =  0
 2 *  1 =  2
 2 *  2 =  4
 2 *  3 =  6
 2 *  4 =  8
 3 *  0 =  0
 3 *  1 =  3
 3 *  2 =  6
 3 *  3 =  9
 4 *  0 =  0
 4 *  1 =  4
 4 *  2 =  8
 5 *  0 =  0
 5 *  1 =  5
 6 *  0 =  0
 6 *  1 =  6
 7 *  0 =  0
 7 *  1 =  7
 8 *  0 =  0
 8 *  1 =  8
 9 *  0 =  0
 9 *  1 =  9
>>> test_number = 9

for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1)):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			
>>> 
>>> test_number = 9
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1)):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))

 2 *  0 =  0
 2 *  1 =  2
 2 *  2 =  4
 2 *  3 =  6
 2 *  4 =  8
 3 *  0 =  0
 3 *  1 =  3
 3 *  2 =  6
 3 *  3 =  9
 4 *  0 =  0
 4 *  1 =  4
 4 *  2 =  8
 5 *  0 =  0
 5 *  1 =  5
 6 *  0 =  0
 6 *  1 =  6
 7 *  0 =  0
 7 *  1 =  7
 8 *  0 =  0
 8 *  1 =  8
 9 *  0 =  0
 9 *  1 =  9
>>> multiple_count = 0
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			multiple_count = multiple_count + 1
			
KeyboardInterrupt
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			multiple_count = multiple_count + 1

		
 2 *  0 =  0
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			if( (i*j) == test_number):
				multiple_count = multiple_count + 1

				
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			if( (i*j) == test_number):
				multiple_count = multiple_count + 1

				
>>> multiple_count = 0
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			if( (i*j) == test_number):
				multiple_count = multiple_count + 1

				
 2 *  0 =  0
 2 *  1 =  2
 2 *  2 =  4
 2 *  3 =  6
 2 *  4 =  8
 3 *  0 =  0
 3 *  1 =  3
 3 *  2 =  6
 3 *  3 =  9
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			if( (i*j) == test_number):
				multiple_count = multiple_count + 1

				
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			if( (i*j) == test_number):
				multiple_count = multiple_count + 1

				
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			if( (i*j) == test_number):
				multiple_count = multiple_count + 1
				if(i == (i*j)) then
				
SyntaxError: invalid syntax
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			if( (i*j) == test_number):
				multiple_count = multiple_count + 1
				if(i == (i*j)):
					1
				else
				
SyntaxError: invalid syntax
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			if( (i*j) == test_number):
				multiple_count = multiple_count + 1
				if(i == (i*j)):
					1
				else:
					0

					
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			if( (i*j) == test_number):
				multiple_count = multiple_count + 1
				if(i == (i*j)):
					print 1
				else:
					print 0

					
>>> for i in range(0,test_number+1):
	for j in range(0,test_number+1):
		if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
			print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
			if( (i*j) == test_number):
				multiple_count = multiple_count + 1
				if(i == (i*j)):
					print '1'
				else:
					print '0'

					
>>> def isPrime(test_number):
	for i in range(0,test_number+1):
		for j in range(0,test_number+1):
			if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
				print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
				if( (i*j) == test_number):
					multiple_count = multiple_count + 1
					if(i == (i*j)):
						print '1'
					else:
						print '0'

						
>>> isPrime(3)

Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    isPrime(3)
  File "<pyshell#324>", line 4, in isPrime
    if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
UnboundLocalError: local variable 'multiple_count' referenced before assignment
>>> def isPrime(test_number):
	multiple_count = 0
	for i in range(0,test_number+1):
		for j in range(0,test_number+1):
			if((i*j) < test_number+1 and (i> 1) and multiple_count < 1):
				print '{0:2d} * {1:2d} = {2:2d}'.format(i,j,(i*j))
				if( (i*j) == test_number):
					multiple_count = multiple_count + 1
					if(i == (i*j)):
						print '1'
					else:
						print '0'

						
>>> isPrime(3)
 2 *  0 =  0
 2 *  1 =  2
 3 *  0 =  0
 3 *  1 =  3
1
>>> isPrime(9)
 2 *  0 =  0
 2 *  1 =  2
 2 *  2 =  4
 2 *  3 =  6
 2 *  4 =  8
 3 *  0 =  0
 3 *  1 =  3
 3 *  2 =  6
 3 *  3 =  9
0
>>> isPrime(99)
 2 *  0 =  0
 2 *  1 =  2
 2 *  2 =  4
 2 *  3 =  6
 2 *  4 =  8
 2 *  5 = 10
 2 *  6 = 12
 2 *  7 = 14
 2 *  8 = 16
 2 *  9 = 18
 2 * 10 = 20
 2 * 11 = 22
 2 * 12 = 24
 2 * 13 = 26
 2 * 14 = 28
 2 * 15 = 30
 2 * 16 = 32
 2 * 17 = 34
 2 * 18 = 36
 2 * 19 = 38
 2 * 20 = 40
 2 * 21 = 42
 2 * 22 = 44
 2 * 23 = 46
 2 * 24 = 48
 2 * 25 = 50
 2 * 26 = 52
 2 * 27 = 54
 2 * 28 = 56
 2 * 29 = 58
 2 * 30 = 60
 2 * 31 = 62
 2 * 32 = 64
 2 * 33 = 66
 2 * 34 = 68
 2 * 35 = 70
 2 * 36 = 72
 2 * 37 = 74
 2 * 38 = 76
 2 * 39 = 78
 2 * 40 = 80
 2 * 41 = 82
 2 * 42 = 84
 2 * 43 = 86
 2 * 44 = 88
 2 * 45 = 90
 2 * 46 = 92
 2 * 47 = 94
 2 * 48 = 96
 2 * 49 = 98
 3 *  0 =  0
 3 *  1 =  3
 3 *  2 =  6
 3 *  3 =  9
 3 *  4 = 12
 3 *  5 = 15
 3 *  6 = 18
 3 *  7 = 21
 3 *  8 = 24
 3 *  9 = 27
 3 * 10 = 30
 3 * 11 = 33
 3 * 12 = 36
 3 * 13 = 39
 3 * 14 = 42
 3 * 15 = 45
 3 * 16 = 48
 3 * 17 = 51
 3 * 18 = 54
 3 * 19 = 57
 3 * 20 = 60
 3 * 21 = 63
 3 * 22 = 66
 3 * 23 = 69
 3 * 24 = 72
 3 * 25 = 75
 3 * 26 = 78
 3 * 27 = 81
 3 * 28 = 84
 3 * 29 = 87
 3 * 30 = 90
 3 * 31 = 93
 3 * 32 = 96
 3 * 33 = 99
0
>>> isPrime(10)
 2 *  0 =  0
 2 *  1 =  2
 2 *  2 =  4
 2 *  3 =  6
 2 *  4 =  8
 2 *  5 = 10
0
>>> 
