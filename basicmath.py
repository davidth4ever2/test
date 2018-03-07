def isPrime(test_number):
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
