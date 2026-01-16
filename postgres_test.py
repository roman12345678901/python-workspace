import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "test_db",
    user = "postgres",
    password = "admin"
)

cur = conn.cursor()

cur.execute("""
    INSERT INTO users (name, email) VALUES (%s, %s)
""", ("Roma", "yatsykovich@gmail.com"))

conn.commit()

cur.execute("SELECT id, name, email, created_at FROM users")
rows = cur.fetchall()

print("Users table content:")
for row in rows:
    print(row)

cur.close()
conn.close()