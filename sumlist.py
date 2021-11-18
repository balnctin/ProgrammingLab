#input 1,2,3,4,5
#output 15
#using sum()
#the_list = [1,2,3,4,5]
#total = sum(the_list)
#print ('Sum  of elements in the list:', total)

#sum using range

the_list = [1,2,3,4,5]
sum = 0

for i in range (0, len(the_list)):
  sum = sum + the_list[i]

print (" Sum of elements in the list:", sum)