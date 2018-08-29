########################################################################################################################
# 이건 SQLAlchemy 사용 예제 site 로 부터
########################################################################################################################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# flask-MYSQL 패키지 설치...후 사용 가능
# uri 설정을 변수형태로 할 수 있다.
from flaskext.mysql import MySQL

class Music_DAO():

    app = Flask(__name__)

    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'stark1234'
    app.config['MYSQL_DATABASE_DB'] = 'webdb'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'

    mysql = MySQL()
    mysql.init_app(app)

    db = SQLAlchemy(app)

md = Music_DAO()


conn = md.mysql.connect()
cursor =conn.cursor()

cursor.execute("SELECT * from customer")
cursor.execute("INSERT INTO customer (name, gender, city) VALUE ('강수정', '여', '경기')")

# cursor.
cursor.execute("SELECT * from customer")
data = cursor.fetchone()

print(cursor.fetchall(),"\n")