import sqlite3

conexao = sqlite3.connect('testeb.db')
cursor = conexao.cursor()  #é o objeto que serve de mensageiro do sqlite e python

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancaria(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
titular TEXT NOT NULL,
saldo FLOAT NOT NULL,
cpf TEXT NOT NULL UNIQUE)""")


# cursor.execute("""INSERT INTO contas_bancaria
# (titular, saldo, cpf) VALUES
# ('Senoura', -8000, '3129381290309')""")

cursor.execute("""SELECT titular, saldo FROM contas_bancaria WHERE id = 1
""")
# cursor.execute("""UPDATE contas_bancaria SET saldo = -10000 WHERE id = 1""")
# cursor.execute('DELETE FROM contas_bancaria WHERE id = 3')
conta = cursor.fetchall()  #ele pega o resultado da query e traz pra conta
for conta in conta:
    id, titular = conta
    print(f"""
id: {id}
titular: {titular}
""")
conexao.commit()  #commit é o comando que salva as alterações no banco de dados


# cursor.execute("""SELECT titular, saldo FROM contas_bancaria WHERE id = 1
# """)
# conta = cursor.fetchall()  #ele pega o resultado da query e traz pra conta
# for conta in conta:
#     id, titular = conta
#     print(f"""
# id: {id}
# titular: {titular}
# """)
# conexao.commit()  #commit é o comando que salva as alterações no banco de dados