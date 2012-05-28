#!/bin/bash -e

if [ $# -ne 2 ]
then
  echo "Usage: `basename $0` mysqlusername mysqlpassword"
  exit -1
fi

echo "Destroying project user and database..."
mysql -u$1 -p$2 < teardowndb.sql
