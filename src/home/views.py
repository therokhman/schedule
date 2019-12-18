from django.shortcuts import render
import psycopg2

def getData(day):
    # conn = psycopg2.connect(database="schedule_10702417",
    #                         user="postgres",
    #                         host="127.0.0.1",
    #                         password="admin",
    #                         port="5432")
    conn = psycopg2.connect(database="schedule_10702417",
                            user="ilwtvyeswnvrxf",
                            host="ec2-46-137-113-157.eu-west-1.compute.amazonaws.com",
                            password="c189da7af2cac8e3977eabc903d8e860adb109f99df320972d1ac17e95543957",
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


def result(request):
    return render(request, "result.html", {"days": get_days().items()})
