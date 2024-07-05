import sqlite3
import csv

# اتصال به دیتابیس
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# ایجاد جدول برای اطلاعات CSV
cursor.execute('''CREATE TABLE IF NOT EXISTS Images (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               image_path TEXT,
               title TEXT,
               tags  TEXT,
               description TEXT,
               category TEXT,
               photographer_code TEXT,
               photographer_name TEXT,
               photographer_email TEXT
               )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Articles (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               content TEXT,
               keywords TEXT,
               title TEXT,
               category TEXT,
               writer_code TEXT,
               writer_name TEXT,
               writer_email TEXT
               )''')
# خواندن اطلاعات از فایل CSV و وارد کردن آن به دیتابیس
with open('Images.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # عبور از هدر فایل CSV

    for row in csv_reader:
        cursor.execute("REPLACE INTO Images (image_path, title, tags,description,category,photographer_code,photographer_name,photographer_email) VALUES (?, ?, ?,?,?,?,?,?)", (row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7]))

with open('Articles.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # عبور از هدر فایل CSV

    for row in csv_reader:
        cursor.execute("REPLACE INTO Articles (content, keywords, title,category,writer_code,writer_name,writer_email) VALUES (?, ?, ?,?,?,?,?)", (row[0], row[1], row[2],row[3],row[4],row[5],row[6]))


# اعمال تغییرات و ذخیره داده‌ها
conn.commit()

# بستن اتصال
conn.close()
