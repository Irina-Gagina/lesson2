answers_new={"Привет": "И тебе привет!", "как дела?": "Лучше всех", "пока": "Увидимся"}

def get_answer(question,answers):
	while question!="Пока!":
		try:
			result=str(answers[question])
			print(result)			
		except KeyError:
			result="Ответ на вопрос не найден."
			print(result)
		question=str(input('Введите вопрос: '))		
	return	result

def ask_user():
	while True:
		try:
			answer_user1=str(input('Как дела,солнышко? '))
			if "?" in answer_user1:			
				get_answer(answer_user1,answers_new)
			elif answer_user1=="Хорошо":
				break
		except (KeyboardInterrupt):
			print("Приятно было пообщаться")
			break


if __name__ == "__main__":
	ask_user()