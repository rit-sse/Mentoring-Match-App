#!/bin/bash -e

if [ $# -ne 2 ]
then
  echo "Usage: `basename $0` msqlusername mysqlpassword"
  exit -1
fi

echo "Creating project user and database..."
mysql -u$1 -p$2 < setupdb.sql

../mentoringmatch/manage.py syncdb --noinput
