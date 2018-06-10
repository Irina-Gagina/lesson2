answers_new={"Привет": "И тебе привет!", "как дела?": "Лучше всех", "пока": "Увидимся"}

def get_answer(question,answers):
	while question!="Пока!":
		result=str(answers.get(question))
		if result=="None":
			result="Ответ на вопрос не найден"
		print(result)
		question=str(input('Введите вопрос '))
	return	result

def ask_user():
	while True:
		answer_user1=str(input('Как дела,солнышко? '))
		if "?" in answer_user1:			
				get_answer(answer_user1,answers_new)
		elif answer_user1=="Хорошо":
			break
ask_user()