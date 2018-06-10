def find_person(name):
	string='пусто'
	name_list=["Вася", "Маша", "Петя", "Саша", "Даша", "Валера"]
	if name in name_list:
		while string=='пусто':
			for n in name_list:
				print("Элемент списка",n)
				index_n=name_list.index(n)
				print("Индекс элемента списка",index_n)
				if name_list.pop(index_n)==str(name):
					string=str(name)
					print("Имя"+str(name)+" нашлось в списке")
					print("Оставшиеся имена",name_list)
	else:
		print(str(name), " отсутствует в списке")
find_person(1)
