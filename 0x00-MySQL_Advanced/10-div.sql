-- create a function safeDiv that divides the first by the second
-- number or return 0 if the second number is equal to 0

DELIMITER $$ ;
CREATE FUNCTION safeDiv(a INT, b INT)
RETURNS FLOAT
NO SQL
BEGIN
	IF b = 0 THEN
		RETURN 0;
	END IF;
	RETURN (a / b);
END;
$$
DELIMITER ;
