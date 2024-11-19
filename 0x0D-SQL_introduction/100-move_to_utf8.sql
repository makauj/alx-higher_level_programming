-- convert a database to utf8
ALTER DATABASE `hbtn_0c_0` CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Change character set and collation of first_table
ALTER TABLE `first_table`
	CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Change character set of name field in first_table
ALTER TABLE `first_table`
	MODIFY COLUMN `name` VARCHAR(256) CHARACTER SET utf8mb4_unicode_ci;
