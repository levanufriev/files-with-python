create database task1;

use task1;

CREATE TABLE t( 
Date VARCHAR(10),
Latin VARCHAR(10),
Cyrillic VARCHAR(10),
Intnumber INT,
Floatnumber FLOAT);

select * from t;

call sum_of_ints();
call median();

DELIMITER //

create procedure sum_of_ints() 
BEGIN
	select SUM(Intnumber) from t;
END //

DELIMITER ; 

DELIMITER //

create procedure median() 
BEGIN
	SELECT AVG(dd.Floatnumber) as median_val
	FROM (
	SELECT d.Floatnumber, @rownum:=@rownum+1 as `row_number`, @total_rows:=@rownum
		FROM t d, (SELECT @rownum:=0) r
		WHERE d.Floatnumber is NOT NULL
		ORDER BY d.Floatnumber
		) as dd
WHERE dd.row_number IN ( FLOOR((@total_rows+1)/2), FLOOR((@total_rows+2)/2) );
END //

DELIMITER ; 

    