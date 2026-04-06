lis = [1,[13,14],2,3,4,[5,6,7,[8,9,[12,[1212,1212]]],10],11,12]

def single(lis):
	singleList = []
	# Iterate with outer list
	for element in lis:
		if type(element) is list:
			# Check if type is list than iterate through the sublist
			for item in element:
				singleList.append(item)
		else:
			singleList.append(element)
	return singleList

print('List', lis)
print('Flat List', single(lis))



