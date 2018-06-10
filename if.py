answer=int(input("Введите свой возраст "))

if answer<7:
	print ("Вы учитесь в детском саду")
elif 7<=answer<16:
	 print ("Вы учитесь в школе")
elif 16<answer<23:
	print ("Вы учитесь в институте")
elif answer>=23:
	print ("Вы работаете на работе")