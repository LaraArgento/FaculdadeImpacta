import requests as r

aluno = {}
aluno['id'] = 1
aluno['nome'] = 'Lara Argento'

print('Lendo database completo')
ret = r.get('http://localhost:5002')
print(ret.json())

r.post('http://localhost:5002/alunos', json=aluno)

print('Lendo database completo')
ret = r.get('http://localhost:5002')
print(ret.json())

print('Lendo somente o aluno 1')
ret = r.get('http://localhost:5002/alunos/1')
print(ret.text)

print('Lendo somente o aluno 99 ##erro##')
ret = r.get('http://localhost:5002/alunos/99')
print(ret.status_code)
print(ret.text)















'''import requests as r

student = {}
student['id'] = 2
student['name'] = 'Lara'

print('Database read sucessfully.')
ret = r.get('http://localhost:5002')
print(ret.json())

r.post('http://localhost:5002/students', json=student)

print('Database read sucessfully.')
ret = r.get('http://localhost:5002')
print(ret.json())

print('Reading only student 1')
ret = r.get('http://localhost:5002/students/1')
print(ret.text)

print('Reading only student 99 (Error)')
ret = r.get('http://localhost:5002/alunos/99')
print(ret.status_code)
print(ret.text)'''