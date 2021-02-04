start = True
while start:
	x = int(input("Masukkan Angka => "))
	if x > 1 : 
		i = 2
		while i < x :
			if (x % i) == 0 :
				print(x, "BUKAN PRIMA")
				break
			i += 1
		else : 
			print(x, "PRIMA")
			break
	else:
		print (x, "BUKAN PRIMA")
		break
