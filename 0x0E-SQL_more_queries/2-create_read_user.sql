-- create dtabase and user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- give user select privileges
GRANT SELECT ON hbtn_0d_2@localhost;
