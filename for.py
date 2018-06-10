mark_class=[{'school_class': '4a', 'scores': [5,5,5,5,5]},{'school_class': '4b', 'scores': [4,4,4,4,4]},{'school_class': '4c', 'scores': [3,3,3,3,3]}]
mark1=0
sum_mark=0
for clas in mark_class:
	print(clas["school_class"])
	m=clas['scores']
	print(m)
	for mark in m:
		mark1=mark1+mark
		sum_mark=sum_mark+1
print("Суммарная оценка по классам равна ",mark1)
print("Количество оценок в классам равна",sum_mark)
sr_mark=int(mark1/sum_mark)
print("Средняя оценка по всем классам равна",sr_mark)

