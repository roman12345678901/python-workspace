import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "test_db",
    user = "postgres",
    password = "admin"
)

cur = conn.cursor()

cur.execute ("""
    INSERT INTO users (id, name, email) VALUES (%s, %s, %s)""", (1, "Roma", "yatsykovich@gmail.com"))

conn.commit()

# select 
cur.execute("SELECT * FROM users;")
rows = cur.fetchall()

print("Users table content:")
for row in rows:
    print(row)

cur.close()
conn.close()