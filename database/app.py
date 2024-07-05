from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# اتصال به دیتابیس
def conn():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id,title,tags,description,category,photographer_code,photographer_name,photographer_email FROM Images")
    return cursor.fetchall()
def conn1():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id,content,keywords,title,category,writer_code,writer_name,writer_email FROM Articles")
    return cursor.fetchall()
@app.route('/')
def home():
    # اجرای کوئری برای خواندن اطلاعات از دیتابیس
    data_table1 = conn()
    data_table2 = conn1()

    return render_template('index.html', data_table1=data_table1)
@app.route('/photo')
def photo():
    data_table1=conn()
    return render_template('photo.html', data_table1=data_table1)
@app.route('/articles')    
def Articles():
    data_table2=conn1()
    return render_template('articles.html', data_table2=data_table2)
@app.route('/writers')
def writers():
    data_table2=conn1()
    return render_template('writers.html', data_table2=data_table2)     
app.run(debug=True)
