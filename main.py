import requests as r

BACKEND = 'http://127.0.0.1:8000/api'

courses = r.get(BACKEND + '/courses')
if courses.status_code == 200:
    courses = courses.json()

print(courses)

questions = r.get(BACKEND + '/questions')
if questions.status_code == 200:
    questions = questions.json()

print(questions)

answers_id = []
for question in questions:
    print(question['text'])
    answer = {'question': question['id'],
              'text': input("Ответ: "),
              }
    answer = r.post(BACKEND + '/answers/', json=answer) # /answers/ слеш в конце обязательно
    if answer.status_code == 201:
        answer = answer.json()
        print(answer)
        answers_id.append(answer['id'])
    
data = {
    'course': courses[0]['id'], # тут надо вставить айди курса который выбрал пользователь
    'answers': answers_id
    }    
data = r.post(BACKEND + '/data/', json=data)
if data.status_code == 201:
    print(data.json())
