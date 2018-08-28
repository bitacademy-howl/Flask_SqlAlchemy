import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='stark1234',
                       db='webdb', charset='utf8')

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
# sql = "DESC customer"
# qq = curs.execute(sql)
# print(qq)

# sql = "CREATE TABLE customer (name VARCHAR(30), gender CHAR(10), city VARCHAR(30));"
# curs.execute(sql)

sql = "INSERT INTO customer (name, gender, city) VALUES ('김정수', '남', '서울')"
curs.execute(sql)
# sql = "INSERT INTO customer VALUES ('이희웅', '남, '서울')"
# curs.execute(sql)
sql = "INSERT INTO customer VALUES ('이삐', '남', '춘천')"
curs.execute(sql)
sql = "INSERT INTO customer VALUES ('강수정', '여', '경기')"
curs.execute(sql)

sql = "select * from customer"
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 rows
# print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
# print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')

# Connection 닫기
conn.close()