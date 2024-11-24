import sqlite3

# Подключаемся к SQLite
conn = sqlite3.connect('reviews.db')
cursor = conn.cursor()

# Запрос на извлечение всех фото
cursor.execute("SELECT id, name, photo FROM reviews")
rows = cursor.fetchall()

# Сохраняем фото в отдельные файлы
for row in rows:
    review_id = row[0]
    name = row[1]
    photo_data = row[2]

    if photo_data:  # Если фото существует
        filename = f"review_{review_id}_{name.replace(' ', '_')}.jpg"
        with open(filename, 'wb') as file:
            file.write(photo_data)
        print(f"Сохранено фото: {filename}")
    else:
        print(f"Отзыв {review_id} ({name}) не содержит фото.")

conn.close()
