USE yes24;

CREATE TABLE Books (
	bookID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    publisher VARCHAR(255),
    publishing DATE, -- DATE 데이터 형식은 날짜 정보를 저장하기에 적합합니다. 예를 들어, 주문일, 생년월일, 계약일 등과 같이 시간 정보가 필요 없는 날짜 데이터를 저장할 때 사용
    rating DECIMAL(3, 1),
    review INT,
    sales INT,
    price DECIMAL(10, 2),
    ranking INT,
    ranking_weeks INT
);
    