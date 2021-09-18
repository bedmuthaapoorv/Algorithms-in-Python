# Selection Sort

'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
Worst-case time Complexity : O(n^2)

sample execution:

Enter elements of array to be sorted separated by commas: 
1,5,2,6,3
sorted array is:['1', '2', '3', '5', '6']

'''

#taking input array from user
print("Enter elements of array to be sorted separated by commas: ")
Array = input().split(',')

i=0
j=1
while(i<len(Array)):
	minElem=i
	while(j<len(Array)):
		if(int(Array[j])<int(Array[minElem])):
			minElem=j
		j=j+1
	temp=Array[i]
	Array[i]=Array[minElem]
	Array[minElem]=temp
	i=i+1
	j=i+1
print('sorted array is:'+str(Array))
