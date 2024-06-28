import oracledb

con = oracledb.connect(user="system", password="1234", dsn="localhost:1521/Oracle_11")
cursor = con.cursor()

def insert(id_num, data):
    cursor.execute(f"insert into kazino_db values({id_num}, {data})")
    con.commit()

def update(id_num, data):
    cursor.execute(f"update kazino_db set coin={data} where id_num={id_num}")
    con.commit()

def select(id_num):
    cursor.execute(f"select coin from kazino_db where id_num={id_num}")
    data = cursor.fetchone()
    print(f"코인 수 {data[0]}, id : {id_num}")

running = True
while running:
    i = input("입력하시오 : ")
    if i == 0:
        running = False

con.close()