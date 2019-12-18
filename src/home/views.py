from django.shortcuts import render
import psycopg2

def getData(day):
    conn = psycopg2.connect(database="schedule_10702417",
                            user="postgres",
                            host="127.0.0.1",
                            password="admin",
                            port="5432")

    cur = conn.cursor()
    result = {}
    cur.execute("SELECT * FROM public."+day)
    data = cur.fetchall()
    for row in data:
        result['p'+str(row[0])] = row[1]
    conn.commit()
    conn.close()
    return result


def get_days():
    days = {'Понедельник': {},
            'Вторник': {},
            'Среда': {},
            'Четверг': {},
            'Пятница': {},
            'Суббота': {}
            }
    for key in dict.keys(days):
        days[key] = getData(key)
    return days


def index(request):
    return render(request, "index.html")


# def result(request):
#     return render(request, "result.html")


def result(request):
    return render(request, "result.html", {"days": get_days().items()})
