def ask_user():
	while True:
		try:
			answer_user1=input('Как дела,солнышко? ')
			if answer_user1=="Хорошо":
				break
		except (KeyboardInterrupt):
			print("Приятно было пообщаться")
			break
ask_user()