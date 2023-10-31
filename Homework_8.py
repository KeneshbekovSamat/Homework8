import sqlite3

from pythonProject.main import conn

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
""")

cursor.execute("INSERT INTO countries (title) VALUES ('Кыргызстан')")
cursor.execute("INSERT INTO countries (title) VALUES ('Германия')")
cursor.execute("INSERT INTO countries (title) VALUES ('Китай')")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries (id)
    )
""")

cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Бишкек', 1)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Ош', 1)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Берлин', 2)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Пекин', 3)")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities (id)
    )
""")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Сыргак', 'Кылычбеков', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Нурсултан', 'Курманбеков', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Аян', 'Илязов', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Автандил', 'Дастанов', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Жаныбек', 'Болотов', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Арлен', 'Асипбеков', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Аяна', 'Жолдошбекова', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Гулиза', 'Токтобекова', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Айыма', 'Батырбекова', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Раяна', 'Эльмирова', 7)")

while True:
    print(
        "Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]}. {city[1]}")

    selected_city_id = input("Введите id города (0 для выхода): ")
    if selected_city_id == "0":
        break

    cursor.execute("""
        SELECT e.first_name, e.last_name, c.title, c.area, co.title
        FROM employees e
        JOIN cities c ON e.city_id = c.id
        JOIN countries co ON c.country_id = co.id
        WHERE c.id = ?
    """, (selected_city_id,))

    employees = cursor.fetchall()
    if not employees:
        print("В данном городе нет сотрудников.")
    else:
        print("Имя  |  Фамилия  |  Город  |  Площадь города  |  Страна")
        for employee in employees:
            print(f"{employee[0]}  |  {employee[1]}  |  {employee[2]}  |  {employee[3]}  |  {employee[4]}")

conn.close()