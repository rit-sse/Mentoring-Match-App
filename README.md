Mentoring-Match-App
===================

Matches students to students in order to facilitate learning.

Requirements:
- Python 2.7
- MySQL 5+
- Django 1.4

Setup:
- Set up Python, Django, MySQL (see internet for details)
- Check out repo
- Run setup/dev-setup.sh (creates the database and user on the MySQL side, syncs the django application to the database, autocreates the superuser)

Some notes:
- If you want to wipe all user data, run setup/dev-teardown.sh.
- Options for dev-setup and dev-teardown can be seen with [script] -h.
- Contact Dorrene Brown (deb3323@rit.edu) for the mentoring superuser password if generating from a fixture.
