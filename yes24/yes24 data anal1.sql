-- USE yes24;

-- 기본 조회 및 필터링
-- SELECT title, author FROM books;
-- SELECT * FROM books WHERE rating >= 4
-- SELECT * FROM books WHERE review >= 100 ORDER BY review DESC
-- SELECT * FROM books WHERE sales < 20000
-- SELECT * FROM books WHERE ranking_weeks >= 4 ORDER BY ranking_weeks DESC
-- SELECT title, author FROM books WHERE author = 'ETS 저'
-- SELECT title, publisher FROM books WHERE publisher LIKE 'YBM%'

-- 조인 및 관계
-- 저자별로 출판한 책의 수와 출판사
-- SELECT
--     author,
--     COUNT(*) AS total_books,
--     GROUP_CONCAT(DISTINCT publisher ORDER BY publisher ASC) AS publishers
-- FROM
--     books
-- GROUP BY
--     author;

-- 가장 많은 책을 출판한 출판사
-- SELECT publisher, COUNT(*) AS publishing_count FROM books GROUP BY publisher
-- ORDER BY publishing_count DESC;

-- 가장 높은 평균 평점을 가진 저자 및 타이틀
-- SELECT title, author, AVG(rating) AS rating_avg FROM books GROUP BY author, title

-- 국내도서랭킹이 1위읜 채그이 제목과 저자 조회
-- SELECT title, author FROM books WHERE ranking = 1;

-- 판매지수와 리뷰수가 모두 높은 상위 10개 책 조회
-- SELECT title, sales, review FROM books ORDER BY sales DESC, review DESC LIMIT 10

-- 가장 최근에 출판된 5권의 책 조회
-- SELECT title FROM books ORDER BY publishing DESC LIMIT 5

