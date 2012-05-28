#!/bin/bash -e
# Much thanks to http://rsalveti.wordpress.com/2007/04/03/bash-parsing-arguments-with-getopts/ for the getopts tutorial

usage()
{
cat << EOF
usage: $0 options

Given a MySQL root username and password, this script will set up and 
initialize the mentoring match application.

OPTIONS:
   -h      Show this message
   -u      MySQL root username
   -p      MySQL root password
   -m      Manually enter Django superuser credentials 
   
EOF
}


USERNAME=
PASSWORD=
SYNCDBOPTION="--noinput"

# grab all options
while getopts “mhu:p:” OPTION
do
     case $OPTION in
         h)
             usage
             exit 1
             ;;
         u)
             USERNAME=$OPTARG
             ;;
         p)
             PASSWORD=$OPTARG
             ;;
         m)
             SYNCDBOPTION=""
             ;;
         ?)
             usage
             exit
             ;;
     esac
done

#check to make sure all required data is entered
if [[ -z $USERNAME ]] || [[ -z $PASSWORD ]]
then
     echo -e "\tError: Missing username/password.\n"
     usage
     exit 1
fi

#huzzah, everything is awesome. Run the script.
echo "Creating project user and database..."
mysql -u$USERNAME -p$PASSWORD < setupdb.sql

echo "Syncing project to database..."
../mentoringmatch/manage.py syncdb $SYNCDBOPTION
