import sys


divisor = str(sys.argv[1])

print "divisor > " + divisor
dividend = str(sys.argv[2])
print "dividend > " + dividend
projection = str()

output = str(int(dividend)/int(divisor))

temp_dividend  = int(dividend)   - ( int(output) * int(divisor) ) 

if(temp_dividend < int(dividend)):
    temp_dividend = str(temp_dividend) + str(0)


print " output > " + output
#print " remainder > " + remainder 




#while(remainder <>  0):

 #   break

#     if( remainder  < int(divisor) ):

#         temp_dividend =  remainder + int(dividend[1])


#         print temp_dividend

#         remainder = int(temp_dividend)/int(divisor)

#         print str(output) + str(remainder)

#         print int(str(output) + str(remainder)) * int(divisor)

#         print int(temp_dividend)  - ( int(str(output) + str(remainder)) * int(divisor) )

#     if( (int(temp_dividend)  - ( int(str(output) + str(remainder)) * int(divisor) ) < int(divisor) )):

#        print str(int(temp_dividend)  - ( int(str(output) + str(remainder)) * int(divisor) )) + dividend[2]

#        temp_dividend = int(str(int(temp_dividend)  - ( int(str(output) + str(remainder)) * int(divisor) )) + dividend[2])/int(divisor)


#        remainder = int(temp_dividend)/int(divisor)

#        print remainder

        

        

    
        
    

##     div = int(dividend[i])/int(divisor)
##
##     remainder =  int(dividend[i])%int(divisor)
##     projection = str(projection) + str(div)  
##     print " div > " + str(div)
##     print " remainder > " + str(remainder)
##     print " projection > " + str(projection)
##     print  (int(projection) * int(divisor))

     


    
