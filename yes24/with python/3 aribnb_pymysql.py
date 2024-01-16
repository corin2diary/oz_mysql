import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Clzlsfjqm8*',
    db = 'airbnb',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    # 문제 1: 새로운 제품 추가
    # MySQL의 경우, 파라미터 바인딩에 사용되는 %s는 단순히 값의 자료형에 상관없이 모든 유형의 값을 적절히 처리
    # sql = "INSERT INTO products(productName, price, stockQuantity) VALUES (%s, %s, %s)"
    # cursor.execute(sql, ('Python Book', 10000, 10))

    # # commit() 메서드는 데이터베이스에 대한 모든 변경 사항을 확정 지어 저장하는 역할
    # connection.commit()

    # # 문제 2: 고객 목록 조회
    # cursor.execute("SELECT * FROM products")

    # # execute() 메서드를 통해 SQL 쿼리를 실행하고, fetchall(), fetchone(), fetchmany(size) 등의 메서드를 사용하여 결과를 가져옴
    # for book in cursor.fetchall():
    #     print(book)

    # 문제 3: 제품 재고 업데이트
    sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    cursor.execute(sql, (1, 5)) # productID가 5인거에서 stockQuantity를 1개 빼겠다.
    connection.commit()
    
    # 문제 4: 고객별 총 주문 금액 (foreign key인 customerID를 이용)
    sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
    cursor.execute(sql)
    datas = cursor.fetchall()
    print(datas)

    # 문제 5: 고객 이메일 업데이트
    sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
    cursor.execute(sql, ('update@update.com', 2)) # cutomerID가 2번인 녀석의 이메일을 업데이트 해주겠다
    connection.commit()

    # 문제 6: 주문 취소
    sql = "DELETE FROM orders WHERE orderID = %s"
    cursor.execute(sql, (15))
    connection.commit()

    # 문제 7: 특정 제품 검색
    sql = "SELECT * FROM products WHERE productName LIKE %s" # like는 내가 입력한 단어가 포함되어있는 전체를 찾아줌
    cursor.execute(sql, ('%Book%'))
    datas= cursor.fetchall()

    for data in datas:
        print(data['productName'])
    
    # 문제 8: 특정 고객의 모든 주문 조회
    sql = "SELECT * FROM orders WHERE customerID = %s"
    cursor.execute(sql, (2))
    datas = cursor.fetchall()

    for data in datas:
        print(data)

    # 문제 9: 가장 많이 주문한 고객
    sql = """SELECT customerID, COUNT(*) as orderCount 
            FROM orders GROUP BY customerID 
            ORDER BY orderCount DESC LIMIT 1"""
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)

cursor.close()