import pymysql

# 1. 데이터베이스 연결
connection = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Clzlsfjqm8*",
    db = "classicmodels",
    charset = "utf8mb4", # 이모지를 포함한 유니코드를 지원

    # 일반적인 커서(Cursor)는 결과를 튜플의 리스트 형태로 받아옴. 결과에 대한 필드에 접근하기 위해서는 인덱스를 사용
    # DictCursor: DictCursor를 사용하면 결과를 딕셔너리의 리스트 형태로 받음.
    # SSCursor: 집합을 처리할 때 유용함. 모든 결과를 한번에 메모리에 로드하지 않고, 필요할 때마다 서버에서 행을 가져옴
    # SSDictCurosr: SScursor의 기능에 딕셔너리 형식의 결과 반환을 추가
    cursorclass = pymysql.cursors.DictCursor
)

def get_customers():

    # cursor를 사용하여 데이터베이스에 쿼리를 실행
    cursor = connection.cursor()

    # 2. CRUD (selecr * from)
    sql = "SELECT * FROM customers"

    # # execute() 메서드를 통해 SQL 쿼리를 실행하고, fetchall(), fetchone(), fetchmany(size) 등의 메서드를 사용하여 결과를 가져옴
    cursor.execute(sql)

    # fetchall = sql에 해당하는 데이터값 전부 가져오기
    customers = cursor.fetchone()

    print("customers = ", customers)
    print("customerNumber = ", customers['customerNumber'])
    print("customerName = ", customers['customerName'])
    print("country = ", customers['country'])
    cursor.close()

def add_customer():
    # 2. CRUD (insert into)
    cursor = connection.cursor()
    name = 'jinmyeong'
    family_name = 'choi'
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES({10000},'{name}','{family_name}')" # customers에 데이터를 집어넣주겠다.
    cursor.execute(sql)

    # 실제 데이터베이스에 반영해달라는 의미
    connection.commit()
    cursor.close()

# add_customer()

# 3. UPDATE SET 
def update_customer():
    cursor = connection.cursor()
    update_name = 'update_jinmyeong'
    contactLastName = "update_choi"
    sql = f"UPDATE customers SET customerName='{update_name}', contactLastName='{contactLastName}' WHERE customerNumber={10000}"

    cursor.execute(sql)
    connection.commit() # update, delete등 데이터 변화가 있을땐 반드시 commit을 사용해줘야 함.
    cursor.close()

# update_customer()

# 4. DELETE FROM
def delet_customer():
    cursor = connection.cursor()
    sql = f"DELETE FROM customers WHERE customerNumber={10000}"

    cursor.execute(sql)
    connection.commit()
    cursor.close()

delet_customer()