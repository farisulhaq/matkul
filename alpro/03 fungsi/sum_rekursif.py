# def jum(a):
# 	if len(a) == 1:
# 		hasil = a[0]
# 	else:
# 		hasil = a[0] + jum(a[1:])
#         # 2 + 3 
# 	return hasil	
# b = [2,3,4,5,6,1]
# print(jum(b))

def jum(a):
	if len(a) == 1:
		return a[0]
	else:
		if a[0] < jum(a[1:]):
			a[0] = jum(a[1:])
		return a[0]
	
b = [5,3,2,1,4]
print(jum(b))

# a = [1,2,3,4,3,2,5,6,8,9,3,4,3]
# b = 3
# for i in range(len(a)):
# 	if a[i] == b:
# 		print(b, i)