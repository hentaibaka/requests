import requests as r

BACKEND = 'http://127.0.0.1:8000/api'

courses = r.get(BACKEND + '/courses')
if courses.status_code == 200:
    courses = courses.json()
print(courses)