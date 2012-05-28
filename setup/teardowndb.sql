DROP DATABASE IF EXISTS mentoringmatchdb;
DROP DATABASE IF EXISTS test_mentoringmatchdb;

/*Give silly privelages to mentoringmatch to make sure it exists 
before deleting it* -- silly mysql with its lack of good user existance 
checking*/
GRANT USAGE ON *.* TO 'mentoringmatch'@'%';
DROP USER 'mentoringmatch'@'%';
