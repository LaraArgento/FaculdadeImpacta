import sqlite3

connection = sqlite3.connect("db.db")
create_sql = """
CREATE TABLE IF NOT EXISTS Pessoa (
    id INTEGER PRIMARY KEY autoincrement,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
"""
cursor = connection.cursor()
cursor.execute(create_sql)
connection.commit()

delete_sql = """
DELETE FROM Pessoa
"""
#cursor.execute(delete_sql)
#connection.commit()

insert_sql = """
INSERT INTO Pessoa(nome, email)
VALUES 
('Nome Completo', 'nome.completo@email.com'),
('Nome Dois', 'nome.dois@email.com'),
('Nome Tres', 'nome.tres@email.com')
"""
cursor.execute(insert_sql)
connection.commit()

select_sql = """
SELECT ID, NOME, EMAIL
FROM PESSOA
"""
cursor.execute(select_sql)
tem_registros = True
while tem_registros:
    print('Proxima pagina')
    linhas = cursor.fetchmany(1)
    if len(linhas) == 0:
        tem_registros = False
    for linha in linhas:
        print('===================')
        print('imprimindo registro')
        print('===================')
        print(f'id: {int(linha[0])}')
        print(f'nome: {linha[1]}')
        print(f'email: {linha[2]}')

print('all good')
cursor.close()
connection.close()