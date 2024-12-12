import psycopg2
import csv

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="phonebook",
            user="postgres",
            password="1234",
            host="localhost",
            port="5433"
        )
        print("Соединение с базой данных установлено.")
        return conn
    except psycopg2.Error as e:
        print("Ошибка подключения к базе данных:", e)
        return None

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            phone_number VARCHAR(15) UNIQUE NOT NULL
        );
        """)
        conn.commit()
        print("Таблица PhoneBook создана.")
    except psycopg2.Error as e:
        print("Ошибка создания таблицы:", e)

# Функция для поиска записей по шаблону
def search_by_pattern(conn, pattern):
    try:
        cursor = conn.cursor()
        query = """
        SELECT * FROM PhoneBook 
        WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone_number ILIKE %s;
        """
        cursor.execute(query, (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
        rows = cursor.fetchall()
        print("Результаты поиска:")
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Телефон: {row[3]}")
    except psycopg2.Error as e:
        print("Ошибка поиска:", e)

# Процедура для вставки или обновления пользователя
def upsert_user(conn, first_name, last_name, phone_number):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO PhoneBook (first_name, last_name, phone_number)
        VALUES (%s, %s, %s)
        ON CONFLICT (first_name, last_name) DO UPDATE
        SET phone_number = EXCLUDED.phone_number;
        """, (first_name, last_name, phone_number))
        conn.commit()
        print(f"Данные обновлены: {first_name} {last_name}, {phone_number}.")
    except psycopg2.Error as e:
        print("Ошибка при обновлении/добавлении данных:", e)


# Процедура для массового добавления пользователей
def bulk_insert_users(conn, user_list):
    try:
        cursor = conn.cursor()
        incorrect_data = []
        for user in user_list:
            first_name, last_name, phone_number = user
            if len(phone_number) >10 or not phone_number.isdigit():
                incorrect_data.append(user)
                continue
            try:
                cursor.execute("""
                INSERT INTO PhoneBook (first_name, last_name, phone_number)
                VALUES (%s, %s, %s)
                ON CONFLICT (phone_number) DO NOTHING;
                """, (first_name, last_name, phone_number))
            except psycopg2.Error as e:
                incorrect_data.append(user)
        conn.commit()
        print("Массовое добавление пользователей выполнено.")
        if incorrect_data:
            print("Некорректные данные:", incorrect_data)
    except psycopg2.Error as e:
        print("Ошибка массового добавления:", e)

# Функция для пагинации
def get_paginated_records(conn, limit, offset):
    try:
        cursor = conn.cursor()
        query = """
        SELECT * FROM PhoneBook
        ORDER BY id
        LIMIT %s OFFSET %s;
        """
        cursor.execute(query, (limit, offset))
        rows = cursor.fetchall()
        print("Записи (с пагинацией):")
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Телефон: {row[3]}")
    except psycopg2.Error as e:
        print("Ошибка пагинации:", e)
    
def update_data(conn):
    try:
        id_to_update = int(input("Введите ID записи для изменения: "))
        print("Выберите, что вы хотите обновить:")
        print("1. Имя")
        print("2. Фамилию")
        print("3. Номер телефона")
        choice = input("Ваш выбор: ")

        if choice == "1":
            new_value = input("Введите новое имя: ")
            column = "first_name"
        elif choice == "2":
            new_value = input("Введите новую фамилию: ")
            column = "last_name"
        elif choice == "3":
            new_value = input("Введите новый номер телефона: ")
            column = "phone_number"
        else:
            print("Неверный выбор.")
            return

        cursor = conn.cursor()
        query = f"UPDATE PhoneBook SET {column} = %s WHERE id = %s;"
        cursor.execute(query, (new_value, id_to_update))
        conn.commit()
        print(f"Данные обновлены: ID={id_to_update}, {column}={new_value}.")
    except Exception as e:
        print("Ошибка обновления данных:", e)


# Процедура для удаления записи по имени или телефону
def delete_by_name_or_phone(conn, value):
    try:
        cursor = conn.cursor()
        query = """
        DELETE FROM PhoneBook
        WHERE first_name = %s OR last_name = %s OR phone_number = %s;
        """
        cursor.execute(query, (value, value, value))
        conn.commit()
        print(f"Записи с именем, фамилией или номером '{value}' удалены.")
    except psycopg2.Error as e:
        print("Ошибка удаления записей:", e)
def select_data(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PhoneBook ORDER BY id asc;")
        rows = cursor.fetchall()
        print("Данные в таблице:")
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Телефон: {row[3]}")
    except psycopg2.Error as e:
        print("Ошибка запроса данных:", e)

# Меню для управления данными
def menu(conn):
    while True:
        print("\nМеню:")
        print("1. Показать все записи")
        print("2. Добавить новую запись")
        print("3. Загрузить данные из CSV")
        print("4. Изменить запись")
        print("5. Удалить запись")
        print("6. Поиск по шаблону")
        print("7. Массовое добавление")
        print("8. Показ с пагинацией")
        print("9. Удаление по имени или телефону")
        print("10. Выйти")
        choice = input("Ваш выбор: ")

        if choice == "1":
            select_data(conn)
        elif choice == "2":
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            phone_number = input("Введите номер телефона: ")
            upsert_user(conn, first_name, last_name, phone_number)
        elif choice == "3":
            file_path = input("Введите путь к CSV-файлу: ")
            bulk_insert_users(conn, file_path)
        elif choice == "4":
            update_data(conn)
        elif choice == "5":
            delete_by_name_or_phone(conn)
        elif choice == "6":
            pattern = input("Введите шаблон для поиска: ")
            search_by_pattern(conn, pattern)
        elif choice == "7":
            user_count = int(input("Введите количество пользователей для добавления: "))
            user_list = []
            for _ in range(user_count):
                first_name = input("Имя: ")
                last_name = input("Фамилия: ")
                phone_number = input("Номер телефона: ")
                user_list.append((first_name, last_name, phone_number))
            bulk_insert_users(conn, user_list)
        elif choice == "8":
            limit = int(input("Введите количество записей на странице: "))
            offset = int(input("Введите смещение: "))
            get_paginated_records(conn, limit, offset)
        elif choice == "9":
            value = input("Введите имя, фамилию или телефон для удаления: ")
            delete_by_name_or_phone(conn, value)
        elif choice == "10":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

# Основной код
if __name__ == "__main__":
    connection = connect_to_db()
    if connection:
        create_table(connection)
        menu(connection)
        connection.close()
        print("Соединение с базой данных закрыто.")