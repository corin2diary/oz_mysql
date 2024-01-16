USE books;

-- 저자별 평균 평점 계산
-- SELECT author, AVG(rating) AS rating_avg FROM books GROUP BY author ORDER BY rating_avg DESC;

-- 출판일별 출간된 책의 수
-- SELECT publishing, COUNT(*) AS publishing_count, title FROM books GROUP BY title, publishing ORDER BY publishing DESC

-- 책 제목별 평균 가격 조회
-- SELECT title, AVG(sales) AS sales_avg FROM books GROUP BY title ORDER BY sales_avg DESC

-- 리뷰수가 가장 많은 상위 5권의 책
-- SELECT title, review FROM books ORDER BY review DESC LIMIT 5 

-- 국내도서랭킹 별 평균 리뷰 수 계산
-- SELECT title, ranking, AVG(review) AS review_avg FROM books GROUP BY title, ranking ORDER BY review_avg DESC

-- 평균 평점보다 높은 평점을 받은 책들을 조회
-- SELECT title, ranking, review, rating FROM books WHERE review > (SELECT AVG(rating) FROM books)

-- 평균 가격보다 비싼 책들의 제목과 가격을 조회
-- SELECT title, price FROM books WHERE price > (SELECT AVG(price) FROM books)

-- 가장 많은 리뷰를 받은 책보다 많은 리뷰를 받은 다른 책들
-- SELECT title, review FROM books WHERE review > (SELECT MAX(review) FROM books)

-- 평균 판매지수보다 낮은 판매지수를 가진 책들을 조회
-- SELECT title, sales FROM books WHERE sales < (SELECT AVG(sales) FROM books)

-- 가장 많이 출판된 저자의 책들 중 최근 출판된 책을 조회
-- SELECT author, title FROM books WHERE author = (SELECT author FROM books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1

-- 특정 책의 가격을 업데이트
-- UPDATE books SET price = 9999 WHERE title LIKE "%한국사%"
-- select * FROM books where title LIKE "%한국사%"

-- 특정 저자의 책 제목을 변경
-- UPDATE books SET title = "서른에 읽는 쇼펜하우어" WHERE author = "강용수 저"
-- SELECT * FROM books

-- 판매 지수가 가장 낮은 책을 데이터베이스에서 삭제
-- SELECT title, sales FROM books WHERE sales = (SELECT MIN(sales) FROM books)
-- DELETE FROM books WHERE sales = (SELECT MIN(sales) FROM (SELECT sales FROM books) AS subquery)

-- 판매지수가 가장 낮은 책을 데이터베이스에서 삭제
-- DELETE FROM books WHERE sales = (SELECT MIN(sales) FROM books)

-- 특정 출판사가 출판한 모든 책의 평점을 1점 증가시키세요
-- UPDATE books set rating = rating +1 where publisher = "웅진하우스"

-- 저자별 평균 평점 및 판매지수를 분석하여 인기있는 저자 추출
-- SELECT author, AVG(rating), AVG(sales) FROM books GROUP BY author ORDER BY AVG(rating) DESC, AVG(sales) DESC

-- 출판일에 따른 책 가격의 변동 추세를 분석
-- SELECT publishing, AVG(price) FROM books GROUP BY publishing ORDER BY publishing

-- 출판사별 출간된 책의 수와 평균 리뷰 수를 비교 분석
-- SELECT publisher, COUNT(*) AS book_count, SUM(review) AS review_sum FROM books GROUP BY publisher ORDER BY book_count DESC

-- 국내도서랭킹과 판매지수의 상관관계를 분석
-- SELECT ranking, AVG(sales) FROM books GROUP BY ranking

-- 가격대비 리뷰수와 평점의 관계를 분석하여 가성비 좋은책을 추출
-- SELECT title, price, AVG(review), AVG(rating) FROM books GROUP BY title, price

-- 출판사별 평균 판매지수가 가장 높은 저자 찾기
-- SELECT publisher, author, AVG(sales) as avg_sales FROM books GROUP BY publisher, author ORDER BY publisher, avg_sales DESC

-- 리뷰수가 평균보다 높으면서 가격이 평균보다 낮은 책 조회
-- SELECT title, review, price FROM books WHERE review > (SELECT AVG(review) FROM books) AND price < (SELECT AVG(price) FROM books)

-- 가장 많은 종류의 책을 출판한 저자 찾기
-- DISTINCT 명령어는 데이터베이스에서 중복된 값을 제거하여 고유한 값만을 반환하도록 하는 명령어
-- SELECT author, COUNT(DISTINCT title) as num_books FROM books GROUP BY author ORDER BY num_books DESC LIMIT 1 

-- 각 저자별로 가장 높은 판매지수를 기록한 책 찾기
-- SELECT title, author, MAX(sales) AS max_sales FROM books GROUP BY author, title

-- 연도별 출판된 책 수와 평균 가격 비교
-- YEAR() 함수는 MySQL과 같은 데이터베이스에서 날짜 데이터로부터 연도를 추출하는 함수
-- SELECT YEAR(publishing) as year, COUNT(*) as num_books, AVG(price) as price_avg FROM books GROUP BY year

-- 출판사가 같은 책들 중 평점 편차가 가장 큰 출판사 찾기
-- SELECT publisher, MAX(rating) - MIN(rating) as rating_difference FROM books GROUP BY publisher ORDER BY rating_difference DESC LIMIT 1

-- 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책 찾기
-- SELECT title, rating/sales as ration FROM books WHERE author = "ETS 저" LIMIT 1