import pymysql
from faker import Faker
import random

# Faker 초기화
fake = Faker()

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Clzlsfjqm8*",
    db = "airbnb",
    charset = "utf8mb4",
    cursorclass = pymysql.cursors.DictCursor
)

# Products 테이블을 위한 더미 데이터 생성
def generate_product_data(n):
    for _ in range(n):
        # fake.word() 함수는 무작위 단어를 생성하고, capitalize() 메서드는 문자열의 첫 글자를 대문자로 만듭니다.
        product_name = fake.word().capitalize() + ' ' + fake.word().capitalize()

        # 10에서 100 사이의 랜덤 가격 생성 (소수점 2자리까지)
        price = round(random.uniform(10, 100), 2)
        stock_quantity = random.randint(10, 100) 

        # fake.date_time_this_year() 함수는 올해에 대한 랜덤한 날짜와 시간을 생성
        create_date = fake.date_time_this_year()

        # yield는 함수의 실행 상태를 보존하고 다음 호출 시에 이어서 실행할 수 있도록 하는데, 
        # 이는 메모리 사용을 최적화하면서도 반복 가능한 데이터를 생성하는 데 도움
        yield (product_name, price, stock_quantity, create_date)


def generate_customer_data(n):
    for _ in range(n):
        customer_name = fake.name()
        email = fake.email()
        address = fake.address()
        create_date = fake.date_time_this_year()
        yield (customer_name, email, address, create_date)

def generate_order_data(n, customer_ids):
    for _ in range(n):
        customer_id = random.choice(customer_ids)
        order_date = fake.date_time_this_year()

        # 20에서 500 사이의 랜덤한 가격 생성 (소수점 2자리까지)
        total_amount = round(random.uniform(20, 500), 2)
        yield (customer_id, order_date, total_amount)

# 데이터베이스에 데이터 삽입
with conn.cursor() as cursor:
    # Products 데이터 삽입
    products_sql = "INSERT INTO Products (productName, price, stockQuantity, createDate) VALUES (%s, %s, %s, %s)"
    for data in generate_product_data(10):
        cursor.execute(products_sql, data)
    conn.commit()

    # Customers 데이터 삽입
    customers_sql = "INSERT INTO Customers (customerName, email, address, createDate) VALUES (%s, %s, %s, %s)"
    for data in generate_customer_data(5):
        cursor.execute(customers_sql, data)
    conn.commit()

    # Orders 데이터 삽입
    # Customers 테이블에서 ID 목록을 얻어옵니다.
    cursor.execute("SELECT customerID FROM Customers")
    customer_ids = [row['customerID'] for row in cursor.fetchall()]
    
    orders_sql = "INSERT INTO Orders (customerID, orderDate, totalAmount) VALUES (%s, %s, %s)"
    for data in generate_order_data(15, customer_ids):
        cursor.execute(orders_sql, data)
    conn.commit()

# 데이터베이스 연결 종료
conn.close()