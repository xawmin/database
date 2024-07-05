import sqlite3

# اتصال به فایل پایگاه داده SQLite
conn = sqlite3.connect('data.db')

# ایجاد یک cursor برای اجرای کوئری‌ها
cursor = conn.cursor()

# نمایش تمام رکوردهای جدول
cursor.execute('SELECT * FROM Images')
rows = cursor.fetchall()

# چاپ کردن رکوردها
for row in rows:
    print(row)

# بستن اتصال
conn.close()
