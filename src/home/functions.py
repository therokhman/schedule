import psycopg2

def getData():
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            host="127.0.0.1",
                            password="admin",
                            port="5432")

    cur = conn.cursor()

    cur.execute("SELECT * FROM public.schedule_10702417")
    data = cur.fetchall()
    for row in data:
        print(row[0], " ", row[1])
    conn.commit()
    conn.close()
