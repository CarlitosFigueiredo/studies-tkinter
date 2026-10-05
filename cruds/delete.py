import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgresDB',
    user = 'admin',
    password = 'admin123',
)

cursor = conn.cursor()

# excluir dados
cursor.execute(""" 
DELETE FROM public."AGENDA"
    WHERE id = 1;
""")

conn.commit()

# ler dados atualizados

cursor.execute("""
SELECT id, nome, telefone FROM public."AGENDA";
""")

rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}")


# fechar a conexão
cursor.close()
conn.close()