import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS contas_bancarias (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL,
    saldo FLOAT NOT NULL,
    cpf TEXT NOT NULL UNIQUE
    )''')

# cursor.execute('''INSERT INTO contas_bancarias
#  (titular, saldo, cpf) VALUES
#  ('Ravel', 800, '13244678900')''') 


cursor.execute("""SELECT * FROM contas_bancarias""")
contas = cursor.fetchall()


for conta in contas:
   id, titular, saldo, cpf = conta

   print(f"""id {id}
titular: {titular}
saldo: {saldo}
""")
conexao.commit()