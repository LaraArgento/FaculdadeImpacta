



delete_sql = """
DELETE FROM Pessoa WHERE id = 1
"""
cursor.execute(delete_sql)
connection.commit()


select_sql = """
SELECT ID, NOME, EMAIL FROM PESSOA
"""
cursor.execute(select_sql)
result_set = cursor.fetchone()
print(result_set)
print(f'id: {result_set[0]}')
print(f'nome: {result_set[1]}')
print(f'email: {result_set[2]}')

connection.close()
