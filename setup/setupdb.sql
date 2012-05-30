CREATE DATABASE IF NOT EXISTS mentoringmatchdb;

GRANT ALL PRIVILEGES ON mentoringmatchdb.*
TO 'mentoringmatch'@'%' IDENTIFIED BY 'aqeraq66' 
WITH GRANT OPTION;

GRANT ALL PRIVILEGES ON test_mentoringmatchdb.*
TO 'mentoringmatch'@'%' IDENTIFIED BY 'aqeraq66' 
WITH GRANT OPTION;
