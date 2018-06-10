def func_if(str1,str2):
	str1=str(str1)
	str2=str(str2)
	if str(str1)==str(str2):
		print("1")
		return("1")
	elif len(str1)>len(str2):
		print("2")
		return("2")
	elif str2=="learn":
		print("3")
		return("3")
	else:
		print("4")
		return("4")

func_if("Ник","learn1")